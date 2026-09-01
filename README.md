# Blender Themes Collection (Blender 5.2+ Extensions)

A curated collection of customized, high-contrast, and tuned themes for **Blender 5.2+**, packaged natively as Blender extensions.

![Blender 5.2+](https://img.shields.io/badge/Blender-5.2%2B-orange.svg)

---

## Available Themes

| Theme Name | Manifest ID | Target | Upstream Basis / Attribution |
| :--- | :--- | :--- | :--- |
| **DRCL (MD Mod)** | `drcl_md` | Blender 5.2+ | Customized from [DRCL](https://extensions.blender.org/themes/theme-drcl/) by Paul Kotelevets (1D_Inc) |
| **Midnight (MD Mod)** | `midnight_md` | Blender 5.2+ | Customized from [Midnight](https://github.com/kame404/Blender-Themes) by kame404 |

---

## Installation

### Method A: Via Personal Extension Repository (Recommended)
Add the central repository in Blender:
* **URL**: `https://m-dr.github.io/blender-extensions/index.json`  
Then search for any theme in **Preferences > Get Extensions** (filter by *Themes*) and click **Install**.

### Method B: Install from Disk (.zip)
1. Download any theme `.zip` (e.g. `drcl_md-1.0.0.zip` or `midnight_md-1.0.0.zip`) from the [Releases](https://github.com/m-dr/blender-themes/releases) page.
2. In Blender: **Preferences > Get Extensions > Install from Disk...**
3. Select the `.zip` file. The theme is automatically activated in **Preferences > Themes**.

---

## Building Packages

To build all theme extension `.zip` archives into `dist/`:
```bash
python scripts/build_themes.py
```

---

## License

Themes are distributed under the GNU General Public License v3.0 or later (GPL-3.0).
