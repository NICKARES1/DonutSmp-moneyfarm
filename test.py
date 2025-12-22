# example.py:

import minescript
import time
import json
import re
import asyncio

from minescript_plus import Inventory, Key,Screen




tradable_items = [
  {"name": "elytra", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "dragon_head", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "zombie_head", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "skeleton_skull", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "creeper_head", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "wither_skeleton_skull", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "piglin_head", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "netherite_block", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["netherite_ingot", "netherite_ingot", "netherite_ingot", "netherite_ingot", "netherite_ingot", "netherite_ingot", "netherite_ingot", "netherite_ingot", "netherite_ingot"], "crafting multiplier": None},
  {"name": "netherite_ingot", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["netherite_scrap", "netherite_scrap", "netherite_scrap", "netherite_scrap", "gold_ingot", "gold_ingot", "gold_ingot", "gold_ingot"], "crafting multiplier": None},
  {"name": "netherite_scrap", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "ancient_debris", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "netherite_helmet", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["diamond_helmet", "netherite_ingot"], "crafting multiplier": None},
  {"name": "netherite_chestplate", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["diamond_chestplate", "netherite_ingot"], "crafting multiplier": None},
  {"name": "netherite_leggings", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["diamond_leggings", "netherite_ingot"], "crafting multiplier": None},
  {"name": "netherite_boots", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["diamond_boots", "netherite_ingot"], "crafting multiplier": None},
  {"name": "netherite_sword", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["diamond_sword", "netherite_ingot"], "crafting multiplier": None},
  {"name": "netherite_pickaxe", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["diamond_pickaxe", "netherite_ingot"], "crafting multiplier": None},
  {"name": "netherite_axe", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["diamond_axe", "netherite_ingot"], "crafting multiplier": None},
  {"name": "netherite_shovel", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["diamond_shovel", "netherite_ingot"], "crafting multiplier": None},
  {"name": "netherite_hoe", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["diamond_hoe", "netherite_ingot"], "crafting multiplier": None},
  {"name": "enchanted_golden_apple", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "mace", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["heavy_core", "breeze_rod"], "crafting multiplier": None},
  {"name": "heavy_core", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "enchanted_book_wind_burst", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "heart_of_the_sea", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "trident", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "trial_key", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "ominous_trial_key", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "nautilus_shell", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "lodestone", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["chiseled_stone_bricks", "chiseled_stone_bricks", "chiseled_stone_bricks", "chiseled_stone_bricks", "chiseled_stone_bricks", "chiseled_stone_bricks", "chiseled_stone_bricks", "chiseled_stone_bricks", "netherite_ingot"], "crafting multiplier": None},
  {"name": "beacon", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["glass", "glass", "glass", "glass", "glass", "nether_star", "obsidian", "obsidian", "obsidian"], "crafting multiplier": None},
  {"name": "nether_star", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "deepslate_emerald_ore", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "gilded_blackstone", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "phantom_membrane", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "conduit", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["nautilus_shell", "nautilus_shell", "nautilus_shell", "nautilus_shell", "nautilus_shell", "nautilus_shell", "nautilus_shell", "nautilus_shell", "heart_of_the_sea"], "crafting multiplier": None},
  {"name": "tall_grass", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "sponge", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "wet_sponge", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "suspicious_sand", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "suspicious_gravel", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "turtle_scute", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "diamond_block", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["diamond", "diamond", "diamond", "diamond", "diamond", "diamond", "diamond", "diamond", "diamond"], "crafting multiplier": None},
  {"name": "diamond", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "lectern", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["oak_slab", "oak_slab", "oak_slab", "bookshelf", "oak_slab"], "crafting multiplier": None},
  {"name": "emerald", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "emerald_block", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["emerald", "emerald", "emerald", "emerald", "emerald", "emerald", "emerald", "emerald", "emerald"], "crafting multiplier": None},
  {"name": "pufferfish", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "glow_item_frame", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["item_frame", "glow_ink_sac"], "crafting multiplier": None},
  {"name": "sea_lantern", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["prismarine_shard", "prismarine_shard", "prismarine_shard", "prismarine_shard", "prismarine_crystals", "prismarine_crystals", "prismarine_crystals", "prismarine_crystals", "prismarine_crystals"], "crafting multiplier": None},
  {"name": "echo_shard", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "pearlescent_froglight", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "verdant_froglight", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "ochre_froglight", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "bee_nest", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "bookshelf", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["oak_planks", "oak_planks", "oak_planks", "book", "book", "book", "oak_planks", "oak_planks", "oak_planks"], "crafting multiplier": None},
  {"name": "gold_block", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["gold_ingot", "gold_ingot", "gold_ingot", "gold_ingot", "gold_ingot", "gold_ingot", "gold_ingot", "gold_ingot", "gold_ingot"], "crafting multiplier": None},
  {"name": "gold_ingot", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "raw_gold_block", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["raw_gold", "raw_gold", "raw_gold", "raw_gold", "raw_gold", "raw_gold", "raw_gold", "raw_gold", "raw_gold"], "crafting multiplier": None},
  {"name": "map", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["paper", "paper", "paper", "paper", "compass", "paper", "paper", "paper", "paper"], "crafting multiplier": None},
  {"name": "amethyst_cluster", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "recovery_compass", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["echo_shard", "echo_shard", "echo_shard", "echo_shard", "compass", "echo_shard", "echo_shard", "echo_shard", "echo_shard"], "crafting multiplier": None},
  {"name": "honey_block", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["honey_bottle", "honey_bottle", "honey_bottle", "honey_bottle"], "crafting multiplier": None},
  {"name": "enchanting_table", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["book", "diamond", "diamond", "obsidian", "obsidian", "obsidian", "obsidian"], "crafting multiplier": None},
  {"name": "rabbit_foot", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "leather", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "target", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["redstone", "redstone", "redstone", "redstone", "hay_block", "redstone", "redstone", "redstone", "redstone"], "crafting multiplier": None},
  {"name": "breeze_rod", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "deepslate_coal_ore", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "deepslate_iron_ore", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "deepslate_copper_ore", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "deepslate_gold_ore", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "deepslate_redstone_ore", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "deepslate_lapis_ore", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "deepslate_diamond_ore", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "anvil", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["iron_block", "iron_block", "iron_block", "iron_ingot", "iron_ingot", "iron_ingot", "iron_ingot"], "crafting multiplier": None},
  {"name": "coal_block", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["coal", "coal", "coal", "coal", "coal", "coal", "coal", "coal", "coal"], "crafting multiplier": None},
  {"name": "book", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["paper", "paper", "paper", "leather"], "crafting multiplier": None},
  {"name": "large_amethyst_bud", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "medium_amethyst_bud", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "small_amethyst_bud", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "sculk_shrieker", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "glow_ink_sac", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "hay_block", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["wheat", "wheat", "wheat", "wheat", "wheat", "wheat", "wheat", "wheat", "wheat"], "crafting multiplier": None},
  {"name": "shroomlight", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "ink_sac", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "crafter", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["iron_ingot", "iron_ingot", "iron_ingot", "iron_ingot", "crafting_table", "iron_ingot", "redstone", "dropper", "redstone"], "crafting multiplier": None},
  {"name": "nether_gold_ore", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "redstone_block", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["redstone", "redstone", "redstone", "redstone", "redstone", "redstone", "redstone", "redstone", "redstone"], "crafting multiplier": None},
  {"name": "dispenser", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["cobblestone", "cobblestone", "cobblestone", "cobblestone", "bow", "cobblestone", "cobblestone", "redstone", "cobblestone"], "crafting multiplier": None},
  {"name": "dropper", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["cobblestone", "cobblestone", "cobblestone", "cobblestone", "cobblestone", "cobblestone", "redstone", "cobblestone"], "crafting multiplier": None},
  {"name": "repeater", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["redstone_torch", "redstone", "redstone_torch", "stone", "stone", "stone"], "crafting multiplier": None},
  {"name": "comparator", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["redstone_torch", "nether_quartz", "redstone_torch", "stone", "stone", "stone"], "crafting multiplier": None},
  {"name": "item_frame", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["stick", "stick", "stick", "stick", "leather", "stick", "stick", "stick", "stick"], "crafting multiplier": None},
  {"name": "slime_block", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["slime_ball", "slime_ball", "slime_ball", "slime_ball", "slime_ball", "slime_ball", "slime_ball", "slime_ball", "slime_ball"], "crafting multiplier": None},
  {"name": "lime_concrete", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "small_dripleaf", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "dark_prismarine", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": ["prismarine_shard", "prismarine_shard", "prismarine_shard", "prismarine_shard", "ink_sac", "prismarine_shard", "prismarine_shard", "prismarine_shard", "prismarine_shard"], "crafting multiplier": None},
  # Music Discs (Beispiele)
  {"name": "music_disc_5", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "music_disc_pigstep", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "music_disc_otherside", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "music_disc_relic", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "music_disc_creator", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "music_disc_precipice", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  # Pottery Sherds (Beispiele)
  {"name": "angler_pottery_sherd", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "archer_pottery_sherd", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "arms_up_pottery_sherd", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "danger_pottery_sherd", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "flow_pottery_sherd", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None},
  {"name": "gush_pottery_sherd", "auction_price_per_stack": None, "highest_order_per_stack": None, "multiplier": None, "profit_per_stack": None, "buy_all": False, "Profit_if_buy_all": 0, "crafting": [], "crafting multiplier": None}
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
    
def gettotalcraftmoney(items_list):
    if "Items to craft not found" == items_list: return "Items to craft not found"
    price = 0
    for element in items_list:
        found = False
        for item in tradable_items:
            if element == item["name"]:
                found = True
                if item["crafting"]:
                    for obj in item["crafting"]:
                        sub_price = gettotalcraftmoney([obj])
                        if isinstance(sub_price, (int, float)):
                            price += sub_price
                        else:
                            if isinstance(item["highest_order_per_stack"], (int, float)):
                                price += item["highest_order_per_stack"]
                            else:
                                return "Items to craft not found"

                else:
                    if isinstance(item["highest_order_per_stack"], (int, float)):
                        price += item["highest_order_per_stack"]
                    else:
                        return "Items to craft not found"
        if  not found:
            return "Items to craft not found"
    return price


def get_auction_cheapest_stack(itemname):
    minescript.execute("ah "+itemname) 
    Screen.wait_screen("",5000)


    sorted_items = []
    another_page = True
    page = 0
    while another_page and page <25:
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
        
        with open("C:/Users/nicks/AppData/Roaming/ModrinthApp/profiles/Nick 1.0.0.mrpack/minescript/log.json", "w") as f:
            json.dump(tradable_items, f, indent=2)


    for element in tradable_items:
        try:
            if not element["crafting"]:
                continue
            cost_craft = gettotalcraftmoney(element["crafting"])
            if isinstance(cost_craft, (int, float)) and cost_craft > 0 and isinstance(element["auction_price_per_stack"], (int, float)):
                element["crafting multiplier"] = element["auction_price_per_stack"] / cost_craft
            else:
                element["crafting multiplier"] = "Items to craft not found or cant craft item"
        except Exception as e:
            with open("C:/Users/nicks/AppData/Roaming/ModrinthApp/profiles/Nick 1.0.0.mrpack/minescript/errorlog.json", "w") as f:
                f.write(f"Fehler: {repr(e)} bei Element: {repr(element)}\n")

            
                


    tradable_items.sort(key=lambda item: item["profit_per_stack"] or 0, reverse=True)
    for item in tradable_items:
        if isinstance(item["highest_order_per_stack"], (int, float)) and money > item["highest_order_per_stack"] *64*26:
            item["buy_all"]= True
            break
    with open("C:/Users/nicks/AppData/Roaming/ModrinthApp/profiles/Nick 1.0.0.mrpack/minescript/log.json", "w") as f:
        json.dump(tradable_items, f, indent=2)




except Exception as e:
        minescript.echo(f"Fehler: {e}")
        with open("C:/Users/nicks/AppData/Roaming/ModrinthApp/profiles/Nick 1.0.0.mrpack/minescript/errorlog.json", "w") as f:
            f.write(repr(e))