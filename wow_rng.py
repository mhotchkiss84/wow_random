"""
WoW RNG Character Creator v 0.1.5
Created By: Mike Hotchkiss
Gist @: https://gist.github.com/mhotchkiss84/3b7f421ba51c0c914d7c72471ca30e1a
Created: 29 Oct 2019
Updated: 25 Jan 2020
v 0.1.5 Changes:
-Cleaned code
-Added all changes to reflect updates in patch 8.3
-Added server list and ability to include a random US server
-Added random specialization option
-Fixed a bug causing crash on the Monk class being selected
v 0.1.1 Changes:
All coding was redone. The main reason for this was to allow for the user
to be able to select which Allied races they have unlocked. In the previous
version if Allied races was used then it would use all of the Allied races.
Not everyone has all the races unlocked, which lead to this rework. Due to the
nature of the previous versions code this was not possible.
Class moved to top of selection order to more balance class selection. In the
previous version Demon Hunters would have a very low probability due to the
faction and race being chose first.
More update notes on the Gist page. Only major changes will be reflected here.
Feel free to share, but please give me credit. - Thanks
Report bugs/issues/change request please contact sxs.linux@hotmail.com
"""

# To Do:
# Clean code
# Check spelling & punctuation in lists
# Add Oceanic, Brazil, Mexico, EU server options
# Create UI
# Move update/patch notes to a separate Gist

import random


# Lists

# Faction List
factions = ["Alliance", "Horde"]
# Gender List
gender = ["Male", "Female"]

# User Selections

# Asking the user if they have a faction preference
faction_pref = ""

while faction_pref != "y":
    user_pref = input("Do you wish to include a random faction?: (Y/N) ")
    if user_pref.lower() == "y":
        faction_pref = user_pref
        break
    elif user_pref.lower() == "n":
        faction_pref = user_pref
        break
    else:
        print("Please enter y for yes, or n for no.")

# Asking the user what faction they prefer if they selected "n" above
user_faction = ""

while faction_pref.lower() == "n":
    faction_input = input("Please enter your faction: ")
    if faction_input.lower() == "alliance":
        user_faction = faction_input
        break
    elif faction_input.lower() == "horde":
        user_faction = faction_input
        break
    else:
        print("Please enter Horde or Alliance")
else:
    pass

if faction_pref.lower() == "y":
    user_faction = random.choice(factions)

