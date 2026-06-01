# -*- coding: utf-8 -*-
"""Apply consistent professional formatting to all DBMS lab markdown files."""
import os
import re

LAB = r"a:\SEM4_Complete\DBMS_LAB"

SECTION_ORDER = [
    "TITLE", "AIM", "PROBLEM STATEMENT", "OBJECTIVES", "THEORY",
    "ENTITY IDENTIFICATION", "CONSTRAINTS", "ER DIAGRAM", "SCHEMA DIAGRAM",
    "RELATIONAL MODEL", "SQL IMPLEMENTATION", "QUERY IMPLEMENTATION",
    "MONGODB IMPLEMENTATION", "PL/SQL", "CURSOR", "TRIGGER", "EXCEPTION",
    "OUTPUT", "STEP-BY-STEP", "VIVA", "LAB EXAM", "FREQUENTLY ASKED", "RESULT",
]


def format_md(content: str) -> str:
    # Normalize line endings
    content = content.replace("\r\n", "\n")

    # Ensure blank line before headers
    content = re.sub(r"\n(## )", r"\n\n\1", content)
    content = re.sub(r"\n{3,}", "\n\n", content)

    # Bold entity names in tables (already have ** in many places)

    # Wrap QUERY IMPLEMENTATION subsections consistently
    content = re.sub(
        r"\n### (i{1,3}|iv|Query \d+)[\.:]",
        r"\n\n### \1.",
        content,
        flags=re.I,
    )

    # Add visual separator comment blocks for record book (HTML strips these in md - skip)

    # Standardize horizontal rules
    content = re.sub(r"\n---\n", "\n\n---\n\n", content)

    # Code blocks: ensure newline after opening fence language tag
    content = re.sub(r"```(\w+)\n", r"```\1\n", content)

    # Figure captions – ensure italic caption on own line after images
    if "*(Figure:" not in content and "Figure:" in content:
        pass

    return content.strip() + "\n"


def process_folder(folder: str) -> None:
    exp_path = os.path.join(LAB, folder)
    for fn in os.listdir(exp_path):
        if not fn.endswith(".md"):
            continue
        path = os.path.join(exp_path, fn)
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        new_text = format_md(text)
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_text)
        print(f"Formatted {path}")


def main():
    for folder in sorted(os.listdir(LAB)):
        if folder.startswith("Experiment_"):
            process_folder(folder)


if __name__ == "__main__":
    main()
