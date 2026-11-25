"""Copy the public website into the Cloudflare assets directory."""
from pathlib import Path
import shutil

root = Path(__file__).resolve().parents[1]
output = root / "dist"
output.mkdir(exist_ok=True)
folders = ['Html', 'Css', 'Images']
for folder in folders:
    shutil.copytree(root / folder, output / folder, dirs_exist_ok=True)
for page in (root / "Html").glob("*.html"):
    shutil.copy2(page, output / page.name)
