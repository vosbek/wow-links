import html
import os

OUT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

PAGES = [
    ("index.html", "Overview"),
    ("sites.html", "Sites & Calculators"),
    ("guides.html", "Guides"),
    ("cheatsheets.html", "Cheat Sheets & Images"),
    ("videos.html", "Videos"),
    ("tools.html", "Desktop Tools"),
    ("voice.html", "Voice-Cue Packs"),
    ("my-setup.html", "My Setup"),
    ("addons.html", "Addons"),
]

def tag(role):
    cls = {"M+": "tag--mplus", "Raid": "tag--raid", "Both": "tag--both"}[role]
    return f'<span class="tag {cls}">{role}</span>'

def row3(name, url, desc, role):
    return f'''            <tr>
              <td class="col-name"><a href="{url}" target="_blank" rel="noopener noreferrer">{html.escape(name)}</a></td>
              <td class="col-desc">{desc}</td>
              <td class="col-tag">{tag(role)}</td>
            </tr>
'''

def row2(name, url, desc):
    return f'''            <tr><td class="col-name"><a href="{url}" target="_blank" rel="noopener noreferrer">{html.escape(name)}</a></td><td class="col-desc">{desc}</td></tr>
'''

def table3(caption, rows):
    body = "".join(row3(*r) for r in rows)
    return f'''      <div class="table-wrap">
        <table class="directory">
          <caption>{caption}</caption>
          <thead>
            <tr><th scope="col">Name</th><th scope="col">What it does</th><th scope="col">Role</th></tr>
          </thead>
          <tbody>
{body}          </tbody>
        </table>
      </div>
'''

def table2(caption, rows):
    body = "".join(row2(*r) for r in rows)
    return f'''      <div class="table-wrap">
        <table class="directory">
          <caption>{caption}</caption>
          <thead>
            <tr><th scope="col">Name</th><th scope="col">What it does</th></tr>
          </thead>
          <tbody>
{body}          </tbody>
        </table>
      </div>
'''

def subsection(code, title, note, table_html):
    return f'''    <section>
      <div class="section-heading">
        <div>
          <p class="section-code">{code}</p>
          <h2>{title}</h2>
        </div>
        <p class="section-note">{note}</p>
      </div>
{table_html}
    </section>
'''

def single(table_html, extra=""):
    return f'''    <section>
{extra}{table_html}
    </section>
'''

# ---------------- Sidebar / nav ----------------

NAV_ITEMS = [
    ("index.html", "Overview", None),
    ("sites.html", "Sites &amp; Calculators", "SITES_COUNT"),
    ("guides.html", "Guides", "GUIDES_COUNT"),
    ("cheatsheets.html", "Cheat Sheets &amp; Images", "CHEATS_COUNT"),
    ("videos.html", "Videos", "VIDEOS_COUNT"),
    ("tools.html", "Desktop Tools", "TOOLS_COUNT"),
    ("voice.html", "Voice-Cue Packs", "VOICE_COUNT"),
    ("my-setup.html", "My Setup", "SETUP_COUNT"),
    ("addons.html", "Addons", "ADDONS_COUNT"),
]

