# example.py:


import minescript
import time
import json
import re
import asyncio
from minescript_plus import Inventory, Keybind, Screen




async def get_item_price():
    minescript.execute("ah") 
    await asyncio.sleep(0.1)

    items = minescript.container_get_items()
    sorted_items = []
    for item in items:
        nbt = item.nbt
        price = "not_found"
        regex_pattern = r'Price: "},{color:"#00FC88",text:"(\$[0-9,.]+[A-Za-z]?)"'
        if nbt:
            match = re.search(regex_pattern, nbt)
            if match:
                price = match.group(1)
                sorted_items.append({
                    "item": item.item,
                    "count": item.count,
                    "price": price,
                    "nbt": item.nbt,
                    "slot": item.slot           
                })
    return sorted_items


async def next_page():
    await asyncio.sleep(0.1)
    items = minescript.container_get_items()
    for element in items:
        if element.slot == 53:
            Inventory.click_slot(53)
            return True
    return False

time.sleep(10)
try:
    while True:
        asyncio.run(next_page())
except Exception as e:
        minescript.echo(f"Fehler: {e}")
        with open("C:/Users/nicks/AppData/Roaming/ModrinthApp/profiles/Nick 1.0.0.mrpack/minescript/errorlog.json", "w") as f:
            f.write(repr(e))