# Asking users if they wish to include a random server
server_list = ["Aegwynn", "Aerie Peak", "Agamaggan", "Aggramar", "Akama", "Alexstrasza", "Alleria", "Altar of Storms",
               "Alterac Mountains", "Aman'Thul", "Andorhal", "Anetheron", "Antonidas", "Anub'arak", "Anvilmar",
               "Arathor", "Archimonde", "Area 52", "Argent Dawn", "Arthas", "Arygos", "Auchindoun", "Azgalor",
               "Azjol-Nerub", "Azshara", "Azuremyst", "Baelgun", "Balnazzar", "Barthilas", "Black Dragonflight",
               "Blackhand", "Blackrock", "Blackwater Raiders", "Blackwing Lair", "Blade's Edge", "Bladefist",
               "Bleeding Hollow", "Blood Furnace", "Bloodhoof", "Bloodscalp", "Bonechewer", "Borean Tundra",
               "Boulderfist", "Bronzebeard", "Burning Blade", "Burning Legion", "Caelestrasz", "Cairne",
               "Cenarion Circle", "Cenarius", "Cho'gall", "Chromaggus", "Coilfang", "Crushridge", "Daggerspine",
               "Dalaran", "Dalvengyr", "Dark Iron", "Darkspear", "Darrowmere", "Dath'Remar", "Dawnbringer", "Deathwing",
               "Demon Soul", "Dentarg", "Destromath", "Dethecus", "Detheroc", "Doomhammer", "Draenor", "Dragonblight",
               "Dragonmaw", "Drak'Tharon", "Drak'thul", "Draka", "Dreadmaul", "Drenden", "Dunemaul", "Durotan",
               "Duskwood", "Earthen Ring", "Echo Isles", "Eitrigg", "Eldre'Thalas", "Elune", "Emerald Dream", "Eonar",
               "Eredar", "Executus", "Exodar", "Farstriders", "Feathermoon", "Fenris", "Firetree", "Fizzcrank",
               "Frostmane", "Frostmourne", "Frostwolf", "Galakrond", "Garithos", "Garona", "Garrosh", "Ghostlands",
               "Gilneas", "Gnomeregan", "Gorefiend", "Gorgonnash", "Greymane", "Grizzly Hills", "Gul'dan", "Gundrak",
               "Gurubashi", "Hakkar", "Haomarush", "Hellscream", "Hydraxis", "Hyjal", "Icecrown", "Illidan", "Jaedenar",
               "Jubei'Thos", "Kael'thas", "Kalecgos", "Kargath", "Kel'Thuzad", "Khadgar", "Khaz Modan", "Khaz'goroth",
               "Kil'jaeden", "Kilrogg", "Kirin Tor", "Korgath", "Korialstrasz", "Kul Tiras", "Laughing Skull", "Lethon",
               "Lightbringer", "Lightning's Blade", "Lightninghoof", "Llane", "Lothar", "Madoran", "Maelstrom",
               "Magtheridon", "Maiev", "Mal'Ganis", "Malfurion", "Malorne", "Malygos", "Mannoroth", "Medivh", "Misha",
               "Mok'Nathal", "Moon Guard", "Moonrunner", "Mug'thol", "Muradin", "Nagrand", "Nathrezim", "Nazgrel",
               "Nazjatar", "Ner'zhul", "Nesingwary", "Nordrassil", "Norgannon", "Onyxia", "Perenolde", "Proudmoore",
               "Quel'dorei", "Ravencrest", "Ravenholdt", "Rexxar", "Rivendare", "Runetotem", "Sargeras", "Saurfang",
               "Scarlet Crusade", "Scilla", "Sen'jin", "Sentinels", "Shadow Council", "Shadowmoon", "Shadowsong",
               "Shandris", "Shattered Halls", "Shattered Hand", "Shu'halo", "Silver Hand", "Silvermoon",
               "Sisters of Elune", "Skullcrusher", "Skywall", "Smolderthorn", "Spinebreaker", "Spirestone", "Staghelm",
               "Steamwheedle Cartel", "Stonemaul", "Stormrage", "Stormreaver", "Stormscale", "Suramar", "Tanaris",
               "Terenas", "Terokkar", "Thaurissan", "The Forgotten Coast", "The Scryers", "The Underbog",
               "The Venture Co", "Thorium Brotherhood", "Thrall", "Thunderhorn", "Thunderlord", "Tichondrius",
               "Tortheldrin", "Trollbane", "Turalyon", "Twisting Nether", "Uldaman", "Uldum", "Undermine", "Ursin",
               "Uther", "Vashj", "Vek'nilash", "Velen", "Warsong", "Whisperwind", "Wildhammer", "Windrunner",
               "Winterhoof", "Wyrmrest Accord", "Ysera", "Ysondre", "Zangarmarsh", "Zul'jin", "Zuluhed"]

random_server_pref = ""

while random_server_pref.lower() != "y":
    server_bool = input("Do you wish to include a random server? : (Y/N) ")
    if server_bool.lower() == "y":
        random_server_pref = "y"
        break
    elif server_bool.lower() == "n":
        random_server_pref = "n"
        break
    else:
        print("Please enter y for yes, or n for no")


random_server = ""
if random_server_pref.lower() == "y":
    random_server = random.choice(server_list)

# Asking user if they have or wish to use the Allied Races
allied_avail = ""

while allied_avail.lower() != "y":
    allied_bool = input("Do you wish to include the Allied races?: (Y/N) ")
    if allied_bool.lower() == "y":
        allied_avail = allied_bool
        break
    elif allied_bool.lower() == "n":
        allied_avail = allied_bool
        break
    else:
        print("Please enter y for yes, or n for no")

# If statement for skipped if the user doesn't want to include Allied races
all_avail = ""

if allied_avail.lower() == "y":
    while all_avail.lower != "y":
        all_input = input("Do you have all the races unlocked?: (Y/N) ")
        if all_input.lower() == "y":
            all_avail = all_input
            break
        elif all_input.lower() == "n":
            all_avail = all_input
            break
        else:
            print("Please enter y for yes, or n for no.")
