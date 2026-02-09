# Dictionary of base weapon types with their base stats in format: 
# type_name: [Damage, Atack Speed, Crit chance, Crit damage multiplier, Hit Chance, Stat bonus (Str, Int, Dex, Con)]
BASE_WEAPONS = {
    # --- Two-Handed Weapons ---
    # Slow, heavy hitters with lower hit chance but massive damage per swing
    "2H Sword":        [10, 20, 0.10, 1.5, 0.80, "str"],
    "Greataxe":        [14, 14, 0.08, 1.8, 0.74, "str"],
    "Warhammer":       [12, 16, 0.05, 1.4, 0.78, "str"],
    "Halberd":         [11, 18, 0.07, 1.6, 0.78, "str"],
    "Maul":            [13, 15, 0.04, 1.3, 0.75, "con"],
    "Pike":            [9,  22, 0.09, 1.5, 0.82, "dex"],
    # --- One-Handed Weapons ---
    # Moderate damage, moderate speed; meant to pair with shields or off-hands
    "Longsword":       [7,  28, 0.10, 1.5, 0.83, "str"],
    "Mace":            [8,  24, 0.06, 1.4, 0.82, "str"],
    "Flail":           [7,  26, 0.08, 1.6, 0.82, "str"],
    "War Axe":         [8,  25, 0.09, 1.7, 0.80, "str"],
    "Morning Star":    [9,  22, 0.07, 1.5, 0.76, "str"],
    "Scimitar":        [6,  30, 0.12, 1.5, 0.88, "dex"],
    # --- Fast / Finesse Weapons ---
    # Low damage per hit but very fast, high crit, high accuracy
    "Dagger":          [3,  50, 0.18, 2.0, 0.95, "dex"],
    "Rapier":          [5,  35, 0.15, 1.8, 0.90, "dex"],
    "Katar":           [4,  42, 0.16, 1.9, 0.90, "dex"],
    "Short Sword":     [5,  34, 0.12, 1.6, 0.90, "dex"],
    # --- Ranged Weapons ---
    # Trade melee presence for range advantage; varying speed/damage profiles
    "Shortbow":        [5,  36, 0.11, 1.5, 0.86, "dex"],
    "Longbow":         [9,  20, 0.10, 1.7, 0.80, "dex"],
    "Crossbow":        [11, 16, 0.12, 1.6, 0.84, "dex"],
    "Hand Crossbow":   [6,  30, 0.13, 1.5, 0.88, "dex"],
    # --- Magic Weapons ---
    # Int-based; lower physical stats but enable spell synergies
    "Wand":            [4,  40, 0.14, 1.7, 0.92, "int"],
    "Staff":           [7,  24, 0.10, 1.6, 0.85, "int"],
    "Scepter":         [6,  30, 0.11, 1.5, 0.88, "int"],
    "Orb":             [3,  48, 0.16, 1.8, 0.94, "int"]
}

#Item quality levels with modifiers to first 5 stats of an item
QUALITY = {
    "Broken": [0.1, 0.5, 0.1, 1.0, 0.2],
    "Damaged": [0.2, 0.6, 0.15, 1.1, 0.3],
    "Flimsy": [0.3, 0.3, 0.2, 1.2, 0.4],
    "Crude": [0.4, 0.5, 0.3, 1.3, 0.5],
    "Rough": [0.5, 0.6, 0.4, 1.4, 0.6],
    "Dull": [0.65, 0.7, 0.55, 1.5, 0.7],
    "Dirty": [0.8, 0.85, 0.7, 1.6, 0.85],
    "": [1, 1, 1, 1.75, 1],
    "Clean": [1.05, 1.05, 1.05, 2.0, 1.05],
    "Sharp": [1.15, 1.05, 1.2, 2.25, 1.1],
    "Elegant": [1.1, 1.15, 1.15, 2.5, 1.2],
    "Fine": [1.2, 1.15, 1.2, 2.75, 1.2],
    "Quality": [1.3, 1.2, 1.3, 3.0, 1.25],
    "Noble": [1.4, 1.25, 1.35, 3.25, 1.3],
    "Superior": [1.5, 1.3, 1.45, 3.5, 1.4],
    "Exceptional": [1.65, 1.35, 1.55, 3.75, 1.5],
    "Masterwork": [1.8, 1.4, 1.7, 4.0, 1.6],
}

