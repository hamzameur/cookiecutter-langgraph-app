import shutil
from pathlib import Path

root_dir = Path("{{ cookiecutter.package_name }}")
shutil.copy(".example.env", ".env")
