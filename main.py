#!/usr/bin/env python3
"""Monday, Reviewed in One Line — make.fun entry. Writes one Monday review to /output/entry.txt."""
import os

ENTRY = "Monday review: deployed on Friday, paged at 3 a.m., and the postmortem blamed 'the intern' — I am the intern."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()

# Deterministic: same single line on every run, no network, no randomness.
