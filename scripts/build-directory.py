#!/usr/bin/env python3
"""Generate tracked catalog views from data/resources.json. Use --check in CI."""
import argparse
import csv
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = {'llm': 'LLM APIs', 'local': 'Local tools', 'models': 'Open models', 'coding': 'Coding assistants', 'image': 'Image & video', 'hosting': 'Hosting', 'rag': 'Embeddings & RAG', 'audio': 'Speech & audio', 'agents': 'Agents & workflows'}

def render():
    rows = json.loads((ROOT / 'data/resources.json').read_text())
    reviewed = [r for r in rows if r['verification'] == 'docs-reviewed']
    lines = [f'**{len(rows)} resources · {len(reviewed)} docs reviewed · {len(rows)-len(reviewed)} awaiting review.** Counts are generated from the catalog.', '']
    for category, title in CATEGORIES.items():
        group = [r for r in reviewed if r['category'] == category]
        if not group:
            continue
        lines += [f'### {title}', '', '| Resource | Access | Useful for / limitations | Source checked |', '|---|---|---|---|']
        for r in group:
            desc = (r['summary'] + ' ' + r['limits']).replace('|', '\\|').replace('\n', ' ')
            lines.append(f"| [{r['name']}]({r['url']}) | {r['kind']} · card: {r['card']} | {desc} | [Official source]({r['source']}) · {r['reviewed']} |")
        lines.append('')
    pending = [r for r in rows if r['verification'] != 'docs-reviewed']
    lines += ['<details>', '<summary>Earlier entries awaiting a fresh review</summary>', '', 'These are candidates, not confirmed free recommendations. Help check one against its current official terms.', '', '| Resource | Category | Status |', '|---|---|---|']
    lines += [f"| [{r['name']}]({r['url']}) | {CATEGORIES[r['category']]} | Needs review |" for r in pending]
    lines += ['', '</details>']
    readme = (ROOT / 'README.md').read_text()
    start, rest = readme.split('<!-- CATALOG:START -->')
    _, end = rest.split('<!-- CATALOG:END -->')
    readme = start + '<!-- CATALOG:START -->\n' + '\n'.join(lines) + '\n<!-- CATALOG:END -->' + end
    out = io.StringIO(newline='')
    fields = list(rows[0])
    writer = csv.DictWriter(out, fieldnames=fields, lineterminator='\n')
    writer.writeheader()
    for r in rows:
        writer.writerow({**r, 'tags': ', '.join(r['tags'])})
    return {'README.md': readme, 'data/resources.csv': out.getvalue(), 'assets/catalog-data.js': 'window.AI_RESOURCES = ' + json.dumps(rows, ensure_ascii=False, indent=2) + ';\n'}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    stale = []
    for path, content in render().items():
        target = ROOT / path
        if args.check:
            if not target.exists() or target.read_text() != content:
                stale.append(path)
        else:
            target.write_text(content)
    if stale:
        raise SystemExit('Regenerate catalog: python3 scripts/build-directory.py\n' + '\n'.join(stale))
    print('Catalog views are current.' if args.check else 'Generated README, CSV and browser data.')

if __name__ == '__main__':
    main()
