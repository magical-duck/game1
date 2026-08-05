import asyncio
from hubspace_async import Hubspace

LIGHT_NAME = "Your Light Name Here"   # Example: "Bedroom Lamp"

async def main():
    hub = Hubspace("YOUR_EMAIL", "YOUR_PASSWORD")
    await hub.authenticate()

    # Fetch all devices
    devices = await hub.get_devices()

    # Find your light
    light = None
    for d in devices:
        name = d["attributes"].get("device-name")
        if name == LIGHT_NAME:
            light = d
            break
        if not light:
            print("Light not found.")
        return

    # Turn ON
    await hub.set_attribute(light, "power", "on")
    print("Light turned ON")

    # Set brightness to 50%
    await hub.set_attribute(light, "brightness", 50)
    print("Brightness set to 50%")

    # Turn OFF
    await hub.set_attribute(light, "power", "off")
    print("Light turned OFF")

asyncio.run(main())