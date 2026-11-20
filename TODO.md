# TODO - Yamaha Legacy Receiver Integration

## ✅ Erledigt
- [x] Integration erstellt
- [x] Auf GitHub veröffentlicht
- [x] Repository public gemacht
- [x] HACS Validierungsfehler behoben
- [x] Version 1.0.1 released
- [x] Platzhalter ersetzt (YOUR_USERNAME, etc.)
- [x] Unterstützte Modelle dokumentiert

## 🔄 In Arbeit
- [ ] Repository Description auf GitHub hinzufügen
  - Gehe zu: https://github.com/lennartjung/yamaha-legacy-receiver-hacs
  - Click ⚙️ neben "About"
  - Description: `Home Assistant integration for legacy Yamaha AV Receivers (2005-2009) using YNC XML protocol`
  - Topics: `home-assistant`, `homeassistant`, `hacs`, `yamaha`, `av-receiver`, `media-player`, `home-automation`, `custom-component`, `integration`

## 📝 TODO
- [ ] **Surround-Modi korrigieren** (wenn Receiver an ist)
  - Receiver einschalten
  - Modi am Display/WebUI notieren
  - Genaue Schreibweise prüfen (z.B. "7ch Enhancer" vs "7ch Enhanced")
  - `custom_components/yamaha_legacy_receiver/const.py` anpassen
  - SURROUND_PROGRAMS Liste aktualisieren

## 🎨 Optional (Nice to have)
- [ ] Custom Icon hinzufügen
  - Yamaha Logo als icon.png (256x256)
  - In `custom_components/yamaha_legacy_receiver/icons/` ablegen
  
- [ ] Screenshots für README
  - Setup-Dialog Screenshot
  - Media Player Entity Screenshot
  - Konfiguration GIF
  
- [ ] GitHub Release v1.0.1 erstellen
  - https://github.com/lennartjung/yamaha-legacy-receiver-hacs/releases/new
  - Tag: v1.0.1
  - Release notes schreiben

- [ ] Community informieren
  - Home Assistant Forum Post
  - Reddit r/homeassistant
  - Feedback sammeln

## 🧪 Testing
- [ ] Mit anderen Yamaha Modellen testen lassen
  - RX-V1900, RX-V2700, RX-Z11, etc.
  - User bitten, Feedback zu geben

## 📚 Dokumentation
- [ ] Wiki auf GitHub erstellen (optional)
  - Installation Guide
  - Troubleshooting
  - FAQ
  - API Documentation

---

## Schnelle Surround-Modi Anpassung (wenn Receiver an):

1. Receiver einschalten
2. Webinterface öffnen: http://192.168.1.168/
3. Surround-Menü öffnen
4. Alle verfügbaren Modi notieren
5. In Integration eintragen:
   ```bash
   cd yamaha-legacy-receiver-hacs
   nano custom_components/yamaha_legacy_receiver/const.py
   # SURROUND_PROGRAMS Liste anpassen
   git add -A
   git commit -m "Update surround modes list"
   git push
   ```

Oder: Modi hier auflisten, dann passe ich es an!
