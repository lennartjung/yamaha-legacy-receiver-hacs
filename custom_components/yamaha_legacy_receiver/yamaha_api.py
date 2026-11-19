"""Yamaha Receiver API."""
from __future__ import annotations

import logging
from typing import Any
import xml.etree.ElementTree as ET

import requests

from .const import API_ENDPOINT, API_TIMEOUT

_LOGGER = logging.getLogger(__name__)


class YamahaRXV3900API:
    """Yamaha Receiver API client."""

    def __init__(self, host: str) -> None:
        """Initialize the API."""
        self.host = host
        self.url = f"http://{host}{API_ENDPOINT}"
        self.headers = {"Content-Type": "text/xml"}

    def _send_command(self, xml_command: str) -> ET.Element | None:
        """Send XML command to receiver."""
        try:
            response = requests.post(
                self.url,
                headers=self.headers,
                data=xml_command.encode("utf-8"),
                timeout=API_TIMEOUT,
            )
            response.raise_for_status()
            return ET.fromstring(response.text)
        except requests.exceptions.RequestException as err:
            _LOGGER.error("Request error: %s", err)
            return None
        except ET.ParseError as err:
            _LOGGER.error("XML parse error: %s", err)
            return None

    def get_status(self, zone: str = "Main_Zone") -> dict[str, Any] | None:
        """Get current status of zone."""
        xml = f"""<?xml version="1.0" encoding="utf-8"?>
<YAMAHA_AV cmd="GET">
  <{zone}>
    <Basic_Status>GetParam</Basic_Status>
  </{zone}>
</YAMAHA_AV>"""

        response = self._send_command(xml)
        if response is None:
            return None

        try:
            status = {}
            zone_elem = response.find(zone)
            if zone_elem is None:
                return None

            basic_status = zone_elem.find("Basic_Status")
            if basic_status is None:
                return None

            # Power
            power = basic_status.find("Power_Control/Power")
            if power is not None:
                status["power"] = power.text

            # Volume
            vol_val = basic_status.find("Vol/Lvl/Val")
            vol_exp = basic_status.find("Vol/Lvl/Exp")
            if vol_val is not None and vol_exp is not None:
                val = int(vol_val.text)
                exp = int(vol_exp.text)
                status["volume_raw"] = val
                status["volume_db"] = val / (10**exp)

            # Mute
            mute = basic_status.find("Vol/Mute")
            if mute is not None:
                status["mute"] = mute.text

            # Input
            input_sel = basic_status.find("Input/Input_Sel")
            if input_sel is not None:
                status["input"] = input_sel.text

            # Surround
            pgm = basic_status.find("Surr/Pgm_Sel/Pgm")
            straight = basic_status.find("Surr/Pgm_Sel/Straight")
            if straight is not None and straight.text == "On":
                status["surround"] = "Straight"
            elif pgm is not None:
                status["surround"] = pgm.text

            # Sleep
            sleep = basic_status.find("Power_Control/Sleep")
            if sleep is not None:
                status["sleep"] = sleep.text

            return status
        except Exception as err:
            _LOGGER.error("Error parsing status: %s", err)
            return None

    def power_on(self, zone: str = "Main_Zone") -> bool:
        """Turn on zone."""
        xml = f"""<?xml version="1.0" encoding="utf-8"?>
<YAMAHA_AV cmd="PUT">
  <{zone}>
    <Power_Control>
      <Power>On</Power>
    </Power_Control>
  </{zone}>
</YAMAHA_AV>"""
        return self._send_command(xml) is not None

    def power_off(self, zone: str = "Main_Zone") -> bool:
        """Turn off zone."""
        xml = f"""<?xml version="1.0" encoding="utf-8"?>
<YAMAHA_AV cmd="PUT">
  <{zone}>
    <Power_Control>
      <Power>Standby</Power>
    </Power_Control>
  </{zone}>
</YAMAHA_AV>"""
        return self._send_command(xml) is not None

    def set_volume(self, volume_db: float, zone: str = "Main_Zone") -> bool:
        """Set volume in dB."""
        val = int(volume_db * 10)
        xml = f"""<?xml version="1.0" encoding="utf-8"?>
<YAMAHA_AV cmd="PUT">
  <{zone}>
    <Vol>
      <Lvl>
        <Val>{val}</Val>
        <Exp>1</Exp>
        <Unit>dB</Unit>
      </Lvl>
    </Vol>
  </{zone}>
</YAMAHA_AV>"""
        return self._send_command(xml) is not None

    def volume_up(self, zone: str = "Main_Zone") -> bool:
        """Increase volume."""
        xml = f"""<?xml version="1.0" encoding="utf-8"?>
<YAMAHA_AV cmd="PUT">
  <{zone}>
    <Vol>
      <Lvl>Up</Lvl>
    </Vol>
  </{zone}>
</YAMAHA_AV>"""
        return self._send_command(xml) is not None

    def volume_down(self, zone: str = "Main_Zone") -> bool:
        """Decrease volume."""
        xml = f"""<?xml version="1.0" encoding="utf-8"?>
<YAMAHA_AV cmd="PUT">
  <{zone}>
    <Vol>
      <Lvl>Down</Lvl>
    </Vol>
  </{zone}>
</YAMAHA_AV>"""
        return self._send_command(xml) is not None

    def mute(self, mute: bool, zone: str = "Main_Zone") -> bool:
        """Mute or unmute."""
        mute_value = "On" if mute else "Off"
        xml = f"""<?xml version="1.0" encoding="utf-8"?>
<YAMAHA_AV cmd="PUT">
  <{zone}>
    <Vol>
      <Mute>{mute_value}</Mute>
    </Vol>
  </{zone}>
</YAMAHA_AV>"""
        return self._send_command(xml) is not None

    def set_input(self, input_name: str, zone: str = "Main_Zone") -> bool:
        """Set input source."""
        xml = f"""<?xml version="1.0" encoding="utf-8"?>
<YAMAHA_AV cmd="PUT">
  <{zone}>
    <Input>
      <Input_Sel>{input_name}</Input_Sel>
    </Input>
  </{zone}>
</YAMAHA_AV>"""
        return self._send_command(xml) is not None

    def set_surround_straight(self, zone: str = "Main_Zone") -> bool:
        """Set straight mode."""
        xml = f"""<?xml version="1.0" encoding="utf-8"?>
<YAMAHA_AV cmd="PUT">
  <{zone}>
    <Surr>
      <Pgm_Sel>
        <Straight>On</Straight>
      </Pgm_Sel>
    </Surr>
  </{zone}>
</YAMAHA_AV>"""
        return self._send_command(xml) is not None

    def set_surround_program(self, program: str, zone: str = "Main_Zone") -> bool:
        """Set surround program."""
        xml = f"""<?xml version="1.0" encoding="utf-8"?>
<YAMAHA_AV cmd="PUT">
  <{zone}>
    <Surr>
      <Pgm_Sel>
        <Straight>Off</Straight>
        <Pgm>{program}</Pgm>
      </Pgm_Sel>
    </Surr>
  </{zone}>
</YAMAHA_AV>"""
        return self._send_command(xml) is not None
