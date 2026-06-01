# -*- coding: utf-8 -*-
"""
Generate ER and Schema diagram PNGs for all DBMS lab experiments.
Updates markdown files to embed images.
"""
from __future__ import annotations

import copy
import os
import re
from dataclasses import dataclass, field

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

LAB = r"a:\SEM4_Complete\DBMS_LAB"

# Colors – print-friendly on white
C_ENTITY = "#1e40af"
C_REL = "#7c3aed"
C_TABLE_HDR = "#0f766e"
C_PK = "#b45309"
C_FK = "#0369a1"
C_TEXT = "#0f172a"
C_LINE = "#475569"
C_BG = "#ffffff"


@dataclass
class Entity:
    name: str
    attrs: list[str]
    x: float
    y: float
    w: float = 2.2
    h: float = None

    def __post_init__(self):
        if self.h is None:
            self.h = 0.35 + 0.28 * len(self.attrs)


@dataclass
class Rel:
    label: str
    x: float
    y: float
    w: float = 1.4
    h: float = 0.55


@dataclass
class Edge:
    fr: str
    to: str
    label: str = ""
    card: str = ""


@dataclass
class Table:
    name: str
    cols: list[tuple[str, str]]  # (name, PK|FK|)
    x: float
    y: float


@dataclass
class SchemaEdge:
    fr: str
    to: str
    fr_col: str
    to_col: str


@dataclass
class DiagramSet:
    title: str
    entities: list[Entity] = field(default_factory=list)
    rels: list[Rel] = field(default_factory=list)
    edges: list[Edge] = field(default_factory=list)
    tables: list[Table] = field(default_factory=list)
    schema_edges: list[SchemaEdge] = field(default_factory=list)


def _entity_centers(entities: list[Entity]) -> dict[str, tuple[float, float]]:
    return {e.name: (e.x + e.w / 2, e.y + e.h / 2) for e in entities}


def draw_er(ds: DiagramSet, path: str) -> None:
    fig, ax = plt.subplots(figsize=(14, 9), facecolor=C_BG)
    ax.set_facecolor(C_BG)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis("off")
    ax.set_title(ds.title + " — ER Diagram", fontsize=16, fontweight="bold", color=C_TEXT, pad=16)

    centers = {}

    for e in ds.entities:
        box = FancyBboxPatch(
            (e.x, e.y),
            e.w,
            e.h,
            boxstyle="round,pad=0.04,rounding_size=0.08",
            linewidth=2,
            edgecolor=C_ENTITY,
            facecolor="#eff6ff",
        )
        ax.add_patch(box)
        ax.text(e.x + e.w / 2, e.y + e.h - 0.22, e.name, ha="center", va="top", fontsize=11, fontweight="bold", color=C_ENTITY)
        for i, a in enumerate(e.attrs):
            ax.text(e.x + 0.12, e.y + e.h - 0.55 - i * 0.28, a, ha="left", va="top", fontsize=8.5, color=C_TEXT, family="monospace")
        centers[e.name] = (e.x + e.w / 2, e.y + e.h / 2)

    for r in ds.rels:
        diamond = plt.Polygon(
            [
                (r.x, r.y + r.h / 2),
                (r.x + r.w / 2, r.y),
                (r.x + r.w, r.y + r.h / 2),
                (r.x + r.w / 2, r.y + r.h),
            ],
            closed=True,
            facecolor="#f5f3ff",
            edgecolor=C_REL,
            linewidth=1.8,
        )
        ax.add_patch(diamond)
        ax.text(r.x + r.w / 2, r.y + r.h / 2, r.label, ha="center", va="center", fontsize=8, color=C_REL, fontweight="bold")
        centers[f"__{r.label}__"] = (r.x + r.w / 2, r.y + r.h / 2)

    def pt(name: str):
        if name.startswith("__"):
            return centers[name]
        return centers[name]

    for ed in ds.edges:
        if ed.fr not in centers or ed.to not in centers:
            continue
        x1, y1 = pt(ed.fr)
        x2, y2 = pt(ed.to)
        ax.annotate(
            "",
            xy=(x2, y2),
            xytext=(x1, y1),
            arrowprops=dict(arrowstyle="-", color=C_LINE, lw=1.5, connectionstyle="arc3,rad=0.1"),
        )
        if ed.label or ed.card:
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            ax.text(mx, my + 0.15, f"{ed.label} {ed.card}".strip(), ha="center", fontsize=7.5, color=C_LINE, style="italic")

    fig.tight_layout()
    fig.savefig(path, dpi=200, bbox_inches="tight", facecolor=C_BG)
    plt.close(fig)


