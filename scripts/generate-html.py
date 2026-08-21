#!/usr/bin/env python3
"""
Generate legal-tech-directory.html from README.md.

Run from the repo root:
    python3 scripts/generate-html.py
"""
import re
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
README = ROOT / "README.md"
OUTPUT = ROOT / "legal-tech-directory.html"


def parse_entries(content):
    entries = []
    current_category = None
    current_subcategory = None

    for line in content.split("\n"):
        if line.startswith("## ") and not line.startswith("### "):
            current_category = line[3:].strip()
            current_subcategory = None
        elif line.startswith("### "):
            current_subcategory = line[4:].strip()
        elif (
            line.startswith("| ")
            and current_category
            and current_category not in ("Contents", "Jurisdiction Flags")
        ):
            if "---" in line or line.startswith("| Name") or line.startswith("| Flag"):
                continue

            parts = [p.strip() for p in line.split("|")]
            if len(parts) < 4:
                continue

            name_cell = parts[1] if len(parts) > 1 else ""
            desc_cell = parts[2] if len(parts) > 2 else ""
            tech_cell = parts[3] if len(parts) > 3 else ""
            license_cell = parts[4] if len(parts) > 4 else ""
            date_cell = parts[5] if len(parts) > 5 else ""

            jurisdictions = re.findall(r'alt="([A-Z]{2})"', name_cell)
            is_stale = "⚠️ Stale" in desc_cell

            url_match = re.search(r"\*{0,2}\[([^\]]+)\]\(([^)]+)\)", name_cell)
            if not url_match:
                continue

            name = url_match.group(1)
            url = url_match.group(2)

            description = re.sub(r"⚠️ Stale[^\s]*(\s*\([^)]*\))?", "", desc_cell).strip()
            description = re.sub(r"\*+", "", description).strip()

            tech_stack = re.sub(r"\*+", "", tech_cell).strip()
            license_str = re.sub(r"\*+", "", license_cell).strip()
            if license_str == "—":
                license_str = ""
            date_str = re.sub(r"\*+", "", date_cell).strip()

            if name and url:
                category_display = current_category
                if current_subcategory:
                    category_display = f"{current_category} › {current_subcategory}"

                entries.append(
                    {
                        "name": name,
                        "url": url,
                        "description": description,
                        "techStack": tech_stack,
                        "license": license_str,
                        "dateAdded": date_str,
                        "category": category_display,
                        "categoryMain": current_category,
                        "jurisdictions": jurisdictions,
                        "isStale": is_stale,
                    }
                )

    return entries


def build_html(entries):
    categories = sorted(set(e["categoryMain"] for e in entries))
    licenses = sorted(set(e["license"] for e in entries if e["license"]))
    jurisdictions = sorted(set(j for e in entries for j in e["jurisdictions"]))

    jur_names = {
        "AR": "Argentina", "AT": "Austria", "BR": "Brazil", "CH": "Switzerland",
        "CN": "China", "DE": "Germany", "ES": "Spain", "EU": "European Union",
        "FR": "France", "IN": "India", "IT": "Italy", "JP": "Japan",
        "KR": "South Korea", "NL": "Netherlands", "NO": "Norway", "PH": "Philippines",
        "PL": "Poland", "SG": "Singapore", "TR": "Turkey", "TW": "Taiwan",
        "UA": "Ukraine", "UK": "United Kingdom", "US": "United States", "ZA": "South Africa",
    }

    data_json = json.dumps(entries, separators=(",", ":"))

    cat_options = "\n".join(f'<option value="{c}">{c}</option>' for c in categories)
    jur_options = "\n".join(
        f'<option value="{j}">{jur_names.get(j, j)} ({j})</option>' for j in jurisdictions
    )
    lic_options = "\n".join(f'<option value="{l}">{l}</option>' for l in licenses)

    entry_count = len(entries)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Awesome Legal Tech — Interactive Directory</title>
