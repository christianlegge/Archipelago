from typing import Dict, Set, Tuple, NamedTuple

class ItemData(NamedTuple):
	category: str
	code: int
	progression: bool = False
	useful: bool = False
	trap: bool = False
	count: int = 1

item_table: Dict[str, ItemData] = {
	'Leather Whip': 					ItemData('MainWeapon', 2359000, progression=True, count=0), #Cannot be sent, only as a starting item
	'Chain Whip': 						ItemData('MainWeapon', 2359001, progression=True),
	'Flail Whip': 						ItemData('MainWeapon', 2359002, progression=True),
	#gonna reserve 2359003 in case we ever implement progressive whips
	'Knife': 							ItemData('MainWeapon', 2359004, progression=True),
	'Key Sword': 						ItemData('MainWeapon', 2359005, progression=True),
	'Axe':								ItemData('MainWeapon', 2359006, progression=True),
	'Katana': 							ItemData('MainWeapon', 2359007, progression=True),
	'Shuriken': 						ItemData('Subweapon', 2359008, progression=True),
	'Rolling Shuriken': 				ItemData('Subweapon', 2359009, progression=True),
	'Earth Spear': 						ItemData('Subweapon', 2359010, progression=True),
	'Flare Gun': 						ItemData('Subweapon', 2359011, progression=True),
	'Bomb': 							ItemData('Subweapon', 2359012, progression=True),
	'Chakram': 							ItemData('Subweapon', 2359013, progression=True),
	'Caltrops': 						ItemData('Subweapon', 2359014, progression=True),
	'Pistol': 							ItemData('Subweapon', 2359015, progression=True),
	'Buckler': 							ItemData('Subweapon', 2359016, useful=True),
	'Fake Silver Shield':				ItemData('Subweapon', 2359017),
	'Silver Shield': 					ItemData('Subweapon', 2359018, progression=True),
	'Angel Shield': 					ItemData('Subweapon', 2359019, progression=True),
	'Ankh Jewel': 						ItemData('Subweapon', 2359020, progression=True, count=8), #Change count to 9 if alt mother ankh
	'Hand Scanner':						ItemData('Usable', 2359021, progression=True),
	'Djed Pillar':						ItemData('Usable', 2359022, progression=True),
	'Mini Doll':						ItemData('Usable', 2359023, progression=True),
	'Magatama Jewel':					ItemData('Usable', 2359024, progression=True),
	'Cog of the Soul':					ItemData('Usable', 2359025, progression=True),
	'Lamp of Time':						ItemData('Usable', 2359026, progression=True),
	'Pochette Key':						ItemData('Usable', 2359027, progression=True),
	'Dragon Bone':						ItemData('Usable', 2359028, progression=True),
	'Crystal Skull':					ItemData('Usable', 2359029, progression=True),
	'Vessel':							ItemData('Usable', 2359030, progression=True),
	'Pepper':							ItemData('Usable', 2359031, progression=True),
	'Woman Statue':						ItemData('Usable', 2359032, progression=True),
	'Maternity Statue':					ItemData('Usable', 2359033, progression=True, count=0), #Optionally swap counts with woman statue
	'Key of Eternity':					ItemData('Usable', 2359034, progression=True),
	'Serpent Staff':					ItemData('Usable', 2359035, progression=True),
	'Talisman':							ItemData('Usable', 2359036, progression=True),
	'Diary':							ItemData('Usable', 2359037, progression=True),
	'Mulana Talisman':					ItemData('Usable', 2359038, progression=True),
	'Waterproof Case':					ItemData('Inventory', 2359039, useful=True),
	'Heatproof Case':					ItemData('Inventory', 2359040, useful=True),
	'Shell Horn':						ItemData('Inventory', 2359041, useful=True),
	'Glove':							ItemData('Inventory', 2359042, useful=True),
	'Holy Grail':						ItemData('Inventory', 2359043, progression=True),
	'Isis\' Pendant':					ItemData('Inventory', 2359044, progression=True),
	'Crucifix':							ItemData('Inventory', 2359045, useful=True),
	'Helmet':							ItemData('Inventory', 2359046, progression=True),
	'Grapple Claw':						ItemData('Inventory', 2359047, progression=True),
	'Bronze Mirror':					ItemData('Inventory', 2359048, progression=True),
	'Eye of Truth':						ItemData('Inventory', 2359049, progression=True),
	'Ring':								ItemData('Inventory', 2359050, progression=True),
	'Scalesphere':						ItemData('Inventory', 2359051, progression=True),
	'Gauntlet':							ItemData('Inventory', 2359052, useful=True),
	'Anchor':							ItemData('Inventory', 2359053, progression=True),
	'Plane Model':						ItemData('Inventory', 2359054, progression=True),
	'Philosopher\'s Ocarina': 			ItemData('Inventory', 2359055, progression=True),
	'Feather':							ItemData('Inventory', 2359056, progression=True),
	'Book of the Dead':					ItemData('Inventory', 2359057, progression=True),
	'Fairy Clothes':					ItemData('Inventory', 2359058, useful=True),
	'Scriptures':						ItemData('Inventory', 2359059, useful=True),
	'Hermes\' Boots':					ItemData('Inventory', 2359060, progression=True),
	'Fruit of Eden':					ItemData('Inventory', 2359061, progression=True),
	'Twin Statue':						ItemData('Inventory', 2359062, progression=True),
	'Bracelet':							ItemData('Inventory', 2359063, useful=True),
	'Perfume':							ItemData('Inventory', 2359064, useful=True),
	'Spaulder':							ItemData('Inventory', 2359065),
	'Dimensional Key':					ItemData('Inventory', 2359066, progression=True),
	'Ice Cape':							ItemData('Inventory', 2359067, progression=True),
	'Origin Seal':						ItemData('Inventory', 2359068, progression=True),
	'Birth Seal':						ItemData('Inventory', 2359069, progression=True),
	'Life Seal':						ItemData('Inventory', 2359070, progression=True),
	'Death Seal':						ItemData('Inventory', 2359071, progression=True),
	'Sacred Orb':						ItemData('Inventory', 2359072, progression=True, count=10),
	'Treasures': 						ItemData('Inventory', 2359073, progression=True),
	'Mobile Super X2':					ItemData('Inventory', 2359074, useful=True),
	'Provocative Bathing Suit':			ItemData('Inventory', 2359075),
	'reader.exe':						ItemData('Software', 2359076, progression=True),
	'xmailer.exe':						ItemData('Software', 2359077),
	'yagomap.exe':						ItemData('Software', 2359078, progression=True),
	'yagostr.exe':						ItemData('Software', 2359079, progression=True),
	'bunemon.exe':						ItemData('Software', 2359080, useful=True),
	'bunplus.exe':						ItemData('Software', 2359081),
	'torude.exe':						ItemData('Software', 2359082, progression=True),
	'guild.exe':						ItemData('Software', 2359083, progression=True), #progression only if Hell Temple on
	'mantra.exe':						ItemData('Software', 2359084, progression=True),
	'emusic.exe':						ItemData('Software', 2359085),
	'beolamu.exe':						ItemData('Software', 2359086),
	'deathv.exe':						ItemData('Software', 2359087, useful=True),
	'randc.exe':						ItemData('Software', 2359088, useful=True),
	'capstar.exe':						ItemData('Software', 2359089),
	'move.exe':							ItemData('Software', 2359090, useful=True),
	'mekuri.exe':						ItemData('Software', 2359091, progression=True), #progression if key fairy combo
	'miracle.exe':						ItemData('Software', 2359092, progression=True), #progression if key fairy combo or NPC rando
	'mirai.exe':						ItemData('Software', 2359093, progression=True),
	'lamulana.exe':						ItemData('Software', 2359094, useful=True),
	#Small gap in IDs
	'Map (Gate of Guidance)': 			ItemData('Map', 2359100),
	'Map (Mausoleum of the Giants)':	ItemData('Map', 2359101),
	'Map (Temple of the Sun)':			ItemData('Map', 2359102),
	'Map (Spring in the Sky)':			ItemData('Map', 2359103),
	'Map (Inferno Cavern)':				ItemData('Map', 2359104),
	'Map (Chamber of Extinction)':		ItemData('Map', 2359105),
	'Map (Twin Labyrinths)':			ItemData('Map', 2359106),
	'Map (Endless Corridor)':			ItemData('Map', 2359107),
	'Map (Shrine of the Mother)':		ItemData('Map', 2359108, progression=True),
	'Map (Gate of Illusion)':			ItemData('Map', 2359109),
	'Map (Graveyard of the Giants)':	ItemData('Map', 2359110),
	'Map (Temple of Moonlight)':		ItemData('Map', 2359111),
	'Map (Tower of the Goddess)':		ItemData('Map', 2359112),
	'Map (Tower of Ruin)':				ItemData('Map', 2359113),
	'Map (Chamber of Birth)':			ItemData('Map', 2359114),
	'Map (Dimensional Corridor)':		ItemData('Map', 2359115),
	'Shuriken Ammo':					ItemData('ShopInventory', 2359116, count=0, progression=True),
	'Rolling Shuriken Ammo':			ItemData('ShopInventory', 2359117, count=0, progression=True),
	'Earth Spear Ammo':					ItemData('ShopInventory', 2359118, count=0, progression=True),
	'Flare Gun Ammo':					ItemData('ShopInventory', 2359119, count=0, progression=True),
	'Bomb Ammo':						ItemData('ShopInventory', 2359120, count=0, progression=True),
	'Chakram Ammo':						ItemData('ShopInventory', 2359121, count=0, progression=True),
	'Caltrops Ammo':					ItemData('ShopInventory', 2359122, count=0, progression=True),
	'Pistol Ammo':						ItemData('ShopInventory', 2359123, count=0, progression=True),
	'5 Weights':						ItemData('ShopInventory', 2359124, count=0),
	'200 coins':						ItemData('Resource', 2359125, count=0), #Escape chest is 200 right?
	'100 coins':						ItemData('Resource', 2359126, count=0), #Adjust counts if money chests shuffled, have various distributions depending on total item pool minus starting item count
	'50 coins':							ItemData('Resource', 2359127, count=0),
	'30 coins':							ItemData('Resource', 2359128, count=0),
	'10 coins':							ItemData('Resource', 2359129, count=0),
	'1 Weight':							ItemData('Resource', 2359130, count=0),
	#Gap in IDs for other possible items in pool before trap items
	'Bat Trap':							ItemData('Trap', 2359150, trap=True, count=0),
	'Explosive Trap':					ItemData('Trap', 2359151, trap=True, count=0),
}

shop_inventory_codes: Set[int] = {2359116, 2359117, 2359118, 2359119, 2359120, 2359121, 2359122, 2359123, 2359124}

def get_items_by_category():
	categories: Dict[str, Set[str]] = {}
	for name, data in item_table.items():
		categories.setdefault(data.category, set()).add(name)
	return categories