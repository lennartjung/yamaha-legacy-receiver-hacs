"""Config flow for Yamaha Receiver integration."""
from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_HOST
from homeassistant.core import HomeAssistant, callback
from homeassistant.data_entry_flow import FlowResult
from homeassistant.exceptions import HomeAssistantError
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN, CONF_ZONES, ZONES, ZONE_MAIN
from .yamaha_api import YamahaRXV3900API

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_HOST): str,
    }
)


async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, Any]:
    """Validate the user input allows us to connect."""
    api = YamahaRXV3900API(data[CONF_HOST])

    try:
        # Test connection
        status = await hass.async_add_executor_job(api.get_status, ZONE_MAIN)
        if status is None:
            raise CannotConnect
    except Exception as err:
        _LOGGER.error("Cannot connect to Yamaha receiver: %s", err)
        raise CannotConnect from err

    # Return info to be stored in config entry
    return {"title": f"Yamaha Receiver ({data[CONF_HOST]})"}


class YamahaConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Yamaha Receiver."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        errors: dict[str, str] = {}

        if user_input is not None:
            try:
                info = await validate_input(self.hass, user_input)
            except CannotConnect:
                errors["base"] = "cannot_connect"
            except Exception:  # pylint: disable=broad-except
                _LOGGER.exception("Unexpected exception")
                errors["base"] = "unknown"
            else:
                # Set unique ID to prevent duplicate entries
                await self.async_set_unique_id(user_input[CONF_HOST])
                self._abort_if_unique_id_configured()

                # Default: nur Main Zone
                user_input[CONF_ZONES] = [ZONE_MAIN]

                return self.async_create_entry(title=info["title"], data=user_input)

        return self.async_show_form(
            step_id="user", data_schema=STEP_USER_DATA_SCHEMA, errors=errors
        )

    @staticmethod
    @callback
    def async_get_options_flow(
        config_entry: config_entries.ConfigEntry,
    ) -> YamahaOptionsFlowHandler:
        """Get the options flow for this handler."""
        return YamahaOptionsFlowHandler(config_entry)


class YamahaOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle options flow for Yamaha Receiver."""

    def __init__(self, config_entry: config_entries.ConfigEntry) -> None:
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Manage the options."""
        if user_input is not None:
            # Update zones
            new_data = {**self.config_entry.data}
            new_data[CONF_ZONES] = user_input[CONF_ZONES]
            self.hass.config_entries.async_update_entry(
                self.config_entry, data=new_data
            )
            return self.async_create_entry(title="", data={})

        # Get current zones
        current_zones = self.config_entry.data.get(CONF_ZONES, [ZONE_MAIN])

        options_schema = vol.Schema(
            {
                vol.Required(
                    CONF_ZONES,
                    default=current_zones,
                ): cv.multi_select(ZONES),
            }
        )

        return self.async_show_form(step_id="init", data_schema=options_schema)


class CannotConnect(HomeAssistantError):
    """Error to indicate we cannot connect."""
