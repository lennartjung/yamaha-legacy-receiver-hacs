# Yamaha Legacy Receiver Home Assistant Integration

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)
[![hacs][hacsbadge]][hacs]

![Project Maintenance][maintenance-shield]
[![Community Forum][forum-shield]][forum]

_Home Assistant integration for Yamaha Legacy Receiver AV Receiver using the XML Control Protocol._

## Features

- 🎵 **Full Media Player Integration** - Native Home Assistant media player entity
- 🔊 **Complete Control** - Power, volume, mute, input selection, surround modes
- 🏠 **Multi-Zone Support** - Control Main Zone, Zone 2, 3, and 4
- ⚡ **Local Control** - No cloud required, fast response times
- 🎨 **UI Configuration** - Easy setup through Home Assistant UI
- 🌍 **Multi-Language** - English and German translations included

## Installation

### HACS (Recommended)

1. Ensure [HACS](https://hacs.xyz/) is installed
2. In Home Assistant, go to HACS → Integrations
3. Click the three dots in the top right → Custom repositories
4. Add repository URL: `https://github.com/lennartjung/yamaha-legacy-receiver-hacs`
5. Category: Integration
6. Click "Add"
7. Search for "Yamaha Legacy Receiver" and click "Download"
8. Restart Home Assistant

### Manual Installation

1. Download the latest release from [releases page][releases]
2. Extract the archive
3. Copy `custom_components/yamaha_legacy_receiver` to your Home Assistant `custom_components` directory
4. Restart Home Assistant

## Configuration

### Add Integration

1. Go to **Settings** → **Devices & Services**
2. Click **+ Add Integration**
3. Search for **"Yamaha Legacy Receiver"**
4. Enter the **IP address** of your receiver
5. Click **Submit**

The integration will automatically create media player entities for your receiver.

### Configure Zones (Optional)

By default, only the Main Zone is enabled. To enable additional zones:

1. Go to **Settings** → **Devices & Services**
2. Find the Yamaha Legacy Receiver integration
3. Click **Configure**
4. Select additional zones (Zone 2, 3, 4)
5. Click **Submit**

## Usage

### Media Player Entities

The integration creates media player entities for each enabled zone:

- `media_player.yamaha_receiver_main_zone`
- `media_player.yamaha_receiver_zone_2`
- `media_player.yamaha_receiver_zone_3`
- `media_player.yamaha_receiver_zone_4`

### Available Features

✅ **Power Control**
```yaml
service: media_player.turn_on
target:
  entity_id: media_player.yamaha_receiver_main_zone
```

✅ **Volume Control**
```yaml
# Set absolute volume (0.0 - 1.0)
service: media_player.volume_set
target:
  entity_id: media_player.yamaha_receiver_main_zone
data:
  volume_level: 0.5

# Volume up/down
service: media_player.volume_up
target:
  entity_id: media_player.yamaha_receiver_main_zone
```

✅ **Mute**
```yaml
service: media_player.volume_mute
target:
  entity_id: media_player.yamaha_receiver_main_zone
data:
  is_volume_muted: true
```

✅ **Input Selection**
```yaml
service: media_player.select_source
target:
  entity_id: media_player.yamaha_receiver_main_zone
data:
  source: "HDMI1"
```

Available inputs: `HDMI1-6`, `AV1-7`, `AUDIO1-2`, `PHONO`, `TV`, `Tuner`, `V-AUX`, `MULTI_CH`, `iPod_USB`, `SIRIUS`, `XM`

✅ **Sound Mode Selection**
```yaml
service: media_player.select_sound_mode
target:
  entity_id: media_player.yamaha_receiver_main_zone
data:
  sound_mode: "7ch Enhancer"
```

Available modes: `Straight`, `7ch Enhancer`, `Hall in Vienna`, `2ch Stereo`, `Sports`, `Standard`, and more.

## Example Automations

### Movie Night Mode

```yaml
automation:
  - alias: "Movie Night"
    trigger:
      - platform: state
        entity_id: input_boolean.movie_mode
        to: 'on'
    action:
      - service: media_player.turn_on
        target:
          entity_id: media_player.yamaha_receiver_main_zone
      - delay:
          seconds: 2
      - service: media_player.select_source
        target:
          entity_id: media_player.yamaha_receiver_main_zone
        data:
          source: "HDMI1"
      - service: media_player.select_sound_mode
        target:
          entity_id: media_player.yamaha_receiver_main_zone
        data:
          sound_mode: "Standard"
      - service: media_player.volume_set
        target:
          entity_id: media_player.yamaha_receiver_main_zone
        data:
          volume_level: 0.6
```

### Good Morning Music

```yaml
automation:
  - alias: "Good Morning Music"
    trigger:
      - platform: time
        at: "07:00:00"
    condition:
      - condition: state
        entity_id: binary_sensor.workday
        state: 'on'
    action:
      - service: media_player.turn_on
        target:
          entity_id: media_player.yamaha_receiver_main_zone
      - delay:
          seconds: 2
      - service: media_player.select_source
        target:
          entity_id: media_player.yamaha_receiver_main_zone
        data:
          source: "iPod_USB"
      - service: media_player.volume_set
        target:
          entity_id: media_player.yamaha_receiver_main_zone
        data:
          volume_level: 0.3
```

### Voice Control with Alexa/Google Home

Since entities are standard Home Assistant media players, they work automatically with voice assistants:

- "Alexa, turn on Yamaha"
- "Hey Google, set Yamaha volume to 50%"
- "Alexa, switch Yamaha to HDMI1"

## Lovelace Dashboard Card

```yaml
type: media-control
entity: media_player.yamaha_receiver_main_zone
```

Or a more detailed card:

```yaml
type: vertical-stack
cards:
  - type: media-control
    entity: media_player.yamaha_receiver_main_zone
  - type: entities
    entities:
      - entity: media_player.yamaha_receiver_main_zone
        type: attribute
        attribute: source
        name: Current Input
      - entity: media_player.yamaha_receiver_main_zone
        type: attribute
        attribute: sound_mode
        name: Sound Mode
```

## Troubleshooting

### Cannot Connect to Receiver

**Symptoms:** Integration setup fails with "Cannot connect" error

**Solutions:**
1. Verify the receiver is powered on
2. Check the IP address is correct
3. Ensure receiver is on the same network as Home Assistant
4. Try accessing `http://YOUR_RECEIVER_IP/` in a browser
5. Check if receiver's network port is enabled

### Entity Shows "Unavailable"

**Symptoms:** Media player entity is unavailable

**Solutions:**
1. Check Home Assistant logs: Settings → System → Logs
2. Verify receiver is still at the same IP address
3. Restart the integration: Settings → Devices & Services → Yamaha Legacy Receiver → ⋮ → Reload
4. Power cycle the receiver

### Commands Not Working

**Symptoms:** Commands are sent but receiver doesn't respond

**Solutions:**
1. Check if commands work via the receiver's web interface
2. Ensure receiver firmware is up to date
3. Try power cycling the receiver
4. Check Home Assistant logs for API errors

### Volume Control Issues

**Symptoms:** Volume slider doesn't work as expected

**Note:** The receiver uses dB scale (-80.5 to +16.5 dB). For safety, the integration limits maximum volume to 0 dB (which is ~83% on the slider). This is normal behavior to prevent hearing damage.

## Technical Details

### Protocol

This integration uses the Yamaha Network Control (YNC) XML protocol via HTTP POST requests to `/YamahaRemoteControl/ctrl`.

### Polling Interval

The integration polls the receiver every 30 seconds to update the state. This is a reasonable interval that balances responsiveness with network load.

### Requirements

- Home Assistant 2024.1.0 or newer
- Yamaha Legacy Receiver with network connection
- Static IP address recommended

## Supported Models

### ✅ Tested and Confirmed Working

- **Yamaha Legacy Receiver** (2007)

### 🧪 Likely Compatible (Untested)

These models use the same YNC (Yamaha Network Control) XML protocol and should work without modifications:

**High-End Z-Series:**
- Yamaha RX-Z11 (2007) - Flagship, 11.2 channels
- Yamaha RX-Z9 (2005) - Previous flagship

**V-Series (Same Generation):**
- Yamaha RX-V3800 (2006)
- Yamaha RX-V2700 (2007)
- Yamaha RX-V2600 (2006)
- Yamaha RX-V1900 (2007)
- Yamaha RX-V1800 (2006)
- Yamaha RX-V1700 (2006)
- Yamaha RX-V2500 (2005)

**Why these models?** All these receivers from the 2005-2007 generation use the same web interface and XML control protocol. The API endpoints and command structure are identical.

### ❓ Your Model Not Listed?

If your Yamaha receiver has a web interface at `http://YOUR_IP/`, it might work! Try:

1. Open `http://YOUR_IP/YamahaRemoteControl/ctrl` in your browser
2. If you see an XML response, the protocol is supported
3. Install this integration and test
4. **Please report back!** Open an issue to let us know if it works

### ⚠️ Not Compatible

**MusicCast Receivers** (2015+) use a different API → Use the official [Yamaha MusicCast](https://www.home-assistant.io/integrations/yamaha_musiccast/) integration instead.

## Contributing

Contributions are welcome! Here's how you can help:

1. **Report Bugs** - Open an issue with details
2. **Feature Requests** - Suggest new features via issues
3. **Pull Requests** - Submit improvements or fixes
4. **Testing** - Test with different receiver models
5. **Documentation** - Improve docs and examples

### Development Setup

```bash
# Clone the repository
git clone https://github.com/lennartjung/yamaha-legacy-receiver-hacs.git
cd yamaha-legacy-receiver-hacs

# Copy to Home Assistant
cp -r custom_components/yamaha_legacy_receiver /path/to/homeassistant/custom_components/

# Restart Home Assistant
```

## FAQ

**Q: Does this work with Yamaha MusicCast receivers?**  
A: No, MusicCast receivers use a different API. Use the official Yamaha MusicCast integration instead.

**Q: Can I control the receiver without Home Assistant?**  
A: Yes, see the [API documentation](yamaha_receiver_api.md) for direct HTTP/XML control.

**Q: Does this require internet connection?**  
A: No, everything runs locally on your network.

**Q: Can I use this with Node-RED?**  
A: Yes, you can call the media player services from Node-RED.

**Q: Why isn't my receiver discovered automatically?**  
A: This integration requires manual setup with the IP address. SSDP discovery may be added in a future version.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits

- **Protocol Research** - Reverse engineered from Yamaha's web interface
- **Testing** - Thanks to all community testers
- **Home Assistant** - Built on the amazing Home Assistant platform

## Support

- 💬 [Community Forum][forum]
- 🐛 [Issue Tracker][issues]
- 📖 [Documentation](https://github.com/lennartjung/yamaha-legacy-receiver-hacs/wiki)

---

**Star this repository if you find it useful!** ⭐

---

[commits-shield]: https://img.shields.io/github/commit-activity/y/lennartjung/yamaha-legacy-receiver-hacs.svg?style=for-the-badge
[commits]: https://github.com/lennartjung/yamaha-legacy-receiver-hacs/commits/main
[hacs]: https://github.com/hacs/integration
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
[license-shield]: https://img.shields.io/github/license/lennartjung/yamaha-legacy-receiver-hacs.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-lennartjung-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/lennartjung/yamaha-legacy-receiver-hacs.svg?style=for-the-badge
[releases]: https://github.com/lennartjung/yamaha-legacy-receiver-hacs/releases
[issues]: https://github.com/lennartjung/yamaha-legacy-receiver-hacs/issues
