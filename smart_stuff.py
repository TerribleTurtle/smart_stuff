import aiohttp
import pysmartthings
import asyncio
import tkinter as tk


token = "THANK-YOU"


async def get_lights():
    async with aiohttp.ClientSession() as session:
        api = pysmartthings.SmartThings(session, token)
        devices = await api.devices()
        lights = []
        for device in range(0, len(devices)):
            if devices[device].capabilities[0] == 'switch':
                lights.append(devices[device])
    return lights


def draw(lights):
    root = tk.Tk()
    num = 0
    for light in range(0, len(lights)):
        b = tk.Button(root, text=f"{lights[light].label}", command=lambda c = num: check_button(c))
        b.pack()
        num += 1
    stop = tk.Button(root, text="QUIT")
    stop.pack()
    root.mainloop()


async def toggle_lights(light):
    async with aiohttp.ClientSession() as session:
        api = pysmartthings.SmartThings(session, token)
        devices = await api.devices()
        lights = []
        for device in range(0, len(devices)):
            if devices[device].capabilities[0] == 'switch':
                lights.append(devices[device])


        current_light = lights[light]
        await current_light.status.refresh()
        if current_light.status.switch:
            result = await current_light.switch_off()
            assert result == True
        else:
            result = await current_light.switch_on()
            assert result == True



def check_button(light):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(toggle_lights(light))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    lights = loop.run_until_complete(get_lights())
    draw(lights)
