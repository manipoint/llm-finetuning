import json
from pathlib import Path

path = Path("/Users/imranlatif/Downloads/homebudget_domain_fine_tuning.ipynb")
backup = path.with_suffix(".backup.ipynb")

# Backup first
backup.write_bytes(path.read_bytes())

# Load notebook JSON
nb = json.loads(path.read_text(encoding="utf-8"))

# Remove problematic widget metadata
nb.get("metadata", {}).pop("widgets", None)

# Save repaired notebook
path.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding="utf-8")

print(f"Fixed: {path}")
print(f"Backup saved as: {backup}")
