from pathlib import Path


autodocs = {}

loader_dirs = (
    "engines",
    "modules",
    "returners",
    "states",
)

for ldir in loader_dirs:
    autodocs[ldir] = []

docs_path = Path("docs")
ref_path = docs_path / "ref"

for path in Path("src").glob("**/*.py"):
    kind = path.parent.name
    if kind in loader_dirs:
        import_path = ".".join(path.with_suffix("").parts[1:])
        autodocs[kind].append(import_path)
        rst_path = ref_path / kind / (import_path + ".rst")
        rst_path.parent.mkdir(parents=True, exist_ok=True)
        rst_path.write_text(
            f"""
{import_path}
{'='*len(import_path)}

.. automodule:: {import_path}
    :members:
"""
        )

for ldir in autodocs:
    if not autodocs[ldir]:
        continue
    all_rst = ref_path / ldir / "all.rst"
    all_rst.parent.mkdir(parents=True, exist_ok=True)
    all_rst.write_text(
        f"""
.. all-saltext.prometheus.{ldir}:

{'-'*len(ldir)}--------
{ldir.title()} Modules
{'-'*len(ldir)}--------

.. autosummary::
    :toctree:

{chr(10).join(sorted('    '+mod for mod in autodocs[ldir]))}
"""
    )