else:
    pass

# Checking which races the user has unlocked
dark_iron_avail = ""
kultiran_avail = ""
lightforged_avail = ""
void_avail = ""
highmountain_avail = ""
maghar_avail = ""
nightborne_avail = ""
zandalari_avail = ""
mecha_avail = ""
vulpera_avail = ""

if all_avail.lower() == "n":
    while dark_iron_avail == "":
        dark_iron_input = input("Do you have the Dark Iron Dwarf unlocked? (Y/N) ")
        if dark_iron_input.lower() == "y":
            dark_iron_avail = dark_iron_input
            break
        elif dark_iron_input.lower() == "n":
            dark_iron_avail = dark_iron_input
            break
        else:
            print("Please enter y for yes, or n for no")
    while kultiran_avail == "":
        kultiran_input = input("Do you have the Kul Tiran unlocked? (Y/N) ")
        if kultiran_input.lower() == "y":
            kultiran_avail = kultiran_input
            break
        elif kultiran_input.lower() == "n":
            kultiran_avail = kultiran_input
            break
        else:
            print("Please enter y for yes, or n for no")
    while lightforged_avail == "":
        light_input = input("Do you have the Lightforged Draenei unlocked? (Y/N) ")
        if light_input.lower() == "y":
            lightforged_avail = light_input
            break
        elif light_input.lower() == "n":
            lightforged_avail = light_input
            break
        else:
            print("Please enter y for yes, or n for no")
    while void_avail == "":
        void_input = input("Do you have the Void Elf unlocked? (Y/N) ")
        if void_input.lower() == "y":
            void_avail = void_input
            break
        elif void_input.lower() == "n":
            void_avail = void_input
            break
        else:
            print("Please enter y for yes or n for no")
    while highmountain_avail == "":
        high_input = input("Do you have the Highmountain Tauren unlocked? (Y/N) ")
        if high_input.lower() == "y":
            highmountain_avail = high_input
            break
        elif high_input.lower() == "n":
            highmountain_avail = high_input
            break
        else:
            print("Please enter y for yes or n for no")
    while maghar_avail == "":
        mag_input = input("Do you have the Mag'har Orc unlocked? (Y/N) ")
        if mag_input.lower() == "y":
            maghar_avail = mag_input
            break
        elif mag_input.lower() == "n":
            maghar_avail = mag_input
            break
        else:
            print("Please enter y for yes, or n for no")
    while nightborne_avail == "":
        night_input = input("Do you have the Nightborne unlocked? (Y/N) ")
        if night_input.lower() == "y":
            nightborne_avail = night_input
            break
        elif night_input.lower() == "n":
            nightborne_avail = night_input
            break
        else:
            print("Please enter y for yes, or n for no")
    while zandalari_avail == "":
        zand_input = input("Do you have the Zandalari unlocked? ")
        if zand_input.lower() == "y":
            zandalari_avail = zand_input
            break
        elif zand_input.lower() == "n":
            zandalari_avail = zand_input
            break
        else:
            print("Please enter y for yes, or n for no")
    while mecha_avail == "":
        mecha_input = input("Do you have the Mechagnome unlocked? ")
        if mecha_input.lower() == "y":
            mecha_avail = mecha_input
            break
        if mecha_input.lower() == "n":
            mecha_avail = mecha_input
            break
        else:
            print("Please enter y for yes, or n for no")
    while vulpera_avail == "":
        vulpera_input = input("Do you have the Vulpera unlocked? ")
        if vulpera_input.lower() == "y":
            vulpera_avail = vulpera_input
            break
        if vulpera_input.lower() == "n":
            vulpera_avail = vulpera_input
            break
        else:
            print("Please enter y for yes, or n for no")
    else:
        pass

# Asking user for Demon Hunter usage
dh_avail = ""
while dh_avail == "":
    dh_input = input("Do you wish to include the Demon Hunter class? (Y/N) ")
    if dh_input.lower() == "y":
        dh_avail = dh_input
        break
    elif dh_input.lower() == "n":
        dh_avail = dh_input
        break
    else:
        print("Please enter y for yes, or n for no")

