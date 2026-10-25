#!/usr/bin/env python3
"""Availability probe only. A successful URL never updates a review date."""
import concurrent.futures
import json
import urllib.error
import urllib.request
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def probe(url):
    request = urllib.request.Request(url, headers={'User-Agent': 'Free-AI-Bible-Link-Check/1.0'})
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            response.read(1024)
            return {'url': url, 'status': response.status, 'result': 'reachable'}
    except urllib.error.HTTPError as exc:
        return {'url': url, 'status': exc.code, 'result': 'manual-review' if exc.code in (401, 403, 429) else 'error'}
    except Exception as exc:
        return {'url': url, 'status': None, 'result': 'error', 'detail': str(exc)}

def main():
    rows = json.loads((ROOT/'data/resources.json').read_text())
    urls = sorted({r['source'] for r in rows})
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        report = list(pool.map(probe, urls))
    (ROOT/'link-report.json').write_text(json.dumps(report, indent=2)+'\n')
    for row in report:
        if row['result'] != 'reachable':
            print(row['result'], row['status'], row['url'])
    print(f"Checked {len(urls)} sources; see link-report.json. Reachability does not prove free access.")
    if any(r['result'] == 'error' for r in report):
        raise SystemExit(1)
if __name__ == '__main__':
    main()
