# Yamaha Legacy Receiver Integration

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

![Project Maintenance][maintenance-shield]

Home Assistant integration for legacy Yamaha AV Receivers (2005-2009) using the YNC XML protocol.

## Features

✅ **Full Control**
- Power on/off
- Volume control
- Mute
- Input selection
- Surround/DSP mode selection

✅ **Multi-Zone Support**
- Main Zone
- Zone 2, 3, 4 support

✅ **Easy Setup**
- UI-based configuration
- Auto-discovery of receiver
- No YAML required

✅ **Local Control**
- No cloud required
- Fast response times
- Works offline

## Installation

### HACS (Recommended)

1. Open HACS in Home Assistant
2. Click on "Integrations"
3. Click the three dots in the top right corner
4. Select "Custom repositories"
5. Add this repository URL: `https://github.com/YOUR_USERNAME/yamaha-legacy-receiver-hacs`
6. Select category: "Integration"
7. Click "Add"
8. Find "Yamaha Legacy Receiver" in HACS and install it
9. Restart Home Assistant

### Manual Installation

1. Copy `custom_components/yamaha_legacy_receiver` to your `custom_components` folder
2. Restart Home Assistant

## Configuration

1. Go to **Settings** → **Devices & Services**
2. Click **+ Add Integration**
3. Search for "Yamaha Legacy Receiver"
4. Enter the IP address of your receiver
5. Click Submit

### Configure Zones (Optional)

1. Go to the integration in **Devices & Services**
2. Click **Configure**
3. Select which zones you want to control
4. Click Submit

## Usage

The integration creates a **Media Player** entity for each zone:

- `media_player.yamaha_receiver_main_zone`
- `media_player.yamaha_receiver_zone_2` (if enabled)

### Services

All standard media player services are supported:

- `media_player.turn_on`
- `media_player.turn_off`
- `media_player.volume_set`
- `media_player.volume_up`
- `media_player.volume_down`
- `media_player.volume_mute`
- `media_player.select_source` (change input)
- `media_player.select_sound_mode` (change surround mode)

### Example Automation

```yaml
automation:
  - alias: "Movie Mode"
    trigger:
      - platform: state
        entity_id: input_boolean.movie_mode
        to: 'on'
    action:
      - service: media_player.turn_on
        target:
          entity_id: media_player.yamaha_receiver_main_zone
      - delay: 2
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
```

## Supported Models

### ✅ Tested & Confirmed
- **Yamaha RX-V3900**

### 🧪 Untested but Compatible
Legacy Yamaha receivers (2005-2009) using YNC XML protocol:
- RX-Z11, RX-Z9 (Flagship series)
- RX-V3800, RX-V2700, RX-V2600, RX-V1900, RX-V1800, RX-V1700, RX-V2500

**Note:** MusicCast receivers (2015+) are NOT compatible → use the official Yamaha MusicCast integration.

## Troubleshooting

### Cannot Connect

- Ensure the receiver is powered on
- Check that the IP address is correct
- Verify the receiver is on the same network
- Try accessing `http://YOUR_IP/` in a browser

### Entity Not Updating

- Check Home Assistant logs for errors
- The integration polls every 30 seconds by default
- Restart the integration if needed

## Support

- [Report a Bug][issues]
- [Request a Feature][issues]

## Credits

This integration was created using the Yamaha Network Control (YNC) XML protocol.

---

[commits-shield]: https://img.shields.io/github/commit-activity/y/YOUR_USERNAME/yamaha-legacy-receiver-hacs.svg?style=for-the-badge
[commits]: https://github.com/YOUR_USERNAME/yamaha-legacy-receiver-hacs/commits/main
[license-shield]: https://img.shields.io/github/license/YOUR_USERNAME/yamaha-legacy-receiver-hacs.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-YOUR_USERNAME-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/YOUR_USERNAME/yamaha-legacy-receiver-hacs.svg?style=for-the-badge
[releases]: https://github.com/YOUR_USERNAME/yamaha-legacy-receiver-hacs/releases
[issues]: https://github.com/YOUR_USERNAME/yamaha-legacy-receiver-hacs/issues
