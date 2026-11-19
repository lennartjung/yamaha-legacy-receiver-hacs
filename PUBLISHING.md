# Publishing Guide

Schritt-für-Schritt Anleitung zur Veröffentlichung dieser Integration.

## Voraussetzungen

- [x] GitHub Account
- [x] Home Assistant Installation zum Testen
- [x] Git installiert

## Schritt 1: GitHub Repository erstellen

### 1.1 Neues Repository auf GitHub

1. Gehe zu https://github.com/new
2. Repository Name: `yamaha-legacy-receiver-hacs` (oder ähnlich)
3. Beschreibung: `Home Assistant integration for Yamaha Legacy Receiver AV Receiver`
4. **Public** Repository (wichtig für HACS!)
5. ❌ KEIN README, .gitignore oder LICENSE hinzufügen (haben wir schon)
6. Click "Create repository"

### 1.2 Lokales Repository initialisieren

```bash
cd yamaha-legacy-receiver-hacs

# Git initialisieren
git init

# Dateien hinzufügen
git add .

# Ersten Commit
git commit -m "Initial commit - Yamaha Legacy Receiver integration v1.0.0"

# Remote hinzufügen (ersetze lennartjung)
git remote add origin https://github.com/lennartjung/yamaha-legacy-receiver-hacs.git

# Branch umbenennen zu main
git branch -M main

# Push
git push -u origin main
```

## Schritt 2: Persönliche Informationen anpassen

Bevor du veröffentlichst, ersetze in folgenden Dateien:

### `manifest.json`
```json
"documentation": "https://github.com/lennartjung/yamaha-legacy-receiver-hacs",
"issue_tracker": "https://github.com/lennartjung/yamaha-legacy-receiver-hacs/issues",
"codeowners": ["@lennartjung"]
```

### `README.md`
Alle Vorkommnisse von:
- `lennartjung` → Dein GitHub Username
- `[YOUR NAME]` → Dein Name (in LICENSE)

### `info.md`
Alle Vorkommnisse von:
- `lennartjung` → Dein GitHub Username

## Schritt 3: Ersten Release erstellen

### 3.1 Tag erstellen

```bash
# Version 1.0.0 Release
git tag -a v1.0.0 -m "Release v1.0.0 - Initial release"
git push origin v1.0.0
```

### 3.2 GitHub Release erstellen

1. Gehe zu deinem Repository auf GitHub
2. Click "Releases" → "Create a new release"
3. Tag: `v1.0.0` (auswählen)
4. Release title: `v1.0.0 - Initial Release`
5. Beschreibung:

```markdown
# Yamaha Legacy Receiver Integration v1.0.0

First official release! 🎉

## Features

- ✅ Media Player integration
- ✅ Power control
- ✅ Volume control
- ✅ Input selection
- ✅ Surround mode selection
- ✅ Multi-zone support (Main, Zone 2-4)
- ✅ UI-based configuration

## Installation

Install via HACS:
1. Add custom repository: `https://github.com/lennartjung/yamaha-legacy-receiver-hacs`
2. Search for "Yamaha Legacy Receiver"
3. Install and restart Home Assistant

## Supported Devices

- Yamaha Legacy Receiver

## Documentation

