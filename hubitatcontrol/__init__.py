"""Hubitat Maker API"""

from hubitatcontrol.hub import Hub
from hubitatcontrol.lights import *
from hubitatcontrol.generic import *

def get_hub(host, token, app_id) -> Hub:
    return Hub(host=host, token=token, app_id=app_id)


def lookup_device(hub_in, device_lookup):
    d = hub_in.get_device(device_lookup)
    if d['type'] == 'Advanced Zigbee RGBW Bulb':
        return Advanced_Zigbee_RGBW_Bulb(device_from_hub=d, hub=hub_in)
    if d['type'] == 'Generic Zigbee Outlet':
        return ZigbeeOutlet(device_from_hub=d, hub=hub_in)