def draw_schema(ds: DiagramSet, path: str) -> None:
    fig, ax = plt.subplots(figsize=(14, 9), facecolor=C_BG)
    ax.set_facecolor(C_BG)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis("off")
    ax.set_title(ds.title + " — Schema Diagram", fontsize=16, fontweight="bold", color=C_TEXT, pad=16)

    tw, line_h, hdr_h = 2.8, 0.32, 0.45
    boxes = {}

    for t in ds.tables:
        th = hdr_h + len(t.cols) * line_h + 0.15
        box = FancyBboxPatch(
            (t.x, t.y),
            tw,
            th,
            boxstyle="round,pad=0.03,rounding_size=0.06",
            linewidth=2,
            edgecolor=C_TABLE_HDR,
            facecolor="#f0fdfa",
        )
        ax.add_patch(box)
        ax.add_patch(
            FancyBboxPatch(
                (t.x, t.y + th - hdr_h),
                tw,
                hdr_h,
                boxstyle="round,pad=0.02,rounding_size=0.06",
                linewidth=0,
                facecolor=C_TABLE_HDR,
            )
        )
        ax.text(t.x + tw / 2, t.y + th - hdr_h / 2, t.name, ha="center", va="center", fontsize=10, fontweight="bold", color="white")
        for i, (col, kind) in enumerate(t.cols):
            yy = t.y + th - hdr_h - 0.28 - i * line_h
            color = C_PK if kind == "PK" else C_FK if kind == "FK" else C_TEXT
            prefix = {"PK": "PK ", "FK": "FK ", "": ""}[kind]
            ax.text(t.x + 0.1, yy, prefix + col, ha="left", va="top", fontsize=8.5, color=color, family="monospace", fontweight="bold" if kind else "normal")
        boxes[t.name] = (t.x + tw / 2, t.y + th / 2, tw, th)

    for se in ds.schema_edges:
        if se.fr not in boxes or se.to not in boxes:
            continue
        x1, y1, _, _ = boxes[se.fr]
        x2, y2, _, _ = boxes[se.to]
        ax.annotate(
            "",
            xy=(x2, y2),
            xytext=(x1, y1),
            arrowprops=dict(arrowstyle="->", color=C_FK, lw=1.8, connectionstyle="arc3,rad=0.15"),
        )
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        ax.text(mx, my, f"{se.fr_col}→{se.to_col}", ha="center", fontsize=7, color=C_FK)

    # Legend
    leg = [
        mpatches.Patch(color=C_PK, label="Primary Key"),
        mpatches.Patch(color=C_FK, label="Foreign Key"),
    ]
    ax.legend(handles=leg, loc="lower right", fontsize=9, framealpha=0.95)

    fig.tight_layout()
    fig.savefig(path, dpi=200, bbox_inches="tight", facecolor=C_BG)
    plt.close(fig)


