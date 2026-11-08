"""Compare a DNS record's value across several resolvers.

Usage: python3 main.py records.csv
CSV columns: resolver,record,value.
A record is CONSISTENT when every resolver returns the same value,
otherwise DIFFERS, with the resolvers that disagree listed.
Records that differ are shown first.
"""
import argparse, csv, sys
from collections import Counter, defaultdict

def check(rows):
    by_record = defaultdict(list)
    for row in rows:
        by_record[row["record"].strip()].append((row["resolver"].strip(), row["value"].strip()))
    out = []
    for record in sorted(by_record):
        answers = by_record[record]
        values = Counter(v for _, v in answers)
        if len(values) == 1:
            out.append((record, "CONSISTENT", answers, None))
        else:
            common = values.most_common(1)[0][0]
            differing = [r for r, v in answers if v != common]
            out.append((record, "DIFFERS", answers, differing))
    return sorted(out, key=lambda r: r[1] == "CONSISTENT")

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        for record, verdict, answers, differing in check(list(csv.DictReader(f))):
            detail = ", ".join(f"{r}={v}" for r, v in answers)
            extra = f" (differs at: {', '.join(differing)})" if differing else ""
            print(f"{record}: {verdict} ({detail}){extra}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
