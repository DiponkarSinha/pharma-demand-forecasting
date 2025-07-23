# requirements.py
from pkg_resources import working_set

with open("requirements.txt", "w") as f:
    for dist in sorted(working_set, key=lambda x: x.project_name.lower()):
        f.write(f"{dist.project_name}>={dist.version}\n")

print("✅ requirements.txt generated with >= versions.")