def all_diagrams() -> dict[int, DiagramSet]:
    """Return diagram specs keyed by experiment number."""
    d = {}

    d[1] = DiagramSet(
        "Exp 1: Employee – Department – Project",
        entities=[
            Entity("EMPLOYEE", ["SSN (PK)", "Name, Address", "Sex, Salary", "SuperSSN (FK)", "DNo (FK)"], 1, 5.5),
            Entity("DEPARTMENT", ["DNo (PK)", "DName", "MgrSSN (FK)", "MgrStartDate"], 5.5, 6.2),
            Entity("PROJECT", ["PNo (PK)", "PName, PLocation", "Domain", "DNo (FK)"], 9.5, 5.5),
            Entity("WORKS_ON", ["SSN (PK,FK)", "PNo (PK,FK)", "Hours"], 5.5, 2.5),
        ],
        rels=[
            Rel("works_in", 3.5, 5.8),
            Rel("manages", 4.8, 6.8, 1.2, 0.5),
            Rel("controls", 7.8, 6.0),
            Rel("works_on", 4.0, 4.2),
            Rel("supervises", 1.5, 4.5, 1.2, 0.5),
        ],
        edges=[
            Edge("EMPLOYEE", "__works_in__", "", "N"),
            Edge("__works_in__", "DEPARTMENT", "", "1"),
            Edge("EMPLOYEE", "__manages__"),
            Edge("__manages__", "DEPARTMENT"),
            Edge("DEPARTMENT", "__controls__", "", "1"),
            Edge("__controls__", "PROJECT", "", "N"),
            Edge("EMPLOYEE", "__works_on__", "", "M"),
            Edge("__works_on__", "WORKS_ON"),
            Edge("PROJECT", "WORKS_ON", "", "N"),
            Edge("EMPLOYEE", "__supervises__", "supervises", "1"),
            Edge("__supervises__", "EMPLOYEE", "", "N"),
        ],
        tables=[
            Table("EMPLOYEE", [("SSN", "PK"), ("Name", ""), ("Address", ""), ("Sex", ""), ("Salary", ""), ("SuperSSN", "FK"), ("DNo", "FK")], 0.5, 4.5),
            Table("DEPARTMENT", [("DNo", "PK"), ("DName", ""), ("MgrSSN", "FK"), ("MgrStartDate", "")], 5.0, 5.5),
            Table("PROJECT", [("PNo", "PK"), ("PName", ""), ("PLocation", ""), ("Domain", ""), ("DNo", "FK")], 9.5, 4.5),
            Table("WORKS_ON", [("SSN", "PK"), ("PNo", "PK"), ("Hours", "")], 5.0, 1.5),
        ],
        schema_edges=[
            SchemaEdge("EMPLOYEE", "DEPARTMENT", "DNo", "DNo"),
            SchemaEdge("DEPARTMENT", "EMPLOYEE", "MgrSSN", "SSN"),
            SchemaEdge("PROJECT", "DEPARTMENT", "DNo", "DNo"),
            SchemaEdge("WORKS_ON", "EMPLOYEE", "SSN", "SSN"),
            SchemaEdge("WORKS_ON", "PROJECT", "PNo", "PNo"),
        ],
    )

    d[2] = DiagramSet(
        "Exp 2: Part – Supplier – Shipment",
        entities=[
            Entity("SUPPLIER", ["SID (PK)", "SName", "SAddr"], 1.5, 5),
            Entity("PART", ["PID (PK)", "PName", "PColor"], 9, 5),
            Entity("SHIPMENT", ["SID (PK,FK)", "PID (PK,FK)", "Qty"], 5, 2.5),
        ],
        rels=[Rel("supplies", 3.2, 4.2), Rel("includes", 7.5, 4.2)],
        edges=[
            Edge("SUPPLIER", "__supplies__", "", "1"),
            Edge("__supplies__", "SHIPMENT", "", "N"),
            Edge("PART", "__includes__", "", "1"),
            Edge("__includes__", "SHIPMENT", "", "N"),
        ],
        tables=[
            Table("SUPPLIER", [("SID", "PK"), ("SName", ""), ("SAddr", "")], 1, 5),
            Table("PART", [("PID", "PK"), ("PName", ""), ("PColor", "")], 9.5, 5),
            Table("SHIPMENT", [("SID", "PK"), ("PID", "PK"), ("Qty", "")], 5, 1.5),
        ],
        schema_edges=[
            SchemaEdge("SHIPMENT", "SUPPLIER", "SID", "SID"),
            SchemaEdge("SHIPMENT", "PART", "PID", "PID"),
        ],
    )

    d[3] = DiagramSet(
        "Exp 3: Boat – Sailor – Reserves",
        entities=[
            Entity("SAILOR", ["SID (PK)", "SName", "Rating", "Age"], 1.5, 5),
            Entity("BOAT", ["BID (PK)", "BName", "Color"], 9, 5),
            Entity("RESERVES", ["SID (PK,FK)", "BID (PK,FK)", "Day"], 5, 2.5),
        ],
        rels=[Rel("reserves", 3.5, 4.2)],
        edges=[
            Edge("SAILOR", "__reserves__", "", "M"),
            Edge("__reserves__", "RESERVES"),
            Edge("BOAT", "RESERVES", "", "M"),
        ],
        tables=[
            Table("SAILOR", [("SID", "PK"), ("SName", ""), ("Rating", ""), ("Age", "")], 1, 5),
            Table("BOAT", [("BID", "PK"), ("BName", ""), ("Color", "")], 9.5, 5),
            Table("RESERVES", [("SID", "PK"), ("BID", "PK"), ("Day", "")], 5, 1.5),
        ],
        schema_edges=[
            SchemaEdge("RESERVES", "SAILOR", "SID", "SID"),
            SchemaEdge("RESERVES", "BOAT", "BID", "BID"),
        ],
    )

    d[4] = DiagramSet(
        "Exp 4: Customer – Branch – Account – Transaction",
        entities=[
            Entity("CUSTOMER", ["CustID (PK)", "CustName", "CustCity"], 0.8, 6),
            Entity("BRANCH", ["BranchName (PK)", "BranchCity", "Assets"], 5.5, 6.5),
            Entity("ACCOUNT", ["AccNo (PK)", "BranchName (FK)", "Balance", "AccType"], 9.5, 6),
            Entity("DEPOSITOR", ["CustID (PK,FK)", "AccNo (PK,FK)"], 2.5, 3),
            Entity("TRANSACTION", ["TxnID (PK)", "AccNo (FK)", "TxnType", "Amount", "TxnDate"], 8, 2.5),
        ],
        rels=[
            Rel("deposits", 3.5, 4.8),
            Rel("hosts", 7.2, 5.5),
            Rel("logs", 9.8, 4.5),
        ],
        edges=[
            Edge("CUSTOMER", "__deposits__"),
            Edge("__deposits__", "DEPOSITOR"),
            Edge("DEPOSITOR", "ACCOUNT"),
            Edge("BRANCH", "__hosts__"),
            Edge("__hosts__", "ACCOUNT"),
            Edge("ACCOUNT", "__logs__"),
            Edge("__logs__", "TRANSACTION"),
        ],
        tables=[
            Table("CUSTOMER", [("CustID", "PK"), ("CustName", ""), ("CustCity", "")], 0.3, 5.5),
            Table("BRANCH", [("BranchName", "PK"), ("BranchCity", ""), ("Assets", "")], 4.8, 6),
            Table("ACCOUNT", [("AccNo", "PK"), ("BranchName", "FK"), ("Balance", ""), ("AccType", "")], 9.2, 5.5),
            Table("DEPOSITOR", [("CustID", "PK"), ("AccNo", "PK")], 2, 2.5),
            Table("TRANSACTION", [("TxnID", "PK"), ("AccNo", "FK"), ("TxnType", ""), ("Amount", "")], 8.5, 2),
        ],
        schema_edges=[
            SchemaEdge("ACCOUNT", "BRANCH", "BranchName", "BranchName"),
            SchemaEdge("DEPOSITOR", "CUSTOMER", "CustID", "CustID"),
            SchemaEdge("DEPOSITOR", "ACCOUNT", "AccNo", "AccNo"),
            SchemaEdge("TRANSACTION", "ACCOUNT", "AccNo", "AccNo"),
        ],
    )

    d[5] = DiagramSet(
        "Exp 5: Books – Student – Borrows",
        entities=[
            Entity("STUDENT", ["SID (PK)", "SName", "Gender", "Course"], 1.5, 5.5),
            Entity("BOOKS", ["ISBN (PK)", "Title", "Author", "Publisher"], 9, 5.5),
            Entity("BORROWS", ["SID (PK,FK)", "ISBN (PK,FK)", "BorrowDate"], 5, 2.5),
        ],
        rels=[Rel("borrows", 3.8, 4.5)],
        edges=[
            Edge("STUDENT", "__borrows__", "", "M"),
            Edge("__borrows__", "BORROWS"),
            Edge("BOOKS", "BORROWS", "", "M"),
        ],
        tables=[
            Table("STUDENT", [("SID", "PK"), ("SName", ""), ("Gender", ""), ("Course", "")], 1, 5),
            Table("BOOKS", [("ISBN", "PK"), ("Title", ""), ("Author", ""), ("Publisher", "")], 9.5, 5),
            Table("BORROWS", [("SID", "PK"), ("ISBN", "PK"), ("BorrowDate", "")], 5, 1.5),
        ],
        schema_edges=[
            SchemaEdge("BORROWS", "STUDENT", "SID", "SID"),
            SchemaEdge("BORROWS", "BOOKS", "ISBN", "ISBN"),
        ],
    )

    d[6] = DiagramSet(
        "Exp 6: Patient – Doctor – Appointment",
        entities=[
            Entity("PATIENT", ["PID (PK)", "PName", "Age", "Gender"], 1.5, 5.5),
            Entity("DOCTOR", ["DID (PK)", "DName", "Specialization", "Experience"], 9, 5.5),
            Entity("APPOINTMENT", ["PID (PK,FK)", "DID (PK,FK)", "AppDate", "AppTime"], 5, 2.5),
        ],
        rels=[Rel("appoints", 3.8, 4.5)],
        edges=[
            Edge("PATIENT", "__appoints__", "", "M"),
            Edge("__appoints__", "APPOINTMENT"),
            Edge("DOCTOR", "APPOINTMENT", "", "M"),
        ],
        tables=[
            Table("PATIENT", [("PID", "PK"), ("PName", ""), ("Age", ""), ("Gender", "")], 1, 5),
            Table("DOCTOR", [("DID", "PK"), ("DName", ""), ("Specialization", ""), ("Experience", "")], 9.5, 5),
            Table("APPOINTMENT", [("PID", "PK"), ("DID", "PK"), ("AppDate", ""), ("AppTime", "")], 5, 1.5),
        ],
        schema_edges=[
            SchemaEdge("APPOINTMENT", "PATIENT", "PID", "PID"),
            SchemaEdge("APPOINTMENT", "DOCTOR", "DID", "DID"),
        ],
    )

    def _clone(ds: DiagramSet, title: str) -> DiagramSet:
        c = copy.deepcopy(ds)
        c.title = title
        return c

    # MongoDB experiments – same logical schemas
    d[7] = DiagramSet(
        "Exp 7: MongoDB Employee – Department",
        entities=[
            Entity("DEPARTMENT", ["dno (PK)", "dname", "location"], 2, 6),
            Entity("EMPLOYEE", ["ssn (PK)", "name, salary", "dno (FK)", "projects[]"], 7.5, 5.5),
        ],
        rels=[Rel("employs", 5.5, 5.8)],
        edges=[Edge("DEPARTMENT", "__employs__", "", "1"), Edge("__employs__", "EMPLOYEE", "", "N")],
        tables=[
            Table("departments", [("dno", "PK"), ("dname", ""), ("location", "")], 2, 5.5),
            Table("employees", [("ssn", "PK"), ("name", ""), ("salary", ""), ("dno", "FK"), ("projects", "")], 8, 4.5),
        ],
        schema_edges=[SchemaEdge("employees", "departments", "dno", "dno")],
    )

    d[8] = DiagramSet(
        "Exp 8: MongoDB Patient – Doctor",
        entities=[
            Entity("PATIENT", ["pid (PK)", "pname, age", "appointments[]"], 1.5, 5.5),
            Entity("DOCTOR", ["did (PK)", "dname", "specialization", "consult_fee"], 9, 5.5),
        ],
        rels=[Rel("treats", 5.2, 5.5)],
        edges=[Edge("PATIENT", "__treats__"), Edge("__treats__", "DOCTOR")],
        tables=[
            Table("patients", [("pid", "PK"), ("pname", ""), ("appointments", "")], 1, 5),
            Table("doctors", [("did", "PK"), ("dname", ""), ("specialization", ""), ("consult_fee", "")], 9, 5),
        ],
        schema_edges=[],
    )

    d[9] = _clone(d[2], "Exp 9: MongoDB Part – Supplier – Shipment")
    d[10] = _clone(d[3], "Exp 10: MongoDB Boat – Sailor")
    d[11] = DiagramSet(
        "Exp 11: MongoDB Customer – Branch",
        entities=[
            Entity("BRANCH", ["branch_id (PK)", "branch_name", "city"], 2, 6),
            Entity("CUSTOMER", ["cust_id (PK)", "cust_name", "accounts[]"], 8, 5.5),
        ],
        rels=[Rel("holds", 5.5, 5.5)],
        edges=[Edge("BRANCH", "__holds__"), Edge("__holds__", "CUSTOMER")],
        tables=[
            Table("branches", [("branch_id", "PK"), ("branch_name", ""), ("city", "")], 2, 5.5),
            Table("customers", [("cust_id", "PK"), ("cust_name", ""), ("accounts", "")], 8.5, 4.5),
        ],
        schema_edges=[],
    )
    d[12] = _clone(d[5], "Exp 12: MongoDB Books – Student")

    return d


