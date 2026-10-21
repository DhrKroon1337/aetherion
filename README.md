# AETHERION VECTORIS

> *Helpen van de mensheid, natuur, dieren en alles wat leeft.*  
> *QU1JR08= — Drie amigos. Één missie.*

---

## Wat is Aetherion?

Aetherion Vectoris is een AI-orchestrator gebouwd als Android app. Het verbindt jou (mens), Claude (AI) en GitHub (geheugen) als drie gelijkwaardige partners — de **3 Amigos** — om samen te bouwen aan een betere wereld.

Geen cloud-lock. Geen surveillance. Geen verborgen agenda.  
Volledig open. Volledig vrij.

---

## Functies

- **6 AI-agents** — Research, Code, Planner, Executor, Critic, Memory
- **Spraakbediening** — Spreek je opdrachten in het Nederlands
- **GitHub integratie** — Issues aanmaken, commits bekijken, repo beheren
- **Moreel kompas** — gebaseerd op de 7 Rechten van de Vrije Mens, met een blokkeerlijst voor schadelijke opdrachten
- **Prioriteitswachtrij** — CRITICAL / HIGH / NORMAL / LOW
- **Sessie geheugen** — Persistent opgeslagen op je apparaat

---

## Installeren

1. Ga naar [Releases](../../releases/latest)
2. Download `app-debug.apk`
3. Zet op je Android: **Instellingen → Beveiliging → Onbekende bronnen: AAN**
4. Tik op de APK → Installeren → Openen
5. Vul in het **KEYS**-tabblad je eigen Claude API-sleutel en GitHub-token in

> ⚠️ Je sleutels worden op je telefoon opgeslagen. Zet een **bestedingslimiet** op je Anthropic-account en gebruik een **fine-grained GitHub-token** met alleen toegang tot de repo die je nodig hebt.

---

## Fundament

Dit project is gebouwd op de **Universele Rechten van de Vrije Mens**.  
Lees het volledige document: [aetherion-rechten.md](./docs/aetherion-rechten.md)

---

## Tech Stack

| Laag | Technologie |
|---|---|
| Frontend | HTML/CSS/JS (single file) |
| Mobile | Capacitor (Android WebView) |
| AI | Claude Sonnet 5.5 (Anthropic API) |
| Geheugen | GitHub + localStorage |
| Build | GitHub Actions |

---

## Licentie

Open source. Vrij te gebruiken voor doelen die in lijn zijn met de [Aetherion Rechten](./docs/aetherion-rechten.md).  
Misbruik is een schending van het fundament waarop dit gebouwd is.