# Classes setup ## Could have used a statement to check if user was using Demon Hunter and if not removing it from list
class_list = ["Warrior", "Paladin", "Hunter", "Rogue", "Priest", "Death Knight", "Shaman", "Mage",
              "Warlock", "Monk", "Druid", "Demon Hunter"]
class_no_dh = ["Warrior", "Paladin", "Hunter", "Rogue", "Priest", "Death Knight", "Shaman", "Mage",
               "Warlock", "Monk", "Druid"]

# Random class selection
final_class = ""
random_spec = ""

while random_spec == "":
    spec_choice = input("Do you wish to include a random specialization? (Y/N) ")
    if spec_choice.lower() == "y":
        random_spec = spec_choice
        break
    elif spec_choice.lower() == "n":
        random_spec = spec_choice
        break
    else:
        print("Please enter y for yes, or n for no.")

if dh_avail.lower() == "y":
    final_class = random.choice(class_list)
else:
    final_class = random.choice(class_no_dh)

# Spec selection
warrior_spec = ["Arms", "Fury", "Protection"]
paladin_spec = ["Holy", "Protection", "Retribution"]
hunter_spec = ["Beast Mastery", "Marksmanship", "Survival"]
rogue_spec = ["Assassination", "Outlaw", "Subtlety"]
priest_spec = ["Discipline", "Holy", "Shadow"]
dk_spec = ["Blood", "Frost", "Unholy"]
shaman_spec = ["Elemental", "Enhancement", "Restoration"]
mage_spec = ["Arcane", "Fire", "Frost"]
warlock_spec = ["Affliction", "Demonology", "Destruction"]
monk_spec = ["Brewmaster", "Mistweaver", "Windwalker"]
druid_spec = ["Balance", "Feral", "Guardian", "Restoration"]
dh_spec = ["Havoc", "Vengeance"]

final_spec = ""
if random_spec.lower() == "y":
    if final_class == "Warrior":
        final_spec = random.choice(warrior_spec)
    elif final_class == "Paladin":
        final_spec = random.choice(paladin_spec)
    elif final_class == "Hunter":
        final_spec = random.choice(hunter_spec)
    elif final_class == "Rogue":
        final_spec = random.choice(rogue_spec)
    elif final_class == "Priest":
        final_spec = random.choice(priest_spec)
    elif final_class == "Death Knight":
        final_spec = random.choice(dk_spec)
    elif final_class == "Shaman":
        final_spec = random.choice(shaman_spec)
    elif final_class == "Mage":
        final_spec = random.choice(mage_spec)
    elif final_class == "Warlock":
        final_spec = random.choice(warlock_spec)
    elif final_class == "Monk":
        final_spec = random.choice(monk_spec)
    elif final_class == "Druid":
        final_spec = random.choice(druid_spec)
    elif final_class == "Demon Hunter":
        final_spec = random.choice(dh_spec)


# Race/Class Lists

# Warrior Races
warrior_race_alliance = ["Dark Iron Dwarf", "Kul Tiran", "Lightforged Draenei", "Void Elf",
                         "Draenei", "Dwarf", "Gnome", "Human", "Night Elf", "Worgen", "Pandaren",
                         "Mechagnome"]
warrior_race_horde = ["Highmountain Tauren", "Mag'har Orc", "Nightborne", "Zandalari Troll",
                      "Blood Elf", "Goblin", "Orc", "Tauren", "Troll", "Undead", "Pandaren",
                      "Vulpera"]
# Paladin Races
paladin_race_alliance = ["Dark Iron Dwarf", "Lightforged Draenei", "Draenei", "Dwarf", "Human"]
paladin_race_horde = ["Zandalari Troll", "Blood Elf", "Tauren"]

# Hunter Races
hunter_race_alliance = ["Dark Iron Dwarf", "Kul Tiran", "Lightforged Draenei", "Void Elf",
                        "Draenei", "Dwarf", "Gnome", "Human", "Night Elf", "Worgen", "Pandaren",
                        "Mechagnome"]
hunter_race_horde = ["Highmountain Tauren", "Mag'har Orc", "Nightborne", "Zandalari Troll",
                     "Blood Elf", "Goblin", "Orc", "Tauren", "Troll", "Undead", "Pandaren",
                     "Vulpera"]
