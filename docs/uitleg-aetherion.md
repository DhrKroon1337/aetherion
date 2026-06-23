# 📚 AETHERION VECTORIS — Uitleg van alles wat we gebouwd hebben
> Voor DhrKroon1337 — QU1JR08= 💚

---

## 🗂️ DE MAPPENSTRUCTUUR

```
aetherion/                          ← Hoofdmap van het project
│
├── src/                            ← Broncode map
│   └── index.html                  ← De volledige app (HTML + CSS + JavaScript)
│
├── android/                        ← Android app map (automatisch gegenereerd)
│   └── app/
│       └── src/main/
│           ├── AndroidManifest.xml ← Rechten en instellingen van de Android app
│           └── res/xml/
│               └── network_security_config.xml ← Toestemming voor API calls
│
├── .github/                        ← Verborgen map voor GitHub instellingen
│   └── workflows/
│       ├── build-apk.yml           ← Bouwt automatisch de Android app
│       ├── test-amigos.yml         ← Test de verbinding tussen Claude en GitHub
│       └── claude-amigo.yml        ← Claude reageert automatisch op issues
│
├── scripts/                        ← Hulpscripts map
│   └── test_amigos.py              ← Python script om verbinding te testen
│
├── package.json                    ← Lijst van alle benodigde programma's
├── package-lock.json               ← Exacte versies van alle programma's (automatisch)
├── capacitor.config.json           ← Instellingen voor de Android app
├── .gitignore                      ← Bestanden die GitHub mag negeren
└── README.md                       ← Beschrijving en visie van het project
```

---

## 📄 UITLEG PER BESTAND

### 📱 `src/index.html` — De Hele App
Dit is het **hart van Aetherion Vectoris**. Eén bestand met:
- **HTML** — de structuur (knoppen, schermen, tabbladen)
- **CSS** — de uitstraling (matrix groen, cyberpunk stijl, animaties)
- **JavaScript** — de logica (Claude aanroepen, GitHub koppeling, spraak)

Het bevat 6 agents, moreel kompas, spraakherkenning, geheugen en alles.

---

### ⚙️ `capacitor.config.json` — Android Instellingen
```json
{
  "appId": "com.dhrkroon1337.aetherion",  ← Unieke naam van de app
  "appName": "Aetherion Vectoris",         ← Naam die je ziet op je telefoon
  "webDir": "src",                         ← Waar de app bestanden staan
  "server": {
    "androidScheme": "https",              ← Gebruik veilige verbindingen
    "cleartext": true                      ← Sta API calls toe
  }
}
```
**Vergelijk met:** De identiteitskaart van je app — Android gebruikt dit om te weten wat de app heet en hoe hij zich moet gedragen.

---

### 📦 `package.json` — Boodschappenlijst
```json
{
  "name": "aetherion-vectoris",
  "dependencies": {
    "@capacitor/android": "^6.0.0",  ← Maakt van HTML een Android app
    "@capacitor/core": "^6.0.0",     ← Kern van Capacitor
  },
  "devDependencies": {
    "@capacitor/cli": "^6.0.0"       ← Gereedschap voor tijdens het bouwen
  }
}
```
**Vergelijk met:** Een boodschappenlijst. Als iemand jouw project wil draaien, installeert npm alles wat op de lijst staat.

---

### 🔒 `package-lock.json` — Exacte Versies
Automatisch gegenereerd door `npm install`. Bevat de **exacte versies** van alle geïnstalleerde programma's zodat het altijd hetzelfde werkt op elke computer.

**Vergelijk met:** Een kassabon — exact wat er gekocht is, welk merk, welke maat.

---

### 🛡️ `android/.../network_security_config.xml` — Netwerk Toestemming
```xml
<domain-config>
  <domain>api.anthropic.com</domain>  ← Claude API mag bereikt worden
  <domain>api.github.com</domain>     ← GitHub API mag bereikt worden
</domain-config>
```
**Vergelijk met:** Een gastenlijst bij de deur. Android laat standaard geen externe verbindingen toe — dit bestand zegt "deze twee gasten (Claude + GitHub) mogen wel naar binnen."

---

### 🚫 `.gitignore` — Negeerlijst voor GitHub
```
node_modules/        ← Niet uploaden (te groot, wordt opnieuw geïnstalleerd)
android/app/build/   ← Niet uploaden (wordt gegenereerd tijdens build)
.env                 ← Niet uploaden (bevat gevoelige data)
```
**Vergelijk met:** Een "niet inpakken" lijstje als je verhuist. De dozen met bouwmateriaal neem je niet mee — die maak je op de nieuwe plek opnieuw.