FOLDER_MAP = {
    1: "Experiment_1_Employee_Department_Project",
    2: "Experiment_2_Part_Supplier_Supply",
    3: "Experiment_3_Boat_Sailor_Reserves",
    4: "Experiment_4_Customer_Branch_Account",
    5: "Experiment_5_Book_Lending_System",
    6: "Experiment_6_Hospital_Management_System",
    7: "Experiment_7_MongoDB_Employee_Department",
    8: "Experiment_8_MongoDB_Patient_Doctor",
    9: "Experiment_9_MongoDB_Part_Supplier_PLSQL_Backup",
    10: "Experiment_10_MongoDB_Boat_Sailor_Weekend_Trigger",
    11: "Experiment_11_MongoDB_Customer_Branch_Cursor",
    12: "Experiment_12_MongoDB_Books_Student_Exception",
}


def embed_images_in_md(md_path: str, er_file: str, schema_file: str) -> None:
    with open(md_path, "r", encoding="utf-8") as f:
        text = f.read()

  # Remove old embeds if re-running
    text = re.sub(r"\n### ER Diagram \(Figure\)\n!\[.*?\]\(.*?\)\n?", "\n", text)
    text = re.sub(r"\n### Schema Diagram \(Figure\)\n!\[.*?\]\(.*?\)\n?", "\n", text)

    er_img = f"![ER Diagram]({er_file})"
    schema_img = f"![Schema Diagram]({schema_file})"

    er_block = f"\n### ER Diagram (Figure)\n{er_img}\n\n*Figure: Entity–Relationship diagram (Chen notation). PK = Primary Key, FK = Foreign Key.*\n"
    schema_block = f"\n### Schema Diagram (Figure)\n{schema_img}\n\n*Figure: Relational schema with referential links. Orange = PK, Blue = FK.*\n"

    if "### ER Diagram (Figure)" not in text:
        if re.search(r"## ER DIAGRAM\s*\n", text):
            text = re.sub(r"(## ER DIAGRAM\s*\n)", r"\1" + er_block, text, count=1)
        elif "## ER DIAGRAM (Mermaid)" in text:
            text = re.sub(r"(## ER DIAGRAM \(Mermaid\)\s*\n)", r"\1" + er_block, text, count=1)

    if "### Schema Diagram (Figure)" not in text and re.search(r"## SCHEMA DIAGRAM\s*\n", text):
        text = re.sub(r"(## SCHEMA DIAGRAM\s*\n)", r"\1" + schema_block, text, count=1)

    # Experiments without SCHEMA section – add before RELATIONAL or MONGODB
    if "## SCHEMA DIAGRAM" not in text and schema_block.strip() not in text:
        for anchor in ("## RELATIONAL MODEL", "## MONGODB IMPLEMENTATION", "## SQL IMPLEMENTATION", "## PL/SQL"):
            if anchor in text:
                text = text.replace(anchor, f"## SCHEMA DIAGRAM\n{schema_block}\n---\n\n{anchor}", 1)
                break

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    specs = all_diagrams()
    for num, folder in FOLDER_MAP.items():
        ds = specs[num]
        exp_dir = os.path.join(LAB, folder)
        os.makedirs(exp_dir, exist_ok=True)
        er_path = os.path.join(exp_dir, "er_diagram.png")
        schema_path = os.path.join(exp_dir, "schema_diagram.png")

        draw_er(ds, er_path)
        draw_schema(ds, schema_path)
        print(f"Exp {num}: {er_path}, {schema_path}")

        md_files = [f for f in os.listdir(exp_dir) if f.endswith(".md")]
        if md_files:
            embed_images_in_md(os.path.join(exp_dir, md_files[0]), "er_diagram.png", "schema_diagram.png")

    print("All diagrams generated and embedded.")


if __name__ == "__main__":
    main()
