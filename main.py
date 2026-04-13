import pathlib

agents_dir = pathlib.Path(".github/agents")
names = sorted(
    p.name.removesuffix(".agent.md")
    for p in agents_dir.glob("*.agent.md")
) if agents_dir.is_dir() else []

col_width = max(len("Agent"), max((len(n) for n in names), default=0))
border = "+" + "-" * (col_width + 2) + "+"
print(border)
print(f"| {'Agent':<{col_width}} |")
print(border)
for name in names:
    print(f"| {name:<{col_width}} |")
print(border)