def render_chrome(active_file, title, page_meta, body_html, counts):
    side_links = []
    mobile_links = []
    for href, label, count_key in NAV_ITEMS:
        cur = ' aria-current="page"' if href == active_file else ''
        count_html = f' <span>{counts[count_key]}</span>' if count_key else ''
        side_links.append(f'      <a href="{href}"{cur}>{label}{count_html}</a>')
        mobile_links.append(f'    <a href="{href}"{cur}>{label.replace("&amp;", "&")}</a>')

    side_nav = "\n".join(side_links)
    mobile_nav = "\n".join(mobile_links)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="A compact, verified directory of addons, sites, calculators, guides, cheat sheets, videos, and tools for World of Warcraft Midnight Season 2 Mythic+ and raid play.">
  <meta name="theme-color" content="#f7f7f4">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title} — Midnight Season 2 Ops Workbook">
  <meta property="og:description" content="Verified tools, sites, guides, and references for M+ and raid, organized by category.">
  <meta property="og:url" content="https://vosbek.github.io/wow-links/{active_file}">
  <meta name="twitter:card" content="summary">
  <title>{title} — Midnight S2 Ops Workbook</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700&family=Public+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@500;600&display=swap">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <a class="skip-link" href="#directory">Skip to content</a>

  <header class="topbar" id="top">
    <div class="masthead">
      <a class="wordmark" href="index.html" aria-label="Midnight Season 2 Ops Workbook, back to overview">
        <span aria-hidden="true" class="wordmark-mark"><i></i><i></i><i></i></span>
        <span>Ops Workbook</span>
      </a>
      <p class="masthead-meta">Midnight Season 2 &middot; Patch 12.1 <span class="meta-sep">/</span> <span class="live-dot" aria-hidden="true"></span> Verified Aug 18, 2026</p>
    </div>
  </header>

  <nav class="section-nav" aria-label="Page sections">
{mobile_nav}
  </nav>

  <div class="layout">
    <aside class="side-nav" aria-label="Page sections">
      <p class="side-nav-title">Contents</p>
{side_nav}
    </aside>

    <div class="content-col">
      <div class="page-heading-row">
        <h1>{title}</h1>
        <p class="page-meta">{page_meta}</p>
      </div>

      <main id="directory">
{body_html}
      </main>
    </div>
  </div>

  <footer class="site-footer">
    <p>Every link was checked live on August 18, 2026. Sites change fast during a new season — if something's dead or a better replacement exists, open an issue or a PR on the repo.</p>
    <p>Fonts: Archivo, Public Sans, and IBM Plex Mono, served via Google Fonts.</p>
  </footer>
