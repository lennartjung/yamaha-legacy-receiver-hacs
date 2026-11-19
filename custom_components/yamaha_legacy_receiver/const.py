"""Constants for the Yamaha Legacy Receiver integration."""

DOMAIN = "yamaha_legacy_receiver"

# Default values
DEFAULT_NAME = "Yamaha Receiver"
DEFAULT_PORT = 80
DEFAULT_TIMEOUT = 5

# Configuration
CONF_ZONES = "zones"

# Available zones
ZONE_MAIN = "Main_Zone"
ZONE_2 = "Zone_2"
ZONE_3 = "Zone_3"
ZONE_4 = "Zone_4"

ZONES = {
    ZONE_MAIN: "Main Zone",
    ZONE_2: "Zone 2",
    ZONE_3: "Zone 3",
    ZONE_4: "Zone 4",
}

# Yamaha API
API_ENDPOINT = "/YamahaRemoteControl/ctrl"
API_TIMEOUT = 5

# Inputs - häufig verwendete Eingänge
INPUTS_COMMON = [
    "HDMI1", "HDMI2", "HDMI3", "HDMI4", "HDMI5", "HDMI6",
    "AV1", "AV2", "AV3", "AV4", "AV5", "AV6", "AV7",
    "AUDIO1", "AUDIO2",
    "PHONO",
    "TV",
    "Tuner",
    "V-AUX",
    "MULTI_CH",
    "iPod_USB",
    "SIRIUS",
    "XM",
]

# Surround programs
SURROUND_PROGRAMS = [
    "Straight",
    "7ch Enhancer",
    "Hall in Munich",
    "Hall in Vienna",
    "Church in Freiburg",
    "Chamber",
    "Cellar Club",
    "The Roxy Theatre",
    "The Bottom Line",
    "Sports",
    "Action Game",
    "Roleplaying Game",
    "Music Video",
    "Standard",
    "Spectacle",
    "Sci-Fi",
    "Adventure",
    "Drama",
    "Mono Movie",
    "2ch Stereo",
    "5ch Stereo",
    "7ch Stereo",
]

# Volume
MIN_VOLUME = -80.5
MAX_VOLUME = 16.5
VOLUME_STEP = 0.5
