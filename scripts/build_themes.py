#!/usr/bin/env python3
"""
Build all compliant Blender 5.2+ theme extension packages.
"""
import hashlib
import json
import os
import tomllib
import zipfile

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
THEMES_DIR = os.path.join(REPO_ROOT, "themes")
DIST_DIR = os.path.join(REPO_ROOT, "dist")


def sha256_file(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return "sha256:" + h.hexdigest()


def main():
    os.makedirs(DIST_DIR, exist_ok=True)
    theme_folders = [
        os.path.join(THEMES_DIR, d)
        for d in os.listdir(THEMES_DIR)
        if os.path.isdir(os.path.join(THEMES_DIR, d)) and not d.startswith(".")
    ]

    built_entries = []

    for theme_dir in sorted(theme_folders):
        manifest_path = os.path.join(theme_dir, "blender_manifest.toml")
        if not os.path.exists(manifest_path):
            print(f"Skipping {os.path.basename(theme_dir)}: No blender_manifest.toml found")
            continue

        with open(manifest_path, "rb") as f:
            manifest = tomllib.load(f)

        ext_id = manifest["id"]
        version = manifest["version"]
        zip_filename = f"{ext_id}-{version}.zip"
        zip_path = os.path.join(DIST_DIR, zip_filename)

        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
            for root, _, files in os.walk(theme_dir):
                for file in files:
                    if file.startswith("."):
                        continue
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, theme_dir)
                    z.write(full_path, arcname=rel_path)

        file_size = os.path.getsize(zip_path)
        file_hash = sha256_file(zip_path)

        print(f"Built theme package: {zip_filename} ({file_size} bytes, {file_hash})")

        entry = {
            "id": ext_id,
            "schema_version": manifest.get("schema_version", "1.0.0"),
            "name": manifest.get("name", ext_id),
            "tagline": manifest.get("tagline", ""),
            "version": version,
            "type": "theme",
            "blender_version_min": manifest.get("blender_version_min", "5.2.0"),
            "maintainer": manifest.get("maintainer", "MD"),
            "license": manifest.get("license", ["SPDX:GPL-3.0-or-later"]),
            "tags": ["Theme"],
            "archive_url": f"https://github.com/m-dr/blender-themes/releases/download/v{version}/{zip_filename}",
            "website": manifest.get("website", "https://github.com/m-dr/blender-themes"),
        }
        built_entries.append(entry)

    print("\n--- Registry Snippet for registry.json ---")
    print(json.dumps(built_entries, indent=2))


if __name__ == "__main__":
    main()