</body>
</html>
'''

# ---------------- Content ----------------

# ===== SITES & CALCULATORS =====
sites_logs = [
    ("Warcraft Logs", "https://www.warcraftlogs.com", "The base combat-log parser everything else in this section builds on.", "Both"),
    ("Wipefest", "https://www.wipefest.gg", "Boss-fight-specific log analysis: mechanic misses, deaths, and interrupt coverage.", "Raid"),
    ("WoWAnalyzer", "https://wowanalyzer.com", "Automated per-spec log analysis with a rotation and talent-usage checklist.", "Both"),
    ("WowCoach.gg", "https://wowcoach.gg", "AI-assisted log coach that answers plain-language questions about what caused a wipe or death.", "Both"),
    ("Warcraft Learner", "https://warcraft-learner.com", "Analyzes Mythic raid logs to surface specific improvement points.", "Raid"),
    ("WoW Codex — DPS Rankings", "https://www.wow-codex.de/gadgets/dps-tierlist?lang=en", "Warcraft Logs-driven spec comparison across M+ dungeons, live and PTR views.", "M+"),
]
sites_gearing = [
    ("Raidbots", "https://www.raidbots.com", "Droptimizer gear sims, consumable planning, and raid/M+ SimulationCraft reports.", "Both"),
    ("WoWBiS.gg", "https://wowbis.gg", "Best-in-slot gear planner and loot-priority reference by spec.", "Both"),
    ("MythicSim", "https://mythicsim.com", "Paste your character and get a DPS number plus a ranked list of gear upgrades for M+.", "M+"),
    ("LootPilot", "https://lootpilot.app", "Ranks bonus-roll and loot spending by value per token to maximize upgrades.", "Both"),
    ("wowaudit", "https://wowaudit.com", "Shared roster view built from uploaded Raidbots reports, showing exact upgrade levels per player.", "Raid"),
    ("Bloodmallet", "https://bloodmallet.com", "Pre-computed SimC charts ranking trinkets, talents, and tier combos per spec with zero setup.", "Both"),
    ("WoW Codex — Crest Calculator", "https://www.wow-codex.de/gadgets/crestcalculator?lang=en", "Plans crest costs and upgrade steps, and converts them into how many M+ or delves you need to run.", "Both"),
    ("For The Ilvl", "https://for-the-ilvl.com", "Ranks Mythic+ dungeons by item-level upgrade chance to prioritize which keys to run.", "M+"),
    ("Reset Ready", "https://reset-ready.com", "Plans which content to run to gear up fastest based on how much time you have each week.", "Both"),
]
sites_planning = [
    ("Raider.IO", "https://raider.io", "The standard site for M+ score, raid progress, and recruitment lookups before inviting someone.", "Both"),
    ("Mythic Planner", "https://mythicplanner.com", "Calculates which key levels you need to run to hit a target Mythic+ rating.", "M+"),
    ("CadenceMDR", "https://cadencemdr.com/", "Shows top-parse cooldown timelines per boss and spec in M+; export your own plan to the companion addon.", "M+"),
    ("RaidPlan.io", "https://raidplan.io", "Visual boss-arena positioning and strategy planner you can share as a link.", "Raid"),
    ("WoW Raid Planner", "https://wowraidplanner.com", "Free roster, signup, and attendance tracker for guild raid teams.", "Raid"),
    ("Wago.io", "https://wago.io", "Import/hosting hub for addon strings and UI packs.", "Both"),
    ("wow-achievement-plan.com", "https://wow-achievement-plan.com", "Ranks every uncompleted achievement by time-to-done, with season deadlines flagged.", "Both"),
    ("Wowhead Talent Calculator", "https://www.wowhead.com/talent-calc", "Build, save, and share full Midnight talent loadouts including hero talents.", "Both"),
    ("Wowhead Profession Tree Calculator", "https://www.wowhead.com/profession-tree-calc", "Plans profession specialization trees for crafting and gearing.", "Both"),
    ("Raidfather Item Level Tracks", "https://raidfather.com/12_1.html", "Season 2 item-level tracks and gear-source reference, resizable and printable.", "Both"),
    ("DanderBot WoW API Changes", "https://danderbot.github.io/wow-api-changes/patches/12.1.0/", "Build-by-build diff of Blizzard's Lua API, including secret-value flags — the source behind \"why did my addon break.\"", "Both"),
]

sites_body = (
    subsection("GROUP 01", "Logs &amp; performance analysis", "Where a pull actually went wrong.", table3("6 sites", sites_logs))
    + subsection("GROUP 02", "Gearing &amp; simulation", "What to equip and where to farm it.", table3("9 sites", sites_gearing))
    + subsection("GROUP 03", "Planning &amp; reference", "Routes, rosters, talents, and API tracking.", table3("11 sites", sites_planning))
)
sites_total = len(sites_logs) + len(sites_gearing) + len(sites_planning)

# ===== GUIDES =====
guides_class = [
    ("Wowhead S2 Guide Compendium", "https://www.wowhead.com/news/patch-12-1-guide-compendium-every-guide-you-ll-need-for-season-2-382408", "Index of every major Season 2 guide across dungeons, raid, gearing, and classes.", "Both"),
    ("Icy Veins — Restoration Shaman", "https://www.icy-veins.com/wow/restoration-shaman-pve-healing-guide", "Talents, rotation, and stat priority for Restoration Shaman healing.", "Both"),
    ("Method — Restoration Shaman", "https://www.method.gg/guides/restoration-shaman", "Mythic-team-authored Restoration Shaman guide covering builds and cooldown usage.", "Both"),
    ("Maxroll — Restoration Shaman M+", "https://maxroll.gg/wow/class-guides/restoration-shaman-mythic-plus-guide", "Mythic+-specific Restoration Shaman build and playstyle guide.", "M+"),
    ("wow.gg — Restoration Shaman", "https://wow.gg/guides/shaman-restoration", "Talents, rotation, stat priority, BiS gear, and M+ tips for Restoration Shaman.", "Both"),
    ("Icy Veins — Preservation Evoker", "https://www.icy-veins.com/wow/preservation-evoker-pve-healing-guide", "Talents, rotation, and stat priority for Preservation Evoker healing.", "Both"),
    ("Wowhead — Preservation Evoker", "https://www.wowhead.com/guide/classes/evoker/preservation/overview-pve-healer", "Wowhead's Preservation Evoker healer overview, updated per patch.", "Both"),
]
guides_raid = [
    ("Icy Veins — Venomous Abyss Raid", "https://www.icy-veins.com/wow/venomous-abyss-raid-guide", "Overview and strategy for all eight bosses in the current raid tier.", "Raid"),
    ("Icy Veins — Ula'tek Boss Guide", "https://www.icy-veins.com/wow/ulatek-raid-guide", "Boss-specific tactics for the raid's final encounter.", "Raid"),
    ("Icy Veins — Healer Tier List", "https://www.icy-veins.com/wow/healer-rankings-tier-list", "Comparative ranking of all seven healer specs for the current season.", "Both"),
    ("Larias' Raiders Guide", "https://lariasguide.com", "Weekly raid checklist addon, loot-tracking spreadsheet, and community Discord for progression teams.", "Raid"),
    ("Raid Boss Quiz", "https://kc.wow-achievement-plan.com", "Drop one link in raid chat and quiz your team on fight knowledge, role by role, before the pull.", "Raid"),
    ("r/CompetitiveWoW", "https://www.reddit.com/r/CompetitiveWoW/", "The main community hub for competitive raid and Mythic+ theorycrafting discussion.", "Both"),
]
guides_body = (
    subsection("GROUP 01", "Class &amp; spec guides", "Talents, rotation, stat priority.", table3("7 guides", guides_class))
    + subsection("GROUP 02", "Raid &amp; season reference", "Boss tactics, tier context, community.", table3("6 guides", guides_raid))
)
guides_total = len(guides_class) + len(guides_raid)

# ===== CHEAT SHEETS & IMAGES =====
cheats = [
    ("Season 2 reference album", "https://imgur.com/a/2xAMQyo", "A saved Imgur album of Season 2 reference images — contents as originally bookmarked, not re-verified by this site."),
    ("In-Game Raid TL;DR Guide (Wago import)", "https://wago.io/Bkl4oqk-S", "An importable in-game TL;DR guide for the current raid. Requires ThisWeeksAuras or M33kAuras (see Addons)."),
    ("Raid Assist — Visual + Audio (Wago import)", "https://wago.io/8-rukvKfa", "Visual and audio raid-mechanic call-outs, supports BigWigs and DBM. Requires ThisWeeksAuras or M33kAuras and the Fox Lab Studio sound pack (see Voice-Cue Packs)."),
    ("Tactyks' Midnight S2 M+ Ability Tracking Sheet", "https://docs.google.com/spreadsheets/d/1gI8-pZVc5LluzupXtsuNOT6Q7LMTu-rD3v2IJhewakY/edit?gid=1683936736", "A community-maintained spreadsheet documenting trash and boss abilities across the Season 2 M+ dungeon pool."),
    ("Amazing Jamo's Healing Assignments (Midnight Dungeons S2)", "https://docs.google.com/spreadsheets/d/1JcKLM5pt2o4xjr_hIBfrizeAcytfPPhE0wxrHvU-oKA/edit", "Public spreadsheet of healing cooldown assignments and strategies for Season 2 Mythic dungeons and raid."),
    ("Midnight Cheat Sheet (addon)", "https://www.curseforge.com/wow/addons/midnight-cheat-sheet", "In-game gearing reference — upgrade tracks, crest costs, consumables, and BiS wishlist notes. Listed as an addon; see Addons."),
]
cheats_body = single(table2(f"{len(cheats)} references", cheats))
cheats_total = len(cheats)

# ===== VIDEOS =====
videos = [
    ("Midnight S2 M+ Healer Survival Guide", "https://youtu.be/HP20FYYNn88", "Healer-focused strategy for Season 2 Mythic+.", "Both"),
    ("AWOWLab Overview", "https://youtu.be/EQqjasuxq1g", "Walkthrough of what AwowLab does and how to use it — see Desktop Tools.", "Both"),
]
videos_body = single(table3(f"{len(videos)} videos", videos))
videos_total = len(videos)

# ===== DESKTOP TOOLS =====
tools = [
    ("AwowLab", "https://www.awowlab.com/", "Local Windows log-review tool: builds a 3D replay from log data, an overlay damage meter reading your combat log live, and a pull-comparison view against a Warcraft Logs report. Only touches the network for updates, WCL pulls, or Wowhead lookups.", "Both"),
    ("AwowlabOverlay (source)", "https://github.com/Wobblucy/AwowlabOverlay", "Open-source parser/overlay component behind AwowLab's standalone overlay.", "Both"),
    ("WowUp", "https://wowup.io", "Free, open-source addon manager — installs and updates addons from CurseForge, Wago, GitHub, and Tukui in one place.", "Both"),
]
tools_body = single(table3(f"{len(tools)} tools", tools))
tools_total = len(tools)

# ===== VOICE-CUE PACKS =====
voice = [
    ("BigWigs Voice", "https://github.com/BigWigsMods/BigWigs_Voice", "Official BigWigs plugin adding text-to-speech call-outs for boss abilities.", "Both"),
    ("Boss Ability Announcement", "https://www.curseforge.com/wow/addons/dbm-event-announcement", "Voice and text announcer plugin that works with either DBM or BigWigs.", "Both"),
    ("BigWigs Midnight Raid Voice Assist", "https://www.curseforge.com/wow/addons/bigwigs-midnight-raid-voice-assist", "Plug-and-play spoken call-outs for current-tier raid mechanics, no manual mapping needed for standard alerts.", "Raid"),
    ("Midnight Season 2 Raid Voice Assist", "https://www.curseforge.com/wow/addons/midnight-season-2-raid-voice-assist", "Sound-media pack required by the Raid Assist Wago import (see Cheat Sheets &amp; Images) for its fine-tuned audio call-outs.", "Raid"),
    ("Fox Lab Studio", "https://www.curseforge.com/wow/addons/fox-lab-studio", "Sound-media addon for the audio-only Raid Assist setup — simpler install, less fine-tuned than the full aura version.", "Raid"),
    ("Fox Lab — Aura Version Setup", "https://foxlabstudio.weebly.com/aura-version.html", "Setup guide for the full visual+audio private-aura version of Raid Assist.", "Raid"),
    ("Fox Lab — Private Auras Setup", "https://foxlabstudio.weebly.com/private-auras-setup.html", "Setup guide for the audio-only, easier-install version of Raid Assist.", "Raid"),
]
voice_intro = '<p class="section-note" style="margin-bottom:1.25rem; max-width:var(--measure);">WeakAuras\' own sound-condition system no longer functions under patch 12.1\'s secret-values restrictions on other units\' data. These packs, plus the ThisWeeksAuras/M33kAuras framework in Addons, are the current working replacements for spoken alerts.</p>'
voice_body = single(table3(f"{len(voice)} packs", voice), extra=voice_intro)
voice_total = len(voice)

# ===== MY SETUP =====
setup = [
    ("BigWigs + LittleWigs", "https://www.curseforge.com/wow/addons/search?search=BigWigs", "Boss and dungeon encounter timers and warnings, current and legacy content."),
    ("Deadly Boss Mods (DBM)", "https://www.curseforge.com/wow/addons/search?search=Deadly+Boss+Mods", "Second boss/dungeon timer addon, run in parallel with BigWigs."),
    ("EllesmereUI", "https://www.curseforge.com/wow/addons/search?search=EllesmereUI", "Full UI replacement: action bars, unit frames, nameplates, cooldown manager, data bars."),
    ("EnhanceQoL", "https://www.curseforge.com/wow/addons/search?search=EnhanceQoL", "Quality-of-life suite: cooldown panels, damage meter, dungeon and raid utilities."),
    ("Grid2", "https://www.curseforge.com/wow/addons/search?search=Grid2", "Compact, clickable raid-frame addon."),
    ("Northern Sky Raid Tools", "addons.html", "Raid cooldown reminders and shared notes — see Addons."),
    ("Plater", "https://www.curseforge.com/wow/addons/search?search=Plater", "Customizable nameplate addon."),
    ("RaiderIO", "https://www.curseforge.com/wow/addons/search?search=RaiderIO", "In-game Mythic+ score and raid progress lookups on frames and Group Finder."),
    ("RCLootCouncil", "https://www.curseforge.com/wow/addons/rclootcouncil", "Loot council roll and award tracking."),
    ("Simulationcraft", "https://www.curseforge.com/wow/addons/search?search=Simulationcraft", "In-game companion addon for the SimC gear and talent simulator."),
    ("TomTom", "https://www.curseforge.com/wow/addons/search?search=TomTom", "Waypoint and coordinate tracking."),
    ("Wago App Companion / WagoUI", "https://wago.io", "Wago.io integration for importable UI profiles and auras."),
    ("HandyNotes (+ packs)", "https://www.curseforge.com/wow/addons/search?search=HandyNotes", "Map pins for treasures, delves, and event locations."),
    ("Gandalin's Gearing Guide", "https://www.curseforge.com/wow/addons/search?search=Gandalin", "In-game gearing and upgrade-priority guide. Author's link hub: linktr.ee/GandalinGaming."),
    ("Midnight Upgrade Calculator", "https://www.curseforge.com/wow/addons/search?search=Midnight+Upgrade+Calculator", "In-game item-upgrade track calculator."),
    ("MPlusMarker", "https://www.curseforge.com/wow/addons/search?search=MPlusMarker", "Mythic+ pull and target marking helper."),
    ("WarbandNexus", "https://www.curseforge.com/wow/addons/search?search=WarbandNexus", "Cross-character warband management."),
    ("Auctionator", "https://www.curseforge.com/wow/addons/search?search=Auctionator", "Auction house search and pricing."),
]
setup_note = '<p class="setup-note">Pulled directly from the live AddOns folder. Shared here so the team can copy anything useful; nothing above requires matching it.</p>'
setup_body = single(table2(f"{len(setup)} installed addons", setup), extra=setup_note)
setup_total = len(setup)

# ===== ADDONS (minimized) =====
addons = [
    ("Mythic Dungeon Tools", "https://www.curseforge.com/wow/addons/mythic-dungeon-tools", "Plans and shares Mythic+ pull routes with boss and trash positioning before the key starts.", "M+"),
    ("Northern Sky Raid Tools", "https://www.curseforge.com/wow/addons/northern-sky-raid-tools", "Raid cooldown reminders and shared notes, rebuilt around patch 12.1's secret-values addon limits.", "Raid"),
    ("ThisWeeksAuras", "https://www.curseforge.com/wow/addons/thisweeksauras", "Midnight-ready fork of M33kAuras (itself a fork of WeakAuras 2), updated for secret-values compatibility. Import strings from WeakAuras and M33kAuras both work. Upstream: <a href=\"https://github.com/m33shoq/M33kAuras\" target=\"_blank\" rel=\"noopener noreferrer\">M33kAuras on GitHub</a>.", "Both"),
    ("Boss Mentor", "https://www.curseforge.com/wow/addons/boss-mentor", "Season 2-ready tactics overlay that explains what to do about a mechanic, not just that it's happening.", "Both"),
    ("Mythic Plus Utility (MPU)", "https://www.curseforge.com/wow/addons/mythic-plus-utility-mpu", "Shows which utility ability to bring and where to use it in a Mythic+ run.", "M+"),
    ("ElvUI", "https://tukui.org/elvui", "Full UI replacement — unit frames, action bars, nameplates, and data bars in one cohesive skin.", "Both"),
    ("Details! Damage Meter", "https://www.curseforge.com/wow/addons/details", "Full combat-analysis meter with segment breakdowns and custom windows.", "Both"),
    ("VuhDo", "https://www.curseforge.com/wow/addons/vuhdo", "Click-heal raid frames with buff/debuff tracking and main-tank management.", "Raid"),
    ("Angry Assignments Plus", "https://www.curseforge.com/wow/addons/angry-assignments-plus", "Shared, editable raid assignment pages — cooldowns, healing, interrupts — synced guild-wide and shown in combat.", "Raid"),
    ("Keystone Karma", "https://www.curseforge.com/wow/addons/keystone-karma", "Tracks who you've run keys with and lets you rate them, visible in LFG — a private alternative to keeping notes on a friends list.", "M+"),
    ("CadenceMDR (addon)", "https://www.curseforge.com/wow/addons/cadencemdr", "In-game cooldown countdown built from a plan exported off the CadenceMDR site (see Sites &amp; Calculators).", "M+"),
    ("Raider.IO (addon)", "https://www.curseforge.com/wow/addons/raiderio", "Shows M+ score, raid progress, and recruitment info on unit frames and tooltips in-game.", "Both"),
]
addons_intro = '<p class="section-note" style="margin-bottom:1.25rem; max-width:var(--measure);">A short, curated list — not a full CurseForge mirror. For everything actually installed on this account, see My Setup.</p>'
addons_body = single(table3(f"{len(addons)} addons", addons), extra=addons_intro)
addons_total = len(addons)

counts = {
    "SITES_COUNT": sites_total,
    "GUIDES_COUNT": guides_total,
    "CHEATS_COUNT": cheats_total,
    "VIDEOS_COUNT": videos_total,
    "TOOLS_COUNT": tools_total,
    "VOICE_COUNT": voice_total,
    "SETUP_COUNT": setup_total,
    "ADDONS_COUNT": addons_total,
}

grand_total = sites_total + guides_total + cheats_total + videos_total + tools_total + voice_total + addons_total

# ===== OVERVIEW =====
overview_cards = [
    ("sites.html", "Sites &amp; Calculators", sites_total, "Logs, sims, gearing, and planning tools."),
    ("guides.html", "Guides", guides_total, "Class, spec, raid, and season reference."),
    ("cheatsheets.html", "Cheat Sheets &amp; Images", cheats_total, "Printable charts, in-game imports, shared trackers."),
    ("videos.html", "Videos", videos_total, "Walkthroughs worth the watch."),
    ("tools.html", "Desktop Tools", tools_total, "Software that runs outside the game client."),
    ("voice.html", "Voice-Cue Packs", voice_total, "Spoken boss-ability call-outs."),
    ("my-setup.html", "My Setup", setup_total, "What this account is currently running, live."),
    ("addons.html", "Addons", addons_total, "A short, curated list — not a full mirror."),
]
overview_rows = "".join(
    f'''            <tr>
              <td class="col-name"><a href="{href}">{label}</a></td>
              <td class="col-desc">{note}</td>
              <td class="col-tag"><span class="tag tag--both">{n}</span></td>
            </tr>