<style>
  :root {{
    --bg: #0f1117;
    --surface: #1a1d27;
    --surface2: #22263a;
    --border: #2d3150;
    --accent: #6c8ef7;
    --text: #e2e8f0;
    --text2: #94a3b8;
    --text3: #64748b;
    --stale: #78350f;
    --stale-text: #fbbf24;
    --radius: 8px;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ background: var(--bg); color: var(--text); font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; font-size: 14px; line-height: 1.5; min-height: 100vh; }}

  header {{ background: linear-gradient(135deg, #1a1d27 0%, #0f1117 100%); border-bottom: 1px solid var(--border); padding: 24px 32px; }}
  header h1 {{ font-size: 28px; font-weight: 700; letter-spacing: -0.5px; }}
  header h1 span {{ color: var(--accent); }}
  header p {{ color: var(--text2); margin-top: 4px; font-size: 14px; }}
  .header-meta {{ display: flex; gap: 16px; margin-top: 12px; flex-wrap: wrap; }}
  .meta-badge {{ background: var(--surface2); border: 1px solid var(--border); border-radius: 20px; padding: 4px 12px; font-size: 12px; color: var(--text2); }}
  .meta-badge b {{ color: var(--accent); }}
  .gh-link {{ margin-left: auto; display: flex; align-items: center; gap: 6px; color: var(--text3); font-size: 12px; text-decoration: none; padding: 4px 12px; border: 1px solid var(--border); border-radius: 20px; transition: color .15s, border-color .15s; }}
  .gh-link:hover {{ color: var(--accent); border-color: var(--accent); }}

  .controls {{ background: var(--surface); border-bottom: 1px solid var(--border); padding: 16px 32px; display: flex; flex-direction: column; gap: 12px; position: sticky; top: 0; z-index: 100; }}
  .search-row {{ display: flex; gap: 12px; align-items: center; flex-wrap: wrap; }}
  .search-wrap {{ position: relative; flex: 1; min-width: 260px; max-width: 500px; }}
  .search-wrap svg {{ position: absolute; left: 12px; top: 50%; transform: translateY(-50%); color: var(--text3); width: 16px; height: 16px; }}
  #search {{ width: 100%; background: var(--surface2); border: 1px solid var(--border); border-radius: var(--radius); padding: 9px 12px 9px 38px; color: var(--text); font-size: 14px; outline: none; transition: border-color .2s; }}
  #search:focus {{ border-color: var(--accent); }}
  #search::placeholder {{ color: var(--text3); }}
  .result-count {{ color: var(--text2); font-size: 13px; white-space: nowrap; }}
  .semantic-note {{ display: flex; align-items: center; gap: 6px; padding: 6px 12px; background: #1e1b4b; border: 1px solid #3730a3; border-radius: 6px; font-size: 12px; color: #a5b4fc; margin-left: auto; white-space: nowrap; }}

  .filter-row {{ display: flex; gap: 10px; flex-wrap: wrap; align-items: center; }}
  .filter-label {{ font-size: 12px; color: var(--text3); font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }}
  select {{ background: var(--surface2); border: 1px solid var(--border); border-radius: 6px; padding: 6px 28px 6px 10px; color: var(--text); font-size: 13px; outline: none; cursor: pointer; transition: border-color .2s; appearance: none; background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='%2364748b' stroke-width='2'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E"); background-repeat: no-repeat; background-position: right 8px center; }}
  select:focus {{ border-color: var(--accent); }}
  .toggle-stale {{ display: flex; align-items: center; gap: 6px; cursor: pointer; font-size: 13px; color: var(--text2); user-select: none; }}
  .toggle-stale input {{ accent-color: var(--accent); width: 14px; height: 14px; cursor: pointer; }}

  .sort-btns {{ display: flex; gap: 6px; margin-left: auto; }}
  .sort-btns button {{ background: var(--surface2); border: 1px solid var(--border); border-radius: 6px; padding: 6px 12px; color: var(--text2); font-size: 12px; cursor: pointer; transition: all .15s; }}
  .sort-btns button.active {{ background: var(--accent); border-color: var(--accent); color: white; }}
  .sort-btns button:hover:not(.active) {{ border-color: var(--accent); color: var(--accent); }}

  .main {{ padding: 20px 32px; overflow-x: auto; }}
  table {{ width: 100%; border-collapse: separate; border-spacing: 0; }}
  thead th {{ background: var(--surface); border-bottom: 2px solid var(--border); padding: 10px 14px; text-align: left; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; color: var(--text3); cursor: pointer; white-space: nowrap; user-select: none; }}
  thead th:hover {{ color: var(--accent); }}
  tbody tr {{ border-bottom: 1px solid var(--border); transition: background .1s; }}
  tbody tr:hover {{ background: var(--surface); }}
  tbody tr.stale {{ opacity: 0.6; }}
  td {{ padding: 11px 14px; vertical-align: top; }}

  .entry-name {{ font-weight: 600; color: var(--text); text-decoration: none; transition: color .15s; display: flex; align-items: flex-start; gap: 6px; }}
  .entry-name:hover {{ color: var(--accent); }}
  .entry-name svg {{ flex-shrink: 0; margin-top: 2px; opacity: 0.4; }}
  .stale-badge {{ display: inline-flex; align-items: center; gap: 3px; background: var(--stale); color: var(--stale-text); border-radius: 4px; padding: 1px 6px; font-size: 10px; font-weight: 600; margin-top: 4px; }}
  .desc {{ font-size: 13px; color: var(--text2); max-width: 400px; }}
  .cat-pill {{ background: var(--surface2); border-radius: 4px; padding: 2px 7px; font-size: 12px; color: var(--text3); white-space: nowrap; }}
  .subcat {{ font-size: 11px; color: var(--text3); display: block; margin-top: 3px; }}
  .flags {{ display: flex; gap: 3px; flex-wrap: wrap; }}
  .flag-img {{ border-radius: 2px; }}
  .tech {{ font-size: 12px; color: var(--text3); max-width: 160px; }}
  .license-badge {{ display: inline-block; background: var(--surface2); border: 1px solid var(--border); border-radius: 4px; padding: 1px 7px; font-size: 11px; color: var(--text3); white-space: nowrap; }}
  .license-badge.foss {{ border-color: #166534; color: #4ade80; background: #052e16; }}
  .license-badge.nonfoss {{ border-color: #7c3aed; color: #c4b5fd; background: #2e1065; }}
  .date {{ font-size: 12px; color: var(--text3); white-space: nowrap; }}
  .hl {{ background: #3b4219; color: #facc15; border-radius: 2px; padding: 0 1px; }}

  .empty-state {{ text-align: center; padding: 80px 20px; color: var(--text3); }}
  .empty-state svg {{ width: 48px; height: 48px; margin: 0 auto 16px; opacity: 0.3; display: block; }}
  .empty-state h3 {{ font-size: 18px; color: var(--text2); margin-bottom: 8px; }}

  @media (max-width: 768px) {{
    header, .controls, .main {{ padding-left: 16px; padding-right: 16px; }}
    .sort-btns, .semantic-note {{ display: none; }}
  }}
</style>
</head>
<body>

<header>
  <h1>Awesome <span>Legal Tech</span></h1>
  <p>A curated directory of legal technology tools, AI models, and resources</p>
  <div class="header-meta">
    <div class="meta-badge">⚡ <b id="entry-count">{entry_count}</b> entries</div>
    <div class="meta-badge"><b>{len(categories)}</b> categories</div>
    <div class="meta-badge"><b>{len(jurisdictions)}</b> jurisdictions</div>
    <a class="gh-link" href="https://github.com/tanko-r/awesome-legal-tech" target="_blank" rel="noopener">
      <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.477 2 2 6.477 2 12c0 4.42 2.865 8.166 6.839 9.489.5.092.682-.217.682-.482 0-.237-.008-.866-.013-1.7-2.782.603-3.369-1.342-3.369-1.342-.454-1.155-1.11-1.463-1.11-1.463-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.529 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.11-4.555-4.943 0-1.091.39-1.984 1.029-2.683-.103-.253-.446-1.27.098-2.647 0 0 .84-.268 2.75 1.026A9.578 9.578 0 0 1 12 6.836c.85.004 1.705.114 2.504.336 1.909-1.294 2.747-1.026 2.747-1.026.546 1.377.202 2.394.1 2.647.64.699 1.028 1.592 1.028 2.683 0 3.842-2.339 4.687-4.566 4.935.359.309.678.919.678 1.852 0 1.336-.012 2.415-.012 2.741 0 .267.18.579.688.481C19.138 20.163 22 16.418 22 12c0-5.523-4.477-10-10-10z"/></svg>
      View on GitHub
    </a>
  </div>
</header>

<div class="controls">
  <div class="search-row">
    <div class="search-wrap">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
      <input type="text" id="search" placeholder="Search names, descriptions, tech stacks, jurisdictions…" autocomplete="off" spellcheck="false">
    </div>
    <span class="result-count" id="result-count"></span>
    <div class="semantic-note">
      <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 8v4l3 3"/></svg>
      Full-text + fuzzy search
    </div>
  </div>
  <div class="filter-row">
    <span class="filter-label">Filter:</span>
    <select id="filter-category">
      <option value="">All Categories</option>
      {cat_options}
    </select>
    <select id="filter-jurisdiction">
      <option value="">All Jurisdictions</option>
      {jur_options}
      <option value="GLOBAL">Global / Jurisdiction-agnostic</option>
    </select>
    <select id="filter-license">
      <option value="">All Licenses</option>
      {lic_options}
    </select>
    <label class="toggle-stale">
      <input type="checkbox" id="hide-stale" checked>
      Hide stale entries
    </label>
    <div class="sort-btns">
      <button id="sort-name" onclick="setSort('name')">Name</button>
      <button id="sort-date" class="active" onclick="setSort('date')">Date ↓</button>
      <button id="sort-category" onclick="setSort('category')">Category</button>
    </div>
  </div>
</div>

<div class="main">
  <table id="main-table">
    <thead>
      <tr>
        <th onclick="setSort('name')">Name</th>
        <th>Description</th>
        <th onclick="setSort('category')">Category</th>
        <th>Jurisdiction</th>
        <th>Tech Stack</th>
        <th onclick="setSort('license')">License</th>
        <th onclick="setSort('date')">Added</th>
      </tr>
    </thead>
    <tbody id="table-body"></tbody>
  </table>
  <div id="empty-state" class="empty-state" style="display:none">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
    <h3>No results found</h3>
    <p>Try different search terms or clear some filters</p>
  </div>
</div>

<script>
const DATA = {data_json};

// ── Search engine (BM25-style inverted index + prefix + substring) ──
(function() {{
  const STOP = new Set(['the','a','an','and','or','in','on','at','to','for','of','with','by','from','is','are','was','were','be','been','has','have','had','that','this','it','its','as','into','via','per','not','no','can','also','which','their','they','these','those','than','when','where','what','how','who','will','would','could','should','may','might','using','used','use','provides','provide','providing','support','supports','based','built','designed','allows','enabling','enables','make','makes','help','helps']);
  function tok(t) {{ return (t||'').toLowerCase().replace(/[^a-z0-9\\s]/g,' ').split(/\\s+/).filter(w=>w.length>1); }}
  const index = {{}};
  DATA.forEach((d,i) => {{
    const words = tok([d.name,d.description,d.techStack,d.categoryMain,d.license].join(' ')).filter(w=>!STOP.has(w));
    words.forEach(w => {{ if(!index[w]) index[w]={{}}; index[w][i]=(index[w][i]||0)+1; }});
  }});
  window._search = q => {{
    const terms = tok(q).filter(t=>t.length>0);
    if (!terms.length) return null;
    const N = DATA.length, scores = {{}};
    terms.forEach(term => {{
      // exact
      if (index[term]) {{
        const df = Object.keys(index[term]).length;
        const idf = Math.log((N-df+0.5)/(df+0.5)+1);
        Object.entries(index[term]).forEach(([i,tf]) => {{ scores[i]=(scores[i]||0)+idf*(tf*2.5)/(tf+1.5); }});
      }}
      // prefix
      if (term.length >= 3) Object.keys(index).forEach(k => {{
        if (k!==term && k.startsWith(term)) {{
          const df=Object.keys(index[k]).length, idf=Math.log((N-df+0.5)/(df+0.5)+1)*0.6;
          Object.entries(index[k]).forEach(([i,tf]) => {{ scores[i]=(scores[i]||0)+idf*(tf*2.5)/(tf+1.5); }});
        }}
      }});
      // substring fallback
      DATA.forEach((d,i) => {{ if((d.name+' '+d.description).toLowerCase().includes(term)) scores[i]=(scores[i]||0)+0.4; }});
    }});
    return new Set(Object.entries(scores).filter(([,s])=>s>0).map(([i])=>parseInt(i)));
  }};
}})();

// ── Flags ──
const JUR = {{AR:'Argentina',AT:'Austria',BR:'Brazil',CH:'Switzerland',CN:'China',DE:'Germany',ES:'Spain',EU:'European Union',FR:'France',IN:'India',IT:'Italy',JP:'Japan',KR:'South Korea',NL:'Netherlands',NO:'Norway',PH:'Philippines',PL:'Poland',SG:'Singapore',TR:'Turkey',TW:'Taiwan',UA:'Ukraine',UK:'United Kingdom',US:'United States',ZA:'South Africa'}};
function flagHtml(c) {{ const cc=({{UK:'gb',EU:'eu'}}[c]||c).toLowerCase(); return `<img class="flag-img" src="https://flagcdn.com/w20/${{cc}}.png" width="20" height="15" alt="${{c}}" title="${{JUR[c]||c}}">`; }}

// ── License badge ──
function licBadge(l) {{
  if (!l||l==='No license'||l==='Unknown') return `<span class="license-badge">${{l||'Unknown'}}</span>`;
  if (l==='Not FOSS') return `<span class="license-badge nonfoss">Proprietary</span>`;
  return `<span class="license-badge foss">${{l}}</span>`;
}}

// ── Highlight ──
function hl(text, q) {{
  if (!q||!text) return text||'';
  const terms = q.toLowerCase().replace(/[^a-z0-9\\s]/g,' ').split(/\\s+/).filter(t=>t.length>1);
  if (!terms.length) return text;
  const re = new RegExp(`(${{terms.map(t=>t.replace(/[.*+?^${{}}()|[\\]\\\\]/g,'\\\\$&')).join('|')}})`, 'gi');
  return text.replace(re, '<span class="hl">$1</span>');
}}

// ── Sort state ──
let curSort = 'date', sortDirs = {{name:1, date:-1, category:1, license:1}};
function setSort(f) {{
  if (curSort===f) sortDirs[f]*=-1; else curSort=f;
  ['name','date','category'].forEach(x => {{
    const b=document.getElementById('sort-'+x);
    if (!b) return;
    b.classList.toggle('active', x===curSort);
    b.textContent = x==='name'?'Name': x==='date'?'Date': 'Category';
    if (x===curSort) b.textContent += sortDirs[x]===-1?' ↓':' ↑';
  }});
  render();
}}

// ── Render ──
function render() {{
  const q = document.getElementById('search').value;
  const cat = document.getElementById('filter-category').value;
  const jur = document.getElementById('filter-jurisdiction').value;
  const lic = document.getElementById('filter-license').value;
  const hideStale = document.getElementById('hide-stale').checked;
  const matches = window._search(q);

  let results = DATA
    .map((e,i) => ({{e,i}}))
    .filter(({{e,i}}) => {{
      if (matches && !matches.has(i)) return false;
      if (hideStale && e.isStale) return false;
      if (cat && e.categoryMain !== cat) return false;
      if (lic && e.license !== lic) return false;
      if (jur) {{
        if (jur==='GLOBAL') {{ if (e.jurisdictions.length>0) return false; }}
        else {{ if (!e.jurisdictions.includes(jur)) return false; }}
      }}
      return true;
    }});

  results.sort((a,b) => {{
    const k=curSort, d=sortDirs[k];
    const av = k==='name'?a.e.name.toLowerCase(): k==='date'?a.e.dateAdded: k==='category'?a.e.categoryMain.toLowerCase(): a.e.license.toLowerCase();
    const bv = k==='name'?b.e.name.toLowerCase(): k==='date'?b.e.dateAdded: k==='category'?b.e.categoryMain.toLowerCase(): b.e.license.toLowerCase();
    return av<bv?-d:av>bv?d:0;
  }});

  const tbody = document.getElementById('table-body');
  const empty = document.getElementById('empty-state');
  document.getElementById('result-count').textContent = results.length===DATA.length
    ? `All ${{DATA.length}} entries`
    : `${{results.length}} of ${{DATA.length}} entries`;

  if (!results.length) {{ tbody.innerHTML=''; empty.style.display=''; return; }}
  empty.style.display='none';

  tbody.innerHTML = results.map(({{e}}) => {{
    const flags = e.jurisdictions.length
      ? `<div class="flags">${{e.jurisdictions.map(flagHtml).join('')}}</div>`
      : '<span style="color:var(--text3);font-size:11px">Global</span>';
    const catParts = e.category.split(' › ');
    const catHtml = catParts.length>1
      ? `<span class="cat-pill">${{catParts[0]}}</span><span class="subcat">${{catParts[1]}}</span>`
      : `<span class="cat-pill">${{catParts[0]}}</span>`;
    return `<tr class="${{e.isStale?'stale':''}}">
      <td style="min-width:180px;max-width:230px">
        <a class="entry-name" href="${{e.url}}" target="_blank" rel="noopener">
          <svg xmlns="http://www.w3.org/2000/svg" width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
          ${{hl(e.name,q)}}
        </a>
        ${{e.isStale?'<span class="stale-badge">⚠ Stale</span>':''}}
      </td>
      <td><div class="desc">${{hl(e.description,q)}}</div></td>
      <td style="min-width:160px">${{catHtml}}</td>
      <td style="min-width:60px">${{flags}}</td>
      <td><div class="tech">${{e.techStack||'<span style="color:var(--text3)">—</span>'}}</div></td>
      <td>${{licBadge(e.license)}}</td>
      <td><span class="date">${{e.dateAdded}}</span></td>
    </tr>`;
  }}).join('');
}}

document.getElementById('search').addEventListener('input', (() => {{ let t; return () => {{ clearTimeout(t); t=setTimeout(render,120); }}; }})());
['filter-category','filter-jurisdiction','filter-license','hide-stale'].forEach(id => document.getElementById(id).addEventListener('change', render));

render();
</script>
</body>
</html>"""


def main():
    print(f"Reading {README}…")
    content = README.read_text(encoding="utf-8")

    print("Parsing entries…")
    entries = parse_entries(content)
    print(f"  → {len(entries)} entries found")

    print("Building HTML…")
    html = build_html(entries)

    OUTPUT.write_text(html, encoding="utf-8")
    print(f"  → Written to {OUTPUT} ({len(html):,} bytes)")


if __name__ == "__main__":
    main()