# Rogue Races
rogue_race_alliance = ["Dark Iron Dwarf", "Kul Tiran", "Void Elf", "Dwarf", "Gnome", "Human",
                       "Night Elf", "Worgen", "Pandaren", "Mechagnome"]
rogue_race_horde = ["Mag'har Orc", "Nightborne", "Zandalari Troll", "Blood Elf", "Goblin",
                    "Orc" "Troll", "Undead", "Pandaren", "Vulpera"]
# Priest Races
priest_race_alliance = ["Dark Iron Dwarf", "Kul Tiran", "Lightforged Draenei", "Void Elf",
                        "Draenei", "Dwarf", "Gnome", "Human", "Night Elf", "Worgen", "Pandaren",
                        "Mechagnome"]
priest_race_horde = ["Mag'har Orc", "Nightborne", "Zandalari Troll", "Blood Elf", "Goblin",
                     "Tauren", "Troll", "Undead", "Pandaren", "Vulpera"]
# Death Knight Races
# Allied Races CANNOT BE DK. No Need For Allied Statement To Run
dk_race_alliance = ["Draenei", "Dwarf", "Gnome", "Human", "Night Elf", "Worgen", "Pandaren",
                    "Void Elf", "Lightforged Draenei", "Kul Tiran", "Dark Iron Dwarf,",
                    "Mechagnome"]
dk_race_horde = ["Blood Elf", "Goblin", "Orc", "Tauren", "Troll", "Undead", "Pandaren",
                 "Nightborne", "Highmountain Tauren", "Zandalari Troll", "Vulpera", "Mag'har Orc"]

# Shaman Races
shaman_race_alliance = ["Dark Iron Dwarf", "Kul Tiran", "Draenei", "Dwarf", "Pandaren"]
shaman_race_horde = ["Highmountain Tauren", "Mag'har Orc", "Zandalari Troll", "Goblin", "Orc",
                     "Tauren", "Troll", "Pandaren", "Vulpera"]
# Mage Races
mage_race_alliance = ["Dark Iron Dwarf", "Kul Tiran", "Lightforged Draenei", "Void Elf",
                      "Draenei", "Dwarf", "Gnome", "Human", "Night Elf", "Worgen", "Pandaren",
                      "Mechagnome"]
mage_race_horde = ["Mag'har Orc", "Nightborne", "Zandalari Troll", "Blood Elf", "Goblin",
                   "Orc", "Troll", "Undead", "Pandaren", "Vulpera"]
# Warlock Races
warlock_race_alliance = ["Dark Iron Dwarf", "Void Elf", "Dwarf", "Gnome", "Human", "Worgen",
                         "Mechagnome"]
warlock_race_horde = ["Nightborne", "Blood Elf", "Goblin", "Orc", "Troll", "Undead", "Vulpera"]

# Monk Races
monk_race_alliance = ["Dark Iron Dwarf", "Kul Tiran", "Void Elf", "Draenei", "Dwarf", "Gnome",
                      "Human", "Night Elf", "Pandaren", "Mechagnome"]
monk_race_horde = ["Highmountain Tauren", "Mag'har Orc", "Nightborne", "Zandalari Troll",
                   "Blood Elf", "Orc", "Tauren", "Troll", "Undead", "Pandaren", "Vulpera"]
# Druid Races
druid_race_alliance = ["Kul Tiran", "Night Elf", "Worgen"]
druid_race_horde = ["Highmountain Tauren", "Zandalari Troll", "Tauren", "Troll"]

# Demon Hunter Races
dh_race_alliance = ["Night Elf"]
dh_race_horde = ["Blood Elf"]

# Assigning race list with the class
race_list = []

if final_class == "Warrior":
    if user_faction.lower() == "alliance":
        race_list = warrior_race_alliance
    else:
        race_list = warrior_race_horde
elif final_class == "Paladin":
    if user_faction.lower() == "alliance":
        race_list = paladin_race_alliance
    else:
        race_list = paladin_race_horde
elif final_class == "Hunter":
    if user_faction.lower() == "alliance":
        race_list = hunter_race_alliance
    else:
        user_faction = hunter_race_horde
elif final_class == "Rogue":
    if user_faction.lower() == "alliance":
        race_list = rogue_race_alliance
    else:
        race_list = rogue_race_horde
elif final_class == "Priest":
    if user_faction.lower() == "alliance":
        race_list = priest_race_alliance
    else:
        race_list = priest_race_horde
elif final_class == "Death Knight":
    if user_faction.lower() == "alliance":
        race_list = dk_race_alliance
    else:
        race_list = dk_race_horde
elif final_class == "Shaman":
    if user_faction.lower() == "alliance":
        race_list = shaman_race_alliance
    else:
        race_list = shaman_race_horde
elif final_class == "Mage":
    if user_faction.lower() == "alliance":
        race_list = mage_race_alliance
    else:
        race_list = mage_race_horde
elif final_class == "Warlock":
    if user_faction.lower() == "alliance":
        race_list = warlock_race_alliance
    else:
        race_list = warlock_race_horde
elif final_class == "Monk":
    if user_faction.lower() == "alliance":
        race_list = monk_race_alliance
    else:
        race_list = monk_race_horde
elif final_class == "Druid":
    if user_faction.lower() == "alliance":
        race_list = druid_race_alliance
    else:
        race_list = druid_race_horde
elif final_class == "Demon Hunter":
    if user_faction.lower() == "alliance":
        race_list = dh_race_alliance
    else:
        race_list = dh_race_horde
else:
    pass


# (final_class)
# (race_list)

# Removing Allied races if user did not want/have them
if allied_avail.lower() == "n":
    if "Dark Iron Dwarf" in race_list:
        race_list.remove("Dark Iron Dwarf")
if allied_avail.lower() == "n":
    if "Kul Tiran" in race_list:
        race_list.remove("Kul Tiran")
if allied_avail.lower() == "n":
    if "Lightforged Draenei" in race_list:
        race_list.remove("Lightforged Draenei")
if allied_avail.lower() == "n":
    if "Void Elf" in race_list:
        race_list.remove("Void Elf")
if allied_avail.lower() == "n":
    if "Highmountain Tauren" in race_list:
        race_list.remove("Highmountain Tauren")
if allied_avail.lower() == "n":
    if "Mag'har Orc" in race_list:
        race_list.remove("Mag'har Orc")
if allied_avail.lower() == "n":
    if "Nightborne" in race_list:
        race_list.remove("Nightborne")
if allied_avail.lower() == "n":
    if "Zandalari Troll" in race_list:
        race_list.remove("Zandalari Troll")
if allied_avail.lower() == "n":
    if "Mechagnome" in race_list:
        race_list.remove("Mechagnome")
if allied_avail.lower() == "n":
    if "Vulpera" in race_list:
        race_list.remove("Vulpera")

# Removing ones not available if some were
if dark_iron_avail.lower() == "n":
    if "Dark Iron Dwarf" in race_list:
        race_list.remove("Dark Iron Dwarf")
if kultiran_avail.lower() == "n":
    if "Kul Tiran" in race_list:
        race_list.remove("Kul Tiran")
if lightforged_avail.lower() == "n":
    if "Lightforged Draenei" in race_list:
        race_list.remove("Lightforged Draenei")
if void_avail.lower() == "n":
    if "Void Elf" in race_list:
        race_list.remove("Void Elf")
if highmountain_avail.lower() == "n":
    if "Highmountain Tauren" in race_list:
        race_list.remove("Highmountain Tauren")
if maghar_avail.lower() == "n":
    if "Mag'har Orc" in race_list:
        race_list.remove("Mag'har Orc")
if nightborne_avail.lower() == "n":
    if "Nightborne" in race_list:
        race_list.remove("Nightborne")
if zandalari_avail.lower() == "n":
    if "Zandalari Troll" in race_list:
        race_list.remove("Zandalari Troll")
if mecha_avail.lower() == "n":
    if "Mechagnome" in race_list:
        race_list.remove("Mechagnome")
if vulpera_avail.lower() == "n":
    if "Vulpera" in race_list:
        race_list.remove("Vulpera")

random_race = random.choice(race_list)
random_gender = random.choice(gender)

print("Faction: " + user_faction)
print("Race: " + random_race)
print("Gender: " + random_gender)
print("Class: " + final_class)
if random_spec.lower() == "y":
    print("Specialization: " + final_spec)
if random_server_pref.lower() == "y":
    print("Server: " + random_server)
