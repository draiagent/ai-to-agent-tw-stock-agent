"""Build or verify a complete SHA-256 manifest using the Python standard library."""
import hashlib, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'SHA256SUMS.json'
def inventory():
    return {f.relative_to(ROOT).as_posix(): hashlib.sha256(f.read_bytes()).hexdigest()
            for f in sorted(ROOT.rglob('*')) if f.is_file() and f != MANIFEST
            and not {'.git', '__pycache__'}.intersection(f.relative_to(ROOT).parts)}
def main():
    if len(sys.argv) != 2 or sys.argv[1] not in {'build', 'verify'}:
        print('Usage: python scripts/checksums.py build|verify'); return 2
    actual = inventory()
    if sys.argv[1] == 'build':
        MANIFEST.write_text(json.dumps(actual, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
        print(f'Built {len(actual)} hashes'); return 0
    expected = json.loads(MANIFEST.read_text(encoding='utf-8'))
    failures = sorted(k for k in set(actual) | set(expected) if actual.get(k) != expected.get(k))
    for k in failures: print('FAIL:', k)
    print('FAIL' if failures else f'PASS: {len(actual)} files')
    return 1 if failures else 0
if __name__ == '__main__': raise SystemExit(main())
