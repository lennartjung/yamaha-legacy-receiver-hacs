"""Media Player platform for Yamaha Receiver."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.components.media_player import (
    MediaPlayerDeviceClass,
    MediaPlayerEntity,
    MediaPlayerEntityFeature,
    MediaPlayerState,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_HOST
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import (
    DOMAIN,
    CONF_ZONES,
    ZONES,
    INPUTS_COMMON,
    SURROUND_PROGRAMS,
    MIN_VOLUME,
    MAX_VOLUME,
)
from .yamaha_api import YamahaRXV3900API

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Yamaha Receiver media player from config entry."""
    api: YamahaRXV3900API = hass.data[DOMAIN][config_entry.entry_id]["api"]
    zones: list[str] = hass.data[DOMAIN][config_entry.entry_id]["zones"]
    host = config_entry.data[CONF_HOST]

    entities = []
    for zone in zones:
        zone_name = ZONES.get(zone, zone)
        entities.append(YamahaMediaPlayer(api, zone, zone_name, host))

    async_add_entities(entities)


class YamahaMediaPlayer(MediaPlayerEntity):
    """Representation of a Yamaha Receiver Media Player."""

    _attr_device_class = MediaPlayerDeviceClass.RECEIVER
    _attr_supported_features = (
        MediaPlayerEntityFeature.VOLUME_SET
        | MediaPlayerEntityFeature.VOLUME_STEP
        | MediaPlayerEntityFeature.VOLUME_MUTE
        | MediaPlayerEntityFeature.TURN_ON
        | MediaPlayerEntityFeature.TURN_OFF
        | MediaPlayerEntityFeature.SELECT_SOURCE
        | MediaPlayerEntityFeature.SELECT_SOUND_MODE
    )

    def __init__(
        self, api: YamahaRXV3900API, zone: str, zone_name: str, host: str
    ) -> None:
        """Initialize the media player."""
        self._api = api
        self._zone = zone
        self._zone_name = zone_name
        self._host = host

        # State
        self._attr_state = MediaPlayerState.OFF
        self._attr_volume_level = 0.0
        self._attr_is_volume_muted = False
        self._attr_source = None
        self._attr_sound_mode = None

        # Device info
        self._attr_name = f"Yamaha Receiver {zone_name}"
        self._attr_unique_id = f"yamaha_rxv3900_{host}_{zone}"

        # Sources
        self._attr_source_list = INPUTS_COMMON
        self._attr_sound_mode_list = SURROUND_PROGRAMS

    @property
    def device_info(self):
        """Return device info."""
        return {
            "identifiers": {(DOMAIN, self._host)},
            "name": "Yamaha Receiver",
            "manufacturer": "Yamaha",
            "model": "RX-V3900",
        }

    async def async_update(self) -> None:
        """Fetch new state data for this media player."""
        status = await self.hass.async_add_executor_job(
            self._api.get_status, self._zone
        )

        if status is None:
            self._attr_available = False
            return

        self._attr_available = True

        # Power state
        power = status.get("power")
        if power == "On":
            self._attr_state = MediaPlayerState.ON
        elif power in ("Standby", "Off"):
            self._attr_state = MediaPlayerState.OFF
        else:
            self._attr_state = MediaPlayerState.OFF

        # Volume (convert dB to 0.0-1.0 range)
        # Yamaha: -80.5 dB to +16.5 dB
        # We map -80.5 to 0.0 and 0.0 dB to ~0.83 (safe max)
        volume_db = status.get("volume_db", MIN_VOLUME)
        # Map -80.5...0 dB to 0.0...1.0 (limit to 0 dB as max for safety)
        self._attr_volume_level = max(0.0, min(1.0, (volume_db - MIN_VOLUME) / (0 - MIN_VOLUME)))

        # Mute
        mute = status.get("mute")
        self._attr_is_volume_muted = mute == "On"

        # Source
        self._attr_source = status.get("input")

        # Sound mode
        self._attr_sound_mode = status.get("surround")

    async def async_turn_on(self) -> None:
        """Turn the media player on."""
        await self.hass.async_add_executor_job(self._api.power_on, self._zone)

    async def async_turn_off(self) -> None:
        """Turn the media player off."""
        await self.hass.async_add_executor_job(self._api.power_off, self._zone)

    async def async_set_volume_level(self, volume: float) -> None:
        """Set volume level (0.0 to 1.0)."""
        # Convert 0.0-1.0 to dB (-80.5 to 0.0)
        # We limit max to 0 dB for safety
        volume_db = MIN_VOLUME + (volume * (0 - MIN_VOLUME))
        volume_db = max(MIN_VOLUME, min(0, volume_db))
        await self.hass.async_add_executor_job(
            self._api.set_volume, volume_db, self._zone
        )

    async def async_volume_up(self) -> None:
        """Volume up."""
        await self.hass.async_add_executor_job(self._api.volume_up, self._zone)

    async def async_volume_down(self) -> None:
        """Volume down."""
        await self.hass.async_add_executor_job(self._api.volume_down, self._zone)

    async def async_mute_volume(self, mute: bool) -> None:
        """Mute or unmute."""
        await self.hass.async_add_executor_job(self._api.mute, mute, self._zone)

    async def async_select_source(self, source: str) -> None:
        """Select input source."""
        await self.hass.async_add_executor_job(self._api.set_input, source, self._zone)

    async def async_select_sound_mode(self, sound_mode: str) -> None:
        """Select sound mode."""
        if sound_mode == "Straight":
            await self.hass.async_add_executor_job(
                self._api.set_surround_straight, self._zone
            )
        else:
            await self.hass.async_add_executor_job(
                self._api.set_surround_program, sound_mode, self._zone
            )