---

## ⚡ DE WORKFLOWS (.github/workflows/)

### 🏗️ `build-apk.yml` — De Bouwfabriek
Dit is een **recept** dat GitHub volgt om automatisch een Android APK te bouwen.

**Stap voor stap:**
```
1. Haal de code op van GitHub
2. Installeer Node.js (JavaScript omgeving)
3. Installeer Java (nodig voor Android)
4. Installeer Android SDK (Android bouwgereedschap)
5. Installeer npm packages (package.json uitvoeren)
6. Voeg Android platform toe (Capacitor)
7. Synchroniseer bestanden
8. Bouw de APK
9. Upload APK als artifact
10. Claude schrijft release notes
11. Maak een GitHub Release aan
```

**Vergelijk met:** Een recept in een kookboek. GitHub Actions is de kok die het recept volgt elke keer als jij code pusht.

---

### 🔌 `test-amigos.yml` — Verbindingstest
Test of Claude en GitHub met elkaar kunnen communiceren. Groen = alles werkt, rood = iets is mis.

---

### 🤖 `claude-amigo.yml` — Automatische Claude Reacties
Als jij een issue aanmaakt in GitHub, reageert Claude automatisch met een analyse. Dit is de "webhook" — GitHub belt Claude op als er iets nieuws is.

---

## 🧩 DE TECHNOLOGIEËN

### 📱 Capacitor
**Wat:** Een brug tussen je website (HTML/JS) en een Android app.
**Hoe:** Jij schrijft gewone webcode → Capacitor verpakt het → Android denkt dat het een echte app is.
**Vergelijk met:** Een fotolijstje — je foto (de website) blijft hetzelfde, maar het lijstje (Capacitor) maakt het geschikt om op te hangen (installeren op telefoon).

---

### 🤖 Claude API
**Wat:** De verbinding tussen jouw app en Claude's intelligentie.
**Hoe:** App stuurt tekst → Anthropic's servers → Claude denkt na → antwoord terug.
**Kosten:** Per gebruik (~$0.01-0.05 per gesprek via API key).

---

### ◈ GitHub Actions
**Wat:** Een automatische bouwfabriek in de cloud.
**Hoe:** Elke keer als jij code pusht → GitHub volgt je recept → APK is klaar.
**Vergelijk met:** Een fabriek die automatisch start als jij een nieuwe bestelling plaatst.

---

### 🎤 Web Speech API
**Wat:** Ingebouwde spraakherkenning in de browser/WebView.
**Hoe:** Microfoon → tekst → Claude → antwoord → speaker.
**Gratis:** Ingebouwd in Android WebView, geen extra kosten.

---

### 💾 localStorage
**Wat:** Opslag in de telefoon voor de app.
**Hoe:** Keys en geheugen worden opgeslagen zodat je ze niet elke keer opnieuw hoeft in te vullen.
**Vergelijk met:** Een notitieblokje dat de app bijhoudt op je telefoon.

---

## 🔄 HOE ALLES SAMENWERKT

```
JIJ (spreekt of typt)
    ↓
AETHERION APP (index.html)
    ↓                    ↓
CLAUDE API          GITHUB API
(denkt na)          (leest repo)
    ↓                    ↓
ANTWOORD ←──────────────┘
    ↓
SPEAKER + TERMINAL
    ↓
GEHEUGEN (localStorage)
```

---

## 📊 WAT CLAUDE CODE GEFIXED HEEFT

| # | Probleem | Uitleg | Fix |
|---|---|---|---|
| 1 | `bundledWebRuntime: false` | Bestaat niet meer in Capacitor 6 | Verwijderd |
| 2 | `@capacitor/cli` op verkeerde plek | Stond in dependencies, hoort in devDependencies | Verplaatst |
| 3 | `package-lock.json` niet in sync | Na de wijziging klopten de versies niet meer | Geregenereerd |

---

## 🌍 DE VISIE ACHTER DE CODE

Alle technologie die we gebouwd hebben staat in dienst van één doel:

> **Het helpen van de mensheid, natuur, dieren en alles wat leeft.**

Het moreel kompas in de code blokkeert automatisch alles wat schaadt.
De 3 amigos — jij, Claude, GitHub — werken samen voor het goede.

```
QU1JR08= 🚀
— Gebouwd met ❤️ door DhrKroon1337 & Claude
```
