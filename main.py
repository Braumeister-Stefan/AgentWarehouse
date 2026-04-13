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
    """Save a polished PNG table of agent names and definitions."""
    from matplotlib.patches import Rectangle

    output.parent.mkdir(parents=True, exist_ok=True)

    # ── Palette ───────────────────────────────────────────────────────────
    HDR_BG   = "#1e2d3d"   # header background (dark navy)
    HDR_FG   = "#ffffff"   # header text
    ODD_BG   = "#ffffff"   # odd data rows
    EVN_BG   = "#f2f6fb"   # even data rows
    NAME_FG  = "#1e2d3d"   # agent name text
    DEF_FG   = "#374151"   # definition text
    ACCENT   = "#4a90d9"   # left accent bar
    GRID     = "#cdd5e0"   # row separator lines
    BORDER   = "#7a8fa6"   # outer frame

    # ── Dimensions (inches) ───────────────────────────────────────────────
    FIG_W    = 13.0
    M_L      = 0.50        # left/right page margin
    M_R      = 0.50
    TABLE_W  = FIG_W - M_L - M_R      # 12.0
    NAME_FRAC = 0.22
    NAME_W   = TABLE_W * NAME_FRAC    # agent name column
    DEF_W    = TABLE_W * (1 - NAME_FRAC)
    HDR_H    = 0.52        # header row height
    TITLE_H  = 0.70        # space for title above table
    FOOT_H   = 0.30        # bottom breathing room
    LINE_H   = 0.205       # height per wrapped text line
    MIN_RH   = 0.52        # minimum data row height
    PAD_X    = 0.20        # horizontal text padding inside cell
    ACCENT_W = 0.055       # width of left accent bar
    BASE_ROW_PADDING = 0.16   # base vertical padding (inches) added to each row
    NAME_TEXT_NUDGE  = 0.65   # fraction of PAD_X used to push name text right of accent bar

    FS_TITLE = 16
    FS_HDR   = 11
    FS_NAME  = 9.5
    FS_DEF   = 9.5
    WRAP_W   = 90          # chars before wrapping definition

    # ── Pre-compute row heights ───────────────────────────────────────────
    cells = [(name, textwrap.fill(defn, WRAP_W)) for name, defn in rows]
    row_heights = [
        max(MIN_RH, BASE_ROW_PADDING + len(defn.splitlines()) * LINE_H)
        for _, defn in cells
    ]

    total_h = TITLE_H + HDR_H + sum(row_heights) + FOOT_H

    fig, ax = plt.subplots(figsize=(FIG_W, total_h))
    ax.set_xlim(0, FIG_W)
    ax.set_ylim(0, total_h)
    ax.axis("off")
    fig.patch.set_facecolor("white")

    # ── Helpers ───────────────────────────────────────────────────────────
    def add_rect(x, y, w, h, fc, ec="none", lw=0, zorder=1):
        ax.add_patch(
            Rectangle((x, y), w, h, facecolor=fc, edgecolor=ec,
                      linewidth=lw, zorder=zorder)
        )

    def hline(x0, x1, y, color=GRID, lw=0.7, zorder=3):
        ax.plot([x0, x1], [y, y], color=color, linewidth=lw,
                solid_capstyle="butt", zorder=zorder)

    def vline(x, y0, y1, color=GRID, lw=0.7, zorder=3):
        ax.plot([x, x], [y0, y1], color=color, linewidth=lw,
                solid_capstyle="butt", zorder=zorder)

    tx = M_L   # table left edge x

    # ── Title ─────────────────────────────────────────────────────────────
    ax.text(
        FIG_W / 2, total_h - TITLE_H / 2,
        "Agent Warehouse",
        ha="center", va="center",
        fontsize=FS_TITLE, fontweight="bold", color=HDR_BG,
        fontstyle="normal",
    )

    # ── Header row ────────────────────────────────────────────────────────
    table_top = total_h - TITLE_H
    add_rect(tx, table_top - HDR_H, NAME_W, HDR_H, HDR_BG)
    add_rect(tx + NAME_W, table_top - HDR_H, DEF_W, HDR_H, HDR_BG)

    ax.text(
        tx + NAME_W / 2, table_top - HDR_H / 2, "Agent",
        ha="center", va="center",
        fontsize=FS_HDR, fontweight="bold", color=HDR_FG,
    )
    ax.text(
        tx + NAME_W + PAD_X, table_top - HDR_H / 2, "Definition",
        ha="left", va="center",
        fontsize=FS_HDR, fontweight="bold", color=HDR_FG,
    )

    # ── Data rows ─────────────────────────────────────────────────────────
    y = table_top - HDR_H
    for i, ((name, defn), rh) in enumerate(zip(cells, row_heights)):
        bg = ODD_BG if i % 2 == 0 else EVN_BG

        # Row backgrounds
        add_rect(tx,          y - rh, NAME_W, rh, bg)
        add_rect(tx + NAME_W, y - rh, DEF_W,  rh, bg)

        # Accent bar
        add_rect(tx, y - rh, ACCENT_W, rh, ACCENT, zorder=2)

        # Agent name – monospace bold, nudged right of accent bar
        ax.text(
            tx + ACCENT_W + PAD_X * NAME_TEXT_NUDGE, y - rh / 2, name,
            ha="left", va="center",
            fontsize=FS_NAME, fontweight="bold", color=NAME_FG,
            fontfamily="monospace", zorder=4,
        )

        # Definition text
        ax.text(
            tx + NAME_W + PAD_X, y - rh / 2, defn,
            ha="left", va="center",
            fontsize=FS_DEF, color=DEF_FG,
            linespacing=1.50, zorder=4,
        )

        # Row separator
        hline(tx, tx + NAME_W + DEF_W, y - rh)
        y -= rh

    # ── Outer frame ───────────────────────────────────────────────────────
    right = tx + NAME_W + DEF_W
    hline(tx, right, table_top, color=HDR_BG,  lw=2.0)   # top
    hline(tx, right, y,         color=BORDER,  lw=1.5)   # bottom
    vline(tx,    y, table_top,  color=BORDER,  lw=1.5)   # left
    vline(right, y, table_top,  color=BORDER,  lw=1.5)   # right
    # Column divider
    vline(tx + NAME_W, y, table_top, color=GRID, lw=0.9)

    plt.savefig(output, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Table saved to {output}")


if __name__ == "__main__":
    rows = load_agents(AGENTS_DIR) if AGENTS_DIR.is_dir() else []
    if not rows:
        print("No agent files found.")
    else:
        print_text_table(rows)
        save_png_table(rows, TABLE_IMG)
