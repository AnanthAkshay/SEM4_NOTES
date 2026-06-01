# -*- coding: utf-8 -*-
"""Fix structure and diagram placement for experiments 10-12."""
import os
import re

LAB = r"a:\SEM4_Complete\DBMS_LAB"

ER_BLOCK = """
## ER DIAGRAM

### ER Diagram (Figure)
![ER Diagram](er_diagram.png)

*Figure: Entity–Relationship diagram (Chen notation). PK = Primary Key, FK = Foreign Key.*

---

"""

SCHEMA_BLOCK = """
## SCHEMA DIAGRAM

### Schema Diagram (Figure)
![Schema Diagram](schema_diagram.png)

*Figure: Relational schema with referential links. Orange = PK, Blue = FK.*

---

"""


def remove_early_schema(text: str) -> str:
    return re.sub(
        r"\n## SCHEMA DIAGRAM\s*\n+### Schema Diagram \(Figure\).*?---\s*\n+",
        "\n",
        text,
        count=1,
        flags=re.DOTALL,
    )


def remove_trailing_patch(text: str) -> str:
    # Remove duplicate THEORY block appended at end (from patch_dbms_exp_9_12)
    m = re.search(r"\n---\s*\n+\s*---\s*\n+\s*## THEORY\n", text)
    if m:
        text = text[: m.start()] + "\n"
    # Also cut from standalone ## THEORY at end if duplicate
    parts = text.split("\n## RESULT\n")
    if len(parts) > 1:
        before_result = parts[0]
        result_part = "## RESULT\n" + parts[1]
        if before_result.rstrip().endswith("---") or "## THEORY" in before_result[-2000:]:
            # find last proper section before duplicate theory
            idx = before_result.rfind("\n## STEP-BY-STEP")
            if idx == -1:
                idx = before_result.rfind("\n## TRIGGER")
            if idx == -1:
                idx = before_result.rfind("\n## CURSOR")
            if idx != -1:
                # keep up to end of viva before duplicate
                end = before_result.find("\n---\n", idx)
                if end != -1:
                    tail = before_result[end:]
                    if "## THEORY" in tail:
                        before_result = before_result[:idx] + "\n\n---\n\n" + result_part.split("## RESULT\n", 1)[-1]
                        text = before_result + "\n## RESULT\n" + parts[1]
    return text


def insert_diagrams_after_problem(text: str) -> str:
    if "## ER DIAGRAM" in text:
        return text
    anchor = "## PROBLEM STATEMENT"
    if anchor not in text:
        return text
    # Find end of problem section (next ##)
    pos = text.find(anchor)
    nxt = text.find("\n## ", pos + 10)
    if nxt == -1:
        return text
    insert = (
        "\n\n## OBJECTIVES\n"
        "1. Execute MongoDB queries on boat reservation data.\n"
        "2. Implement Oracle weekend modification trigger on EMPLOYEE.\n"
        "3. Interpret trigger errors and MongoDB aggregation results.\n\n---\n"
        + ER_BLOCK
        + SCHEMA_BLOCK
    )
    # Only for exp 10 - vary by file in caller
    return text[:nxt] + insert + text[nxt:]


def fix_file(folder: str, objectives: str, entity_md: str, constraints_md: str):
    path = os.path.join(LAB, folder)
    mds = [f for f in os.listdir(path) if f.endswith(".md")]
    if not mds:
        return
    fp = os.path.join(path, mds[0])
    with open(fp, "r", encoding="utf-8") as f:
        text = f.read()

    text = remove_early_schema(text)
    text = remove_trailing_patch(text)
    text = re.sub(r"\*Figure: Relational schema.*?\n(\*Figure: Relational schema.*?\n)?", "", text)

    if "## ER DIAGRAM" not in text:
        anchor = "## PROBLEM STATEMENT"
        pos = text.find(anchor)
        nxt = text.find("\n## ", pos + 15)
        block = (
            f"\n\n## OBJECTIVES\n{objectives}\n\n---\n"
            f"\n## ENTITY IDENTIFICATION\n{entity_md}\n\n---\n"
            f"\n## CONSTRAINTS\n{constraints_md}\n\n---\n"
            + ER_BLOCK
            + SCHEMA_BLOCK
        )
        text = text[:nxt] + block + text[nxt:]

    # Ensure RESULT at end only once
    text = re.sub(r"(## RESULT\n.+?)\n+## THEORY", r"\1", text, flags=re.DOTALL)

    with open(fp, "w", encoding="utf-8") as f:
        f.write(text.strip() + "\n")
    print(f"Fixed {fp}")


if __name__ == "__main__":
    fix_file(
        "Experiment_10_MongoDB_Boat_Sailor_Weekend_Trigger",
        "1. Query boat reservations in MongoDB.\n2. Create weekend block trigger on EMPLOYEE.\n3. Test trigger with INSERT on weekday/weekend.",
        "| Entity | Attributes | PK |\n|--------|------------|-----|\n| SAILOR | SID, SName, Rating, Age | SID |\n| BOAT | BID, BName, Color | BID |\n| RESERVES | SID, BID, Day | (SID,BID,Day) |",
        "Domain: Rating 1–10; Age > 0. Referential: RESERVES → SAILOR, BOAT. Cardinality: M:N.",
    )
    fix_file(
        "Experiment_11_MongoDB_Customer_Branch_Cursor",
        "1. Query branches and customer accounts in MongoDB.\n2. Copy Oracle table using explicit cursor.\n3. Compare cursor vs INSERT-SELECT.",
        "| Entity | Attributes | PK |\n|--------|------------|-----|\n| BRANCH | branch_id, branch_name, city | branch_id |\n| CUSTOMER | cust_id, cust_name, accounts[] | cust_id |",
        "Logical FK: accounts.branch_id → branches. Embedded accounts in MongoDB.",
    )
    fix_file(
        "Experiment_12_MongoDB_Books_Student_Exception",
        "1. Query books and borrows in MongoDB.\n2. Implement user-defined exception e_bigger in PL/SQL.\n3. Handle exception with custom message.",
        "| Entity | Attributes | PK |\n|--------|------------|-----|\n| BOOKS | ISBN, Title, Author, Publisher | ISBN |\n| STUDENT | SID, SName, Gender, borrows[] | SID |",
        "Partial participation: students may have zero borrows. M:N via borrows array.",
    )