'''
    for href, label, n, note in overview_cards
)
overview_table = f'''      <div class="table-wrap">
        <table class="directory">
          <caption>{len(overview_cards)} sections &middot; {grand_total} entries &middot; {setup_total} in My Setup</caption>
          <thead>
            <tr><th scope="col">Section</th><th scope="col">What's in it</th><th scope="col">Count</th></tr>
          </thead>
          <tbody>
{overview_rows}          </tbody>
        </table>
      </div>
'''
overview_intro = '<p class="section-note" style="max-width:var(--measure); margin-bottom:1.5rem;">A working directory for the guild: what to install, what to bookmark, and what this account is currently running. Every entry is a live, checked link — nothing here is aspirational.</p>'
overview_body = single(overview_table, extra=overview_intro)

PAGE_CONTENT = {
    "index.html": ("Overview", f"{grand_total} entries across {len(overview_cards)} sections", overview_body),
    "sites.html": ("Sites & Calculators", f"{sites_total} sites", sites_body),
    "guides.html": ("Guides", f"{guides_total} guides", guides_body),
    "cheatsheets.html": ("Cheat Sheets & Images", f"{cheats_total} references", cheats_body),
    "videos.html": ("Videos", f"{videos_total} videos", videos_body),
    "tools.html": ("Desktop Tools", f"{tools_total} tools", tools_body),
    "voice.html": ("Voice-Cue Packs", f"{voice_total} packs", voice_body),
    "my-setup.html": ("My Setup", f"{setup_total} installed addons &middot; checked live, not aspirational", setup_body),
    "addons.html": ("Addons", f"{addons_total} addons &middot; curated, not exhaustive", addons_body),
}

os.makedirs(OUT, exist_ok=True)
for fname, (title, meta, body) in PAGE_CONTENT.items():
    html_out = render_chrome(fname, title, meta, body, counts)
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(html_out)

print("Wrote:", ", ".join(PAGE_CONTENT.keys()))
print("Counts:", counts)
print("Grand total (excl My Setup):", grand_total)
