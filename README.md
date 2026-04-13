# Chicago Bears 2024 Stats Dashboard

A full-stack web application for exploring Chicago Bears 2024 season statistics — built with a Python/Flask REST API backend and a vanilla HTML/CSS/JS frontend. No frontend framework or build step required.

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python) ![Flask](https://img.shields.io/badge/Flask-3.0-green?logo=flask) ![SQLite](https://img.shields.io/badge/SQLite-3-lightblue?logo=sqlite) ![License](https://img.shields.io/badge/License-MIT-orange)

---

## Features

- **Overview Dashboard** — season leaders with horizontal bar charts for rushing, receiving, and tackles
- **Passing Stats** — completions, yards, TDs, INTs, passer rating
- **Rushing Stats** — attempts, yards, avg, TDs with visual bars
- **Receiving Stats** — receptions, yards, avg, TDs
- **Defense** — tackles (solo/assist/sack/FF) and interceptions
- **Special Teams** — field goals by range, punting, kick returns
- **Roster Browser** — all players with position filter, height/weight/college/experience

---

## Project Structure

```
bears-stats-app/
├── backend/
│   └── app.py          # Flask REST API
├── frontend/
│   └── index.html      # Single-page dashboard (no build needed)
├── requirements.txt    # Python dependencies
├── start.sh            # One-command launcher (Mac/Linux)
├── .gitignore
└── README.md
```

> **Note:** The `bears.db` SQLite database is not tracked by git. Place your `bears.db` in the project root before running.

---

## Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/bears-stats-app.git
cd bears-stats-app
```

### 2. Add the database

```bash
cp /path/to/your/bears.db .
```

### 3. Install Python dependencies

```bash
pip3 install -r requirements.txt
```

### 4. Run the app

**Option A — one command (Mac/Linux):**
```bash
bash start.sh
```

**Option B — manually:**
```bash
# Terminal 1: start the backend
python3 backend/app.py

# Terminal 2: open the frontend
open frontend/index.html        # Mac
xdg-open frontend/index.html    # Linux
```

The API runs at `http://localhost:5001`. Open `frontend/index.html` in any browser.

---

## API Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/roster` | Full team roster |
| `GET` | `/api/passing` | Passing stats |
| `GET` | `/api/rushing` | Rushing stats |
| `GET` | `/api/receiving` | Receiving stats |
| `GET` | `/api/tackles` | Tackle stats |
| `GET` | `/api/interceptions` | Interception stats |
| `GET` | `/api/field_goals` | Field goals by range |
| `GET` | `/api/stats/summary` | Season leaders summary |
| `GET` | `/api/positions` | Player count by position |

---

## Database Schema

The app expects a SQLite file (`bears.db`) in the project root with these tables:

| Table | Key Columns |
|-------|-------------|
| `roster` | name, number, position, height, weight, age, experience, college |
| `passing` | player, att, comp, yds, comp_pct, yds_per_att, td, int_thrown, sck, rate |
| `rushing` | player, att, yds, yds_per_att, long, td |
| `receiving` | player, rec, yds, yds_per_rec, long, td |
| `tackles` | player, total, solo, assist, sck, forced_fmbl |
| `interceptions` | player, int_caught, yds, yds_per_ret, long, tds |
| `field_goals` | player, fg_20_29, fg_30_39, fg_40_49, fg_50_59, fg_60_plus |
| `punting` | player, punts, yds, avg, long, in_20, net_avg |
| `kick_returns` | player, ret, yds, yds_per_ret, long, td |

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3, Flask, Flask-CORS |
| Database | SQLite 3 (Python built-in `sqlite3`) |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Fonts | Google Fonts — Barlow Condensed + Barlow |

No npm, no webpack, no React — the frontend is a single `.html` file.

---

## License

MIT
