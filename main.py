"""Reads agent definitions and produces a summary table as text and PNG."""

import pathlib
import re
import textwrap

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

AGENTS_DIR = pathlib.Path(".github/agents")
ASSETS_DIR = pathlib.Path("assets")
TABLE_IMG = ASSETS_DIR / "agent-table.png"

# --- Definition pattern: first line matching **Definition:** ... ---
_DEF_RE = re.compile(r"\*\*Definition:\*\*\s*(.+)")


def load_agents(agents_dir: pathlib.Path) -> list[tuple[str, str]]:
    """Return sorted list of (name, definition) tuples from agent files."""
    rows = []
    for path in sorted(agents_dir.glob("*.agent.md")):
        name = path.name.removesuffix(".agent.md")
        definition = ""
        for line in path.read_text(encoding="utf-8").splitlines():
            m = _DEF_RE.search(line)
            if m:
                definition = m.group(1).strip()
                break
        rows.append((name, definition))
    return rows


def print_text_table(rows: list[tuple[str, str]]) -> None:
    """Print a plain-text summary table to stdout."""
    name_w = max(len("Agent"), max((len(r[0]) for r in rows), default=0))
    def_w = max(len("Definition"), max((len(r[1]) for r in rows), default=0))
    border = f"+{'-' * (name_w + 2)}+{'-' * (def_w + 2)}+"
    print(border)
    print(f"| {'Agent':<{name_w}} | {'Definition':<{def_w}} |")
    print(border)
    for name, definition in rows:
        print(f"| {name:<{name_w}} | {definition:<{def_w}} |")
    print(border)


def save_png_table(rows: list[tuple[str, str]], output: pathlib.Path) -> None:
    """Save a formatted PNG table of agent names and definitions."""
    output.parent.mkdir(parents=True, exist_ok=True)

    col_labels = ["Agent", "Definition"]
    wrap_width = 72
    cell_data = [
        [name, "\n".join(textwrap.wrap(defn, wrap_width))]
        for name, defn in rows
    ]

    # Estimate row heights from wrapped text
    row_heights = [0.35] + [
        max(0.35, 0.18 * len(defn.splitlines()))
        for _, defn in cell_data
    ]
    fig_height = sum(row_heights) + 0.6
    fig, ax = plt.subplots(figsize=(14, fig_height))
    ax.axis("off")

    tbl = ax.table(
        cellText=cell_data,
        colLabels=col_labels,
        cellLoc="left",
        loc="center",
    )
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(9)
    tbl.auto_set_column_width([0, 1])

    # Style header
    for col in range(len(col_labels)):
        cell = tbl[0, col]
        cell.set_facecolor("#2c3e50")
        cell.set_text_props(color="white", fontweight="bold")

    # Alternate row shading
    for row_idx in range(1, len(rows) + 1):
        colour = "#f0f4f8" if row_idx % 2 == 0 else "white"
        for col in range(len(col_labels)):
            tbl[row_idx, col].set_facecolor(colour)

    # Apply row heights
    for row_idx, height in enumerate(row_heights):
        for col in range(len(col_labels)):
            tbl[row_idx, col].set_height(height / fig_height)

    plt.tight_layout(pad=0.4)
    plt.savefig(output, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Table saved to {output}")


if __name__ == "__main__":
    rows = load_agents(AGENTS_DIR) if AGENTS_DIR.is_dir() else []
    if not rows:
        print("No agent files found.")
    else:
        print_text_table(rows)
        save_png_table(rows, TABLE_IMG)
