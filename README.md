# wow-links

A compact, verified directory of addons, sites, calculators, guides, and voice-cue packs for World of Warcraft Midnight Season 2 (patch 12.1) Mythic+ and raid play. Static site, deployed via GitHub Actions to GitHub Pages: https://vosbek.github.io/wow-links/

Includes a personal "My Setup" section listing the addons currently installed on this account, kept separate from the shared directory.

## Structure

- `index.html` — page content
- `style.css` — light, neutral-plus-indigo design system (Archivo / Public Sans / IBM Plex Mono, via Google Fonts)
- `.github/workflows/pages.yml` — deploys `main` to GitHub Pages on push

## Updating

Edit `index.html` directly and push to `main` — the Pages workflow redeploys automatically. Links should be checked live before adding; season patches move fast and sites go stale.
