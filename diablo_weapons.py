from random import randint, choice, sample
from vars import BASE_WEAPONS, QUALITY, RARITY, QUALITY_CHANCES, RARITY_CHANCE, SPECIAL_MODIFIERS, MODIFIER_NUMBER

class Weapon:
    def __init__(self, level : int, weapon_type : str, rarity : str, quality : str):
        self.level = level + RARITY[rarity]
        self.weapon_type = weapon_type
        self.rarity = rarity
        self.quality = quality

        num_modifiers = MODIFIER_NUMBER[rarity][0] if randint(1,100) <= 50 else MODIFIER_NUMBER[rarity][1]
        self.modifiers = sample(SPECIAL_MODIFIERS, num_modifiers)
        self.prefixes = [p["prefix"] for p in self.modifiers if p["prefix"] != ""]
        self.suffixes = [s["suffix"] for s in self.modifiers if s["suffix"] != ""]
        self.prefix = choice(self.prefixes) if self.prefixes != [] else ""
        self.suffix = choice(self.suffixes) if self.suffixes != [] else ""
        self.damage = round(BASE_WEAPONS[weapon_type][0] * QUALITY[quality][0] * (1.05 ** (level - 1)), 2)
        self.attack_speed = round(BASE_WEAPONS[weapon_type][1] * QUALITY[quality][1] * (1.01 ** (level - 1)), 2)
        self.crit_chance = round(BASE_WEAPONS[weapon_type][2] * QUALITY[quality][2] * (1.03 ** (level - 1)), 2)
        self.crit_damage = round(BASE_WEAPONS[weapon_type][3] * QUALITY[quality][3], 2)
        self.hit_chance = round(BASE_WEAPONS[weapon_type][4] * QUALITY[quality][4] * (1.03 ** (level - 1)), 2)
        self.stat_bonus = BASE_WEAPONS[weapon_type][5]

        for modifier in self.modifiers:
            if modifier["stats"] != [0, 0, 0, 0, 0]:
                for i in range(5):
                    if modifier["stats"][i] != 0 and i == 0:
                        self.damage = round(self.damage * modifier["stats"][i], 2)
                    elif modifier["stats"][i] != 0 and i == 1:
                        self.attack_speed = round(self.attack_speed * modifier["stats"][i], 2)
                    elif modifier["stats"][i] != 0 and i == 2:
                        self.crit_chance = round(self.crit_chance * modifier["stats"][i], 2)
                    elif modifier["stats"][i] != 0 and i == 3:
                        self.crit_damage = round(self.crit_damage * modifier["stats"][i], 2)
                    elif modifier["stats"][i] != 0 and i == 4:
                        self.hit_chance = round(self.hit_chance * modifier["stats"][i], 2)

        if self.crit_chance > 1:
            self.crit_chance = 1
        if self.hit_chance > 1:
            self.hit_chance = 1

        self.name = [
            self.prefix,
            self.rarity,
            self.quality,
            self.weapon_type,
            self.suffix
        ]

    
    def __str__(self):
        return f"""
    Name: {" ".join(self.name)}
    Level: {self.level}
    Weapon Type: {self.weapon_type}
    Weapon Rarity: {self.rarity}
    Weapon Quality: {self.quality}
    Damage: {self.damage}
    Crit Chance: {self.crit_chance * 100}%
    Crit Damage Multiplier: x{self.crit_damage} 
    Attack Speed: {self.attack_speed}
    Stat Bonus: {self.stat_bonus}
    Hit Chance: {self.hit_chance * 100}%
    Special Modifiers: 
        {"\n        ".join([f"- {modifier['description']}" for modifier in self.modifiers]) if self.modifiers != [] else "No special modifiers"}
        """

def generate_weapon(level = None):
    if level is None:
        level = randint(1, 100)
    weapon_type = choice(list(BASE_WEAPONS.items()))
    weapon_rarity = ""
    rarity_roll = randint(1, 100)
    quality_roll = randint(1, 100)
    for chance, rarity in RARITY_CHANCE.items():
        weapon_rarity = rarity
        if chance > rarity_roll:
            break
    for quality, chance in QUALITY_CHANCES[weapon_rarity].items():
        weapon_quality = quality
        if chance > quality_roll:
            break
    weapon = Weapon(level, weapon_type[0], weapon_rarity, weapon_quality)
    return weapon

with open("weapons.txt", "w") as f:
    for i in range(1, 101):
        for j in range(10):
            f.write(str(generate_weapon(i)) + "\n")
