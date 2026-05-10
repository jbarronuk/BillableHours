# BillableHours

Automated work tracking dashboard that monitors Clockify time entries and sends push notifications when billable hours need attention.

## What it does

- Pulls time tracking data from the Clockify API
- Generates a live dashboard hosted on GitHub Pages
- Sends push notifications via ntfy.sh when billable hours need attention
- Runs automatically on a schedule using GitHub Actions — no server required

## Stack

| Tool | Purpose |
|---|---|
| [Clockify](https://clockify.me) | Time tracking source |
| [ntfy.sh](https://ntfy.sh) | Push notifications |
| [GitHub Actions](https://github.com/features/actions) | Scheduled automation |
| [GitHub Pages](https://pages.github.com) | Dashboard hosting |
| Python | Glue |

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/jbarronuk/BillableHours.git
```

### 2. Add secrets

Go to **Settings → Secrets and variables → Actions** and add:

| Secret | Where to find it |
|---|---|
| `CLOCKIFY_API_KEY` | clockify.me → Profile → API |
| `CLOCKIFY_WORKSPACE` | clockify.me → Settings → copy from URL |
| `NTFY_TOPIC` | Your chosen ntfy.sh topic name |

### 3. Enable GitHub Pages

Go to **Settings → Pages** and set the source to **main branch / root**.

Your dashboard will be live at `https://yourusername.github.io/BillableHours`

## Schedule

The dashboard regenerates every 15 minutes. Notifications are sent at 19:00 UTC on weekdays.

## Project structure

```
├── generate.py              # Generates the dashboard HTML
├── notify.py                # Sends ntfy.sh notifications
├── .github/
│   └── workflows/
│       ├── dashboard.yml    # Dashboard generation schedule
│       └── notify.yml       # Notification schedule
└── index.html               # Generated dashboard (do not edit manually)
```