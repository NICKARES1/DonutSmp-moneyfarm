# example.py:

import minescript
import time
import json
import re
import asyncio

from minescript_plus import Inventory, Key,Screen



tradable_items = [
    {"name": "repeater", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None},
    {"name": "comparator", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None},

]


def next_page():
    items = minescript.container_get_items()
    for element in items:
        if element.slot == 53:
            Inventory.click_slot(53)
            return True
    return False


def get_number(num):
    num = num.replace("$","")
    if num[-1] == "T":
        return float(num[:-1])*1000000000000
    if num[-1] == "B":
        return float(num[:-1])*1000000000 
    if num[-1] == "M":
        return float(num[:-1])*1000000 
    if num[-1] == "K":
        return float(num[:-1])*1000
    return float(num)    
    


def get_auction_cheapest_stack(itemname):
    minescript.execute("ah "+itemname) 
    Screen.wait_screen("",5000)


    sorted_items = []
    another_page = True
    while another_page:
        start = time.time()
        Screen.wait_screen("",5000)
        if(time.time()-start<0.3):
            time.sleep(0.25-(time.time()-start))
        items = minescript.container_get_items()
        for item in items:
            nbt = item.nbt
            price = "not_found"
            regex_pattern = r'Price: "},{color:"#00FC88",text:"(\$[0-9,.]+[A-Za-z]?)"'
            if nbt:
                match = re.search(regex_pattern, nbt)
                if match:
                    """  {
                        "item": "minecraft:iron_block",
                        "count": 2,
                        "price": "$10K",
                        "nbt": "{components:{\"minecraft:custom_data\":{PublicBukkitValues:{\"minecraft:auctionsecurity\":1}},\"minecraft:custom_name\":{italic:0b,text:\"Block of Iron\"},\"minecraft:lore\":[{extra:[{color:\"white\",text:\"Price: \"},{color:\"#00FC88\",text:\"$10K\"}],italic:0b,text:\"\"},{extra:[{color:\"white\",text:\"Seller: \"},{color:\"#00FC88\",text:\"Go_Shower\"}],italic:0b,text:\"\"},{extra:[{color:\"white\",text:\"Time Left: \"},{color:\"#00FC88\",text:\"23h 59m 59s\"}],italic:0b,text:\"\"},{extra:[{color:\"gray\",italic:0b,text:\"Worth: \"},{bold:0b,color:\"#00FF00\",italic:0b,obfuscated:0b,strikethrough:0b,text:\"$90\",underlined:0b}],text:\"\"}]},count:2,id:\"minecraft:iron_block\"}",
                        "slot": 0
                    },
                    """
                    price = match.group(1)
                    if price is None:
                        continue
                    sorted_items.append({
                        "item": item.item,
                        "count": item.count,
                        "price": price,
                        "nbt": item.nbt,
                        "slot": item.slot           
                    })
        another_page = next_page()
        
        


    cheapest = 1000000000000000000000000000000000000000
    for element in sorted_items:
        if element["item"] == "minecraft:"+itemname:
            if get_number(element["price"])/float(element["count"]) <cheapest:
                cheapest = round(get_number(element["price"])/float(element["count"]))

    if cheapest == 1000000000000000000000000000000000000000:
        return "not_found"
    else:
        return cheapest





try:
    for element in tradable_items:
        element["auction_price_per_stack"] = get_auction_cheapest_stack(element["name"])
    with open("C:/Users/nicks/AppData/Roaming/ModrinthApp/profiles/Nick 1.0.0.mrpack/minescript/log.json", "w") as f:
        json.dump(tradable_items, f, indent=2)




except Exception as e:
        minescript.echo(f"Fehler: {e}")
        with open("C:/Users/nicks/AppData/Roaming/ModrinthApp/profiles/Nick 1.0.0.mrpack/minescript/errorlog.json", "w") as f:
            f.write(repr(e))