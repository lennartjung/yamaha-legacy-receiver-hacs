# Quick Start - GitHub veröffentlichen

## 📦 Was du hast

Eine vollständige, HACS-kompatible Home Assistant Integration für den Yamaha Legacy Receiver!

## 📁 Repository Struktur

```
yamaha-legacy-receiver-hacs/
├── .github/
│   └── workflows/
│       └── validate.yaml          # Automatische Tests
├── custom_components/
│   └── yamaha_legacy_receiver/
│       ├── __init__.py           # Integration Setup
│       ├── config_flow.py        # UI Konfiguration
│       ├── const.py              # Konstanten
│       ├── manifest.json         # Integration Metadata
│       ├── media_player.py       # Media Player Entity
│       ├── strings.json          # UI Texte
│       ├── yamaha_api.py         # API Client
│       └── translations/
│           ├── en.json           # Englisch
│           └── de.json           # Deutsch
├── .gitignore
├── CHANGELOG.md                  # Versionshistorie
├── hacs.json                     # HACS Konfiguration
├── info.md                       # HACS Store Info
├── LICENSE                       # MIT Lizenz
├── PUBLISHING.md                 # Ausführliche Anleitung
├── QUICK_START.md               # Diese Datei
└── README.md                     # Hauptdokumentation
```

## 🚀 In 5 Minuten veröffentlichen

### 1️⃣ Personalisieren (2 Min)

Ersetze in **allen Dateien** folgende Platzhalter:

- `lennartjung` → Dein GitHub Username
- `[YOUR NAME]` → Dein voller Name (für LICENSE)

**Betroffen:**
- `custom_components/yamaha_legacy_receiver/manifest.json`
- `README.md`
- `info.md`
- `LICENSE`
- `PUBLISHING.md`

**Schnellweg (Linux/Mac):**
```bash
# In yamaha-legacy-receiver-hacs/ Verzeichnis
find . -type f -name "*.md" -o -name "*.json" | xargs sed -i 's/lennartjung/dein-username/g'
find . -type f -name "*.md" -o -name "LICENSE" | xargs sed -i 's/\[YOUR NAME\]/Dein Name/g'
```

**Windows:**
Nutze Suchen & Ersetzen in deinem Editor (VS Code, Notepad++, etc.)

### 2️⃣ GitHub Repository erstellen (1 Min)

1. Gehe zu: https://github.com/new
2. Name: `yamaha-legacy-receiver-hacs`
3. Beschreibung: `Home Assistant integration for Yamaha Legacy Receiver AV Receiver`
4. **Public** (wichtig!)
5. ❌ Keine README/License/gitignore hinzufügen
6. Create Repository

### 3️⃣ Hochladen (2 Min)

```bash
cd yamaha-legacy-receiver-hacs

# Git initialisieren
git init
git add .
git commit -m "Initial commit - v1.0.0"

# Remote hinzufügen (USERNAME ersetzen!)
git remote add origin https://github.com/USERNAME/yamaha-legacy-receiver-hacs.git

# Hochladen
git branch -M main
git push -u origin main

# Release Tag erstellen
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0
```

### 4️⃣ GitHub Release erstellen (1 Min)

1. Auf GitHub: "Releases" → "Create a new release"
2. Tag: `v1.0.0`
3. Title: `v1.0.0 - Initial Release`
4. Description:
   ```markdown
   First release of Yamaha Legacy Receiver integration! 🎉
   
   Features: Power, Volume, Input, Surround modes, Multi-zone
   ```
5. Publish Release

### 5️⃣ In Home Assistant installieren (1 Min)

**Via HACS Custom Repository:**

1. HACS → Integrations → ⋮ → Custom repositories
2. URL: `https://github.com/USERNAME/yamaha-legacy-receiver-hacs`
3. Category: Integration
4. Add
5. Suche "Yamaha Legacy Receiver"
6. Install
7. Restart Home Assistant

**Direkte Installation:**

```bash
# Kopiere zu Home Assistant
cp -r custom_components/yamaha_legacy_receiver /config/custom_components/
```

## ✅ Fertig!

Deine Integration ist jetzt:
- ✅ Auf GitHub verfügbar
- ✅ Via HACS installierbar
- ✅ Bereit für die Community

## 🎯 Nächste Schritte (Optional)

### Offiziell in HACS listen

Folge: [PUBLISHING.md](PUBLISHING.md) → "Option A: HACS Default Repository"

Dauert 1-2 Wochen Review, aber danach ist es offiziell in HACS.

### Community informieren

1. **Home Assistant Forum:**
   https://community.home-assistant.io/c/third-party/9

2. **Reddit:**
   - r/homeassistant
   - r/homeautomation

3. **Social Media:**
   - Twitter/X mit #HomeAssistant
   - Mastodon

### README verbessern

- [ ] Screenshots hinzufügen
- [ ] GIF der Konfiguration
- [ ] Video-Tutorial (optional)

## 📝 Updates veröffentlichen

```bash
# 1. Änderungen machen
# 2. manifest.json Version erhöhen (z.B. 1.1.0)
# 3. CHANGELOG.md aktualisieren

git add .
git commit -m "feat: Added XYZ feature"
git push

# Neuen Release
git tag -a v1.1.0 -m "Release v1.1.0"
git push origin v1.1.0

# GitHub Release erstellen (wie oben)
```

## 🐛 Support

**Probleme?**
- [PUBLISHING.md](PUBLISHING.md) - Ausführliche Anleitung
- [Home Assistant Discord](https://discord.gg/home-assistant)
- [HACS Discord](https://discord.gg/apgchf8)

## 🎉 Glückwunsch!

Du hast deine erste Home Assistant Integration veröffentlicht! 🚀

**Share it:**
- Twitter/X: "Just published my first #HomeAssistant integration for Yamaha Legacy Receiver! 🎵"
- Reddit: "I made a Yamaha Legacy Receiver integration"
- Forum: "New integration: Yamaha Legacy Receiver"

---

**Viel Erfolg! Bei Fragen oder Problemen: Öffne ein Issue auf GitHub! 💬**
