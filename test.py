# example.py:

import minescript
import time
import json
import re
import asyncio

from minescript_plus import Inventory, Key,Screen



tradable_items = [
    # Redstone/Mechanik (64er Stacks)
    {"name": "repeater", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "comparator", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "redstone", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "observer", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "piston", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "dispenser", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "dropper", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "hopper", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "lever", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "target", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "daylight_detector", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "tnt", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},

    # Farm- und Massenwaren (64er Stacks)
    {"name": "sugar_cane", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "bamboo", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "bone", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "kelp", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "oak_log", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "cobblestone", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "glass", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "sand", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "gravel", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "string", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "gunpowder", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": 0},
    {"name": "rotten_flesh", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "spider_eye", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "firework_rocket", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "packed_ice", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "blue_ice", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "slime_ball", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "honey_bottle", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "honeycomb", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "nether_wart", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "magma_cream", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "glowstone_dust", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "chorus_fruit", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},

    # Erze und Währungen (64er Stacks)
    {"name": "iron_ingot", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "gold_ingot", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "diamond", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "emerald", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "lapis_lazuli", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "coal", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "quartz", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},

    # End-Game Materialien (64er Stacks)
    {"name": "blaze_rod", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "ghast_tear", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "ender_pearl", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "end_stone", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "purpur_block", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "end_rod", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "prismarine_shard", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "prismarine_crystal", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "sea_lantern", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},

    # Spezifische Blöcke und Drops (64er Stacks)
    {"name": "terracotta", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "concrete_powder", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0}, # Beliebt für Bauprojekte
    {"name": "wool", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0}, # Kann lukrativ sein (siehe Suchergebnisse)
    {"name": "carpet", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "diorite", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "andesite", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "granite", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "netherrack", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "basalt", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "blackstone", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "mushroom_stem", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "brown_mushroom_block", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "red_mushroom_block", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "dirt", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "ice", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
    {"name": "scaffolding", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0},
]
possible_sell_items = 26
money = 243460

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
    page = 0
    while another_page and page <15:
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
        page += 1
        
        


    cheapest = 1000000000000000000000000000000000000000
    for element in sorted_items:
        if element["item"] == "minecraft:"+itemname:
            if get_number(element["price"])/float(element["count"]) <cheapest:
                cheapest = round(get_number(element["price"])/float(element["count"]))

    if cheapest == 1000000000000000000000000000000000000000:
        return "not_found"
    else:
        return cheapest


def get_highest_order(itemname):
    minescript.execute("orders "+itemname) 
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
            regex_pattern =  r'text:"(\$\d[\d,.]*[A-Za-z]?) ",underlined:0b\},\{bold:0b,color:"white",italic:0b,obfuscated:0b,strikethrough:0b,text:"each"'
            if nbt and item.slot <45:
                match = re.search(regex_pattern, nbt)
                if match:
                    """  
                    ItemStack(item='minecraft:comparator', count=1, nbt='{components:{"minecraft:attribute_modifiers":[{amount:0.0d,id:"minecraft:ghide",operation:"add_value",type:"minecraft:armor"}],"minecraft:custom_data":{PublicBukkitValues:{"minecraft:auctionsecurity":1,"minecraft:wi":1765723665285L}},"minecraft:custom_name":{extra:[{bold:0b,color:"#00FC88",italic:0b,obfuscated:0b,strikethrough:0b,text:"habijbb\'s Order",underlined:0b}],text:""},"minecraft:lore":[{extra:[{bold:0b,color:"#FFFFFF",italic:0b,obfuscated:0b,strikethrough:0b,text:"Redstone Comparators",underlined:0b}],text:""},{extra:[{bold:0b,color:"#00FC88",italic:0b,obfuscated:0b,strikethrough:0b,text:"$1 ",underlined:0b},{bold:0b,color:"white",italic:0b,obfuscated:0b,strikethrough:0b,text:"each",underlined:0b}],text:""},"",{extra:[{bold:0b,color:"#80802A",italic:0b,obfuscated:0b,strikethrough:0b,text:"161/",underlined:0b},{bold:0b,color:"#008F4D",italic:0b,obfuscated:0b,strikethrough:0b,text:"1K ",underlined:0b},{bold:0b,color:"#878787",italic:0b,obfuscated:0b,strikethrough:0b,text:"Delivered",underlined:0b}],text:""},{extra:[{bold:0b,color:"#80802A",italic:0b,obfuscated:0b,strikethrough:0b,text:"$161/",underlined:0b},{bold:0b,color:"#008F4D",italic:0b,obfuscated:0b,strikethrough:0b,text:"$1K ",underlined:0b},{bold:0b,color:"#878787",italic:0b,obfuscated:0b,strikethrough:0b,text:"Paid",underlined:0b}],text:""},"",{extra:[{bold:0b,color:"white",italic:0b,obfuscated:0b,strikethrough:0b,text:"Click to deliver ",underlined:0b},{bold:0b,color:"#00FC88",italic:0b,obfuscated:0b,strikethrough:0b,text:"habijbb",underlined:0b},{color:"white",italic:0b,text:" "},{bold:0b,color:"#FFFFFF",italic:0b,obfuscated:0b,strikethrough:0b,text:"Redstone Comparators",underlined:0b}],text:""},{extra:[{bold:0b,color:"dark_gray",italic:0b,obfuscated:0b,strikethrough:0b,text:"3d 17h 24m Until Order expires",underlined:0b}],text:""}],"minecraft:tooltip_display":{hidden_components:["minecraft:attribute_modifiers"]}},count:1,id:"minecraft:comparator"}', slot=30, selected=None)
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

        
        


    highest = 0
    for element in sorted_items:
        if element["item"] == "minecraft:"+itemname:
            if get_number(element["price"]) >highest:
                highest = round(get_number(element["price"]))

    if highest == 0:
        return "not_found"
    else:
        return highest




try:
    for element in tradable_items:
        auction = get_auction_cheapest_stack(element["name"])
        order = get_highest_order(element["name"])
        element["auction_price_per_stack"] = auction
        element["highest_order_per_stack"] = order
        if isinstance(auction, (int, float)) and isinstance(order, (int, float)) and order != 0:
            element["multiplier"] = auction / order
            element["profit_per_stack"] = (auction - order) * 64
            element["Profit_if_buy_all"] = (auction - order) * 64 * 26
        else:
            element["multiplier"] = 0
            element["profit_per_stack"] = 0
            element["Profit_if_buy_all"] = 0


    tradable_items.sort(key=lambda item: item["profit_per_stack"] or 0, reverse=True)
    for item in tradable_items:
        if money > item["highest_order_per_stack"] *64*26:
            item["buy_all"]= True
            break
    with open("C:/Users/nicks/AppData/Roaming/ModrinthApp/profiles/Nick 1.0.0.mrpack/minescript/log.json", "w") as f:
        json.dump(tradable_items, f, indent=2)




except Exception as e:
        minescript.echo(f"Fehler: {e}")
        with open("C:/Users/nicks/AppData/Roaming/ModrinthApp/profiles/Nick 1.0.0.mrpack/minescript/errorlog.json", "w") as f:
            f.write(repr(e))