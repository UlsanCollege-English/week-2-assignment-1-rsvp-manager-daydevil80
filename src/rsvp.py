"""RSVP Manager — Starter

You are cleaning up RSVP emails for an event.

Implement the three functions below without mutating inputs.
"""
from typing import List, Tuple

def dedupe_emails_case_preserve_order(emails: List[str]) -> List[str]:
    result = []
    seen = []
    for e in emails:
        if "@" not in e:
            continue
        low = e.lower()
        if low not in seen:
            seen.append(low)
            result.append(e)
    return result


def first_with_domain(emails: List[str], domain: str) -> int | None:
    domain = domain.lower()
    for i in range(len(emails)):
        if "@" not in emails[i]:
            continue
        parts = emails[i].split("@")
        if parts[1].lower() == domain:
            return i
    return None


def domain_counts(emails: List[str]) -> List[Tuple[str, int]]:
    counts = {}
    for e in emails:
        if "@" not in e:
            continue
        parts = e.split("@")
        dom = parts[1].lower()
        if dom in counts:
            counts[dom] += 1
        else:
            counts[dom] = 1

    # convert dict to list of tuples and sort
    result = list(counts.items())
    result.sort(key=lambda x: x[0])
    return result