See [README.md](https://github.com/lennartjung/yamaha-legacy-receiver-hacs) for full documentation.
```

6. Click "Publish release"

## Schritt 4: In HACS verfügbar machen

Es gibt zwei Wege:

### Option A: HACS Default Repository (Empfohlen)

Deine Integration wird offiziell in HACS gelistet.

1. Warte bis du einen Release erstellt hast (v1.0.0)
2. Gehe zu: https://github.com/hacs/default
3. Fork das Repository
4. Füge deine Integration hinzu in `custom_components/integration` als neue JSON-Datei:

`custom_components/yamaha_legacy_receiver/hacs.json`:
```json
{
  "name": "Yamaha Legacy Receiver",
  "content_in_root": false,
  "zip_release": false,
  "filename": "yamaha_legacy_receiver",
  "render_readme": true,
  "domains": ["media_player"]
}
```

5. Erstelle Pull Request
6. Warte auf Approval (kann 1-2 Wochen dauern)

### Option B: Custom Repository (Sofort nutzbar)

User können deine Integration als Custom Repository hinzufügen:

1. In Home Assistant → HACS → Integrations
2. Three dots (oben rechts) → Custom repositories
3. Repository URL: `https://github.com/lennartjung/yamaha-legacy-receiver-hacs`
4. Category: Integration
5. Click "Add"

**Vorteile Option B:**
- Sofort verfügbar
- Keine Genehmigung nötig

**Vorteile Option A:**
- Offiziell in HACS
- Mehr Sichtbarkeit
- Automatische Updates für alle User

## Schritt 5: Testen

### Lokale Installation testen

1. Kopiere `custom_components/yamaha_legacy_receiver` nach:
   ```
   /config/custom_components/yamaha_legacy_receiver
   ```

2. Restart Home Assistant

3. Füge Integration hinzu:
   - Settings → Devices & Services → Add Integration
   - Suche "Yamaha Legacy Receiver"
   - Teste alle Funktionen

### HACS Installation testen (Option B)

1. Füge als Custom Repository hinzu (siehe oben)
2. Installiere über HACS
3. Restart Home Assistant
4. Teste Integration

## Schritt 6: Dokumentation vervollständigen

### README.md
- [ ] Screenshots hinzufügen
- [ ] GIFs von der Konfiguration
- [ ] Mehr Beispiele

### Wiki erstellen (Optional)
1. Auf GitHub: Settings → Features → Wikis aktivieren
2. Erstelle Wiki-Seiten:
   - Installation Guide
   - Configuration
   - Troubleshooting
   - API Reference

## Schritt 7: Community bekannt machen

### Home Assistant Community Forum

1. Gehe zu: https://community.home-assistant.io/c/third-party/9
2. Erstelle neuen Thread:

**Title:** `Yamaha Legacy Receiver Custom Integration`

**Post:**
```markdown
Hi everyone! 👋

I've created a custom integration for the Yamaha Legacy Receiver AV Receiver.

## Features
- Full media player control
- Power, volume, input, surround modes
- Multi-zone support
- Local control (no cloud)

## Installation
Via HACS custom repository:
https://github.com/lennartjung/yamaha-legacy-receiver-hacs

## Feedback Welcome
This is my first integration, feedback welcome!

GitHub: https://github.com/lennartjung/yamaha-legacy-receiver-hacs
```

### Reddit

Post in:
- r/homeassistant
- r/homeautomation

### Social Media

- Twitter/X mit #HomeAssistant
- Mastodon HomeAssistant Community

## Maintenance

### Updates veröffentlichen

1. Änderungen machen
2. Version in `manifest.json` erhöhen
3. `CHANGELOG.md` aktualisieren
4. Commit und Push
5. Neuen Tag erstellen:
   ```bash
   git tag -a v1.1.0 -m "Release v1.1.0"
   git push origin v1.1.0
   ```
6. GitHub Release erstellen

### Issues bearbeiten

- Antworte auf Issues zeitnah
- Label nutzen: `bug`, `enhancement`, `question`
- Pull Requests willkommen heißen

### HACS Validation

HACS hat automatische Checks. Stelle sicher:
- [x] `manifest.json` ist valide
- [x] `hacs.json` existiert
- [x] GitHub Releases existieren
- [x] README.md vorhanden
- [x] LICENSE vorhanden

## Checkliste vor Veröffentlichung

- [ ] Alle `lennartjung` ersetzt
- [ ] Alle `[YOUR NAME]` ersetzt
- [ ] Git Repository initialisiert
- [ ] Auf GitHub gepusht
- [ ] Ersten Release (v1.0.0) erstellt
- [ ] Integration lokal getestet
- [ ] README.md vollständig
- [ ] Screenshots/GIFs hinzugefügt (optional)
- [ ] CHANGELOG.md aktualisiert
- [ ] HACS Option gewählt (A oder B)
- [ ] Community informiert

## Hilfe & Support

### Bei Fragen:
- HACS Discord: https://discord.gg/apgchf8
- Home Assistant Community: https://community.home-assistant.io/
- Home Assistant Discord: https://discord.gg/home-assistant

### Nützliche Links:
- HACS Dokumentation: https://hacs.xyz/docs/publish/start
- HA Integration Development: https://developers.home-assistant.io/
- HA Integration Quality Scale: https://www.home-assistant.io/docs/quality_scale/

---

**Viel Erfolg mit deiner Integration! 🎉**