# Item rarity with modifiers to level of the item. i.e. Uncommon has stats as if it was 2 levels higher
RARITY = {
    "Common": 0,
    "Uncommon": 2,
    "Rare": 3,
    "Epic": 5,
    "Heroic": 7,
    "Legendary": 10
}

RARITY_CHANCE = {
    50: "Common",
    75: "Uncommon",
    87: "Rare",
    94: "Epic",
    98: "Heroic",
    100: "Legendary"
}

# Items have a chance for certain quality based on their rarity
# Each rarity maps to a dict of {quality: percent_chance}
QUALITY_CHANCES = {
    "Common": {
        "Broken": 2, "Damaged": 7, "Flimsy": 15, "Crude": 27, "Rough": 42,
        "Dull": 60, "Dirty": 77, "": 89, "Clean": 95, "Sharp": 98,
        "Elegant": 99, "Fine": 100,
    },
    "Uncommon": {
        "Crude": 2, "Rough": 7, "Dull": 16, "Dirty": 30, "": 50,
        "Clean": 70, "Sharp": 84, "Elegant": 93, "Fine": 98, "Quality": 100,
    },
    "Rare": {
        "Dull": 1, "Dirty": 4, "": 11, "Clean": 23, "Sharp": 41,
        "Elegant": 63, "Fine": 81, "Quality": 93, "Noble": 98, "Superior": 100,
    },
    "Epic": {
        "": 2, "Clean": 7, "Sharp": 17, "Elegant": 32, "Fine": 52,
        "Quality": 74, "Noble": 89, "Superior": 97, "Exceptional": 100,
    },
    "Heroic": {
        "Clean": 1, "Sharp": 4, "Elegant": 11, "Fine": 23, "Quality": 41,
        "Noble": 63, "Superior": 83, "Exceptional": 96, "Masterwork": 100,
    },
    "Legendary": {
        "Sharp": 1, "Elegant": 3, "Fine": 8, "Quality": 18, "Noble": 34,
        "Superior": 56, "Exceptional": 81, "Masterwork": 100,
    },
}
# Special modifiers for items, list short for demo purposes, but can be expanded
SPECIAL_MODIFIERS = [
    {"description": "10% chance to cause Bleeding (5% of max health per second for 5 seconds)", "prefix": "", "suffix": "of deep wounds", "stats": [0, 0, 0, 0, 0]},
    {"description": "Ignores 50% of enemy's armor", "prefix": "Piercing", "suffix": "", "stats": [0, 0, 0, 0, 0]},
    {"description": "Increased speed", "prefix": "", "suffix": "of haste", "stats": [0, 1.75, 0, 0, 0]},
    {"description": "Increased accuracy", "prefix": "", "suffix": "of sure hand", "stats": [0, 0, 0, 0, 2]},
    {"description": "Applies burn 10% of weapon damage for 5s", "prefix": "Burning", "suffix": "", "stats": [0, 0, 0, 0, 0]},
    {"description": "Lights up area around player", "prefix": "", "suffix": "of illumination", "stats": [0, 0, 0, 0, 0]},
    {"description": "Applies poison 10% of weapon damage for 5s", "prefix": "Toxic", "suffix": "", "stats": [0, 0, 0, 0, 0]},
    {"description": "Applies freeze 10% of weapon damage for 5s", "prefix": "Frosty", "suffix": "", "stats": [0, 0, 0, 0, 0]},
    {"description": "Deals additional shock damage, 10% of weapon damage for 5s", "prefix": "", "suffix": "of thunder", "stats": [0, 0, 0, 0, 0]}
]

# Tuple of (min, max) number of modifiers for each rarity
MODIFIER_NUMBER = {
    "Common": (0,0),
    "Uncommon": (0,1),
    "Rare": (1,2),
    "Epic": (2,3),
    "Heroic": (3,4),
    "Legendary": (4,4)
}