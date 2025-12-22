import minescript
import time
from minescript_plus import Inventory,Key,Screen

keybind_swap = "g"
keybind_openinv = "e"
prefered_totem_hotbar_slot = 5 #0-8
hotbarload = False   #doesnt work great yet
cooldown = 0.01



while True:
    inv = minescript.player_inventory()
    totem_e = False
    for element in inv:
        #minescript.echo(element.slot,element.item)
        if element.slot == 40:
            if element.item == "minecraft:totem_of_undying":
                totem_e = True
    if not totem_e:
        newtotem = Inventory.find_item("minecraft:totem_of_undying")
        if newtotem is not None:
                if newtotem >8:
                    Key.press_key("key.keyboard."+keybind_openinv,True)
                    Screen.wait_screen("",5000)
                    Inventory.click_slot(newtotem, right_button=False)
                    time.sleep(cooldown)
                    Inventory.click_slot(45, right_button=False)
                    time.sleep(0.01)
                    Screen.close_screen()
                if newtotem <=8:
                    minescript.player_inventory_select_slot(newtotem)
                    time.sleep(cooldown)
                    Key.press_key("key.keyboard."+keybind_swap,True)
                    if hotbarload:
                        time.sleep(0.01)
                        Key.press_key("key.keyboard."+keybind_openinv,True)
                        newtotem = Inventory.find_item("minecraft:totem_of_undying")
                        Screen.wait_screen("",5000)
                        Inventory.inventory_hotbar_swap(newtotem,prefered_totem_hotbar_slot)
                        Screen.close_screen()

    


    time.sleep(0.01)


