"""The Yamaha Receiver integration."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_HOST, Platform
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady

from .const import DOMAIN, CONF_ZONES, ZONE_MAIN
from .yamaha_api import YamahaRXV3900API

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [Platform.MEDIA_PLAYER]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Yamaha Receiver from a config entry."""
    host = entry.data[CONF_HOST]
    zones = entry.data.get(CONF_ZONES, [ZONE_MAIN])

    _LOGGER.debug("Setting up Yamaha Receiver at %s with zones %s", host, zones)

    # Create API instance
    api = YamahaRXV3900API(host)

    # Test connection
    try:
        status = await hass.async_add_executor_job(api.get_status, ZONE_MAIN)
        if status is None:
            raise ConfigEntryNotReady(f"Unable to connect to Yamaha Receiver at {host}")
    except Exception as err:
        _LOGGER.error("Error connecting to Yamaha Receiver at %s: %s", host, err)
        raise ConfigEntryNotReady(f"Unable to connect to Yamaha Receiver at {host}") from err

    # Store API instance
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = {
        "api": api,
        "zones": zones,
    }

    # Forward entry setup to platforms
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok


async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Reload config entry."""
    await async_unload_entry(hass, entry)
    await async_setup_entry(hass, entry)
