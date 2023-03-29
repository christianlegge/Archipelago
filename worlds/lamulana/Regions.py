from typing import List, Set, Dict, Tuple, Optional, Callable
from BaseClasses import MultiWorld, Region, Entrance, Location
from .Options import is_option_enabled, get_option_value
from .Locations import get_locations_by_region
from .NPCs import LaMulanaNPCDoor, get_npcs

def create_regions_and_locations(world: MultiWorld, player: int):
	s = LaMulanaLogicShortcuts(world, player)

	locations = get_locations_by_region(world, player, s)
	npcs = get_npcs(world, player, s)

	regions = [
		create_region(world, player, "Menu", locations, npcs),
		create_region(world, player, "Surface [Main]", locations, npcs),
		create_region(world, player, "Surface [Ruin Path Upper]", locations, npcs),
		create_region(world, player, "Surface [Ruin Path Lower]", locations, npcs),
		create_region(world, player, "Gate of Guidance [Main]", locations, npcs),
		create_region(world, player, "Gate of Guidance [Door]", locations, npcs),
		create_region(world, player, "Gate of Illusion [Eden]", locations, npcs),
		create_region(world, player, "Gate of Illusion [Lower]", locations, npcs),
		create_region(world, player, "Gate of Illusion [Middle]", locations, npcs),
		create_region(world, player, "Gate of Illusion [Dracuet]", locations, npcs),
		create_region(world, player, "Gate of Illusion [Grail]", locations, npcs),
		create_region(world, player, "Gate of Illusion [Ruin]", locations, npcs),
		create_region(world, player, "Gate of Illusion [Upper]", locations, npcs),
		create_region(world, player, "Gate of Illusion [Pot Room]", locations, npcs),
		create_region(world, player, "Mausoleum of the Giants", locations, npcs),
		create_region(world, player, "Graveyard of the Giants [West]", locations, npcs),
		create_region(world, player, "Graveyard of the Giants [Grail]", locations, npcs),
		create_region(world, player, "Graveyard of the Giants [East]", locations, npcs),
		create_region(world, player, "Temple of the Sun [Top Entrance]", locations, npcs),
		create_region(world, player, "Temple of the Sun [Grail]", locations, npcs),
		create_region(world, player, "Temple of the Sun [Main]", locations, npcs),
		create_region(world, player, "Temple of the Sun [West]", locations, npcs),
		create_region(world, player, "Temple of the SUn [East]", locations, npcs),
		create_region(world, player, "Temple of the Sun [Sphinx]", locations, npcs),
		create_region(world, player, "Temple of Moonlight [Pyramid]", locations, npcs),
		create_region(world, player, "Temple of Moonlight [Upper]", locations, npcs),
		create_region(world, player, "Temple of Moonlight [Lower]", locations, npcs),
		create_region(world, player, "Temple of Moonlight [Eden]", locations, npcs),
		create_region(world, player, "Temple of Moonlight [Grail]", locations, npcs),
		create_region(world, player, "Temple of Moonlight [Grapple]", locations, npcs),
		create_region(world, player, "Temple of Moonlight [Map]", locations, npcs),
		create_region(world, player, "Temple of Moonlight [Southeast]", locations, npcs),
		create_region(world, player, "Spring in the Sky [Main]", locations, npcs),
		create_region(world, player, "Spring in the Sky [Upper]", locations, npcs),
		create_region(world, player, "Tower of the Goddess [Lower]", locations, npcs),
		create_region(world, player, "Tower of the Goddess [Lamp]", locations, npcs),
		create_region(world, player, "Tower of the Goddess [Grail]", locations, npcs),
		create_region(world, player, "Tower of the Goddess [Spaulder]", locations, npcs),
		create_region(world, player, "Tower of the Goddess [Shield Statue]", locations, npcs),
		create_region(world, player, "Inferno Cavern [Main]", locations, npcs),
		create_region(world, player, "Inferno Cavern [Pazuzu]", locations, npcs),
		create_region(world, player, "Inferno Cavern [Viy]", locations, npcs),
		create_region(world, player, "Inferno Cavern [Lava]", locations, npcs),
		create_region(world, player, "Inferno Cavern [Spikes]", locations, npcs),
		create_region(world, player, "Tower of Ruin [Southeast]", locations, npcs),
		create_region(world, player, "Tower of Ruin [Southwest]", locations, npcs),
		create_region(world, player, "Tower of Ruin [Southwest Door]", locations, npcs),
		create_region(world, player, "Tower of Ruin [La-Mulanese]", locations, npcs),
		create_region(world, player, "Tower of Ruin [Illusion]", locations, npcs),
		create_region(world, player, "Tower of Ruin [Grail]", locations, npcs),
		create_region(world, player, "Tower of Ruin [Spirits]", locations, npcs),
		create_region(world, player, "Tower of Ruin [Medicine]", locations, npcs),
		create_region(world, player, "Tower of Ruin [Top]", locations, npcs),
		create_region(world, player, "Chamber of Extinction [Map]", locations, npcs),
		create_region(world, player, "Chamber of Extinction [Main]", locations, npcs),
		create_region(world, player, "Chamber of Extinction [Left Main]", locations, npcs),
		create_region(world, player, "Chamber of Extinction [Teleport]", locations, npcs),
		create_region(world, player, "Chamber of Extinction [Magatama Left]", locations, npcs),
		create_region(world, player, "Chamber of Extinction [Magatama Right]", locations, npcs),
		create_region(world, player, "Chamber of Extinction [Magatama]", locations, npcs),
		create_region(world, player, "Chamber of Extinction [Ankh Upper]", locations, npcs),
		create_region(world, player, "Chamber of Extinction [Ankh Lower]", locations, npcs),
		create_region(world, player, "Chamber of Birth [West Entrance]", locations, npcs),
		create_region(world, player, "Chamber of Birth [West]", locations, npcs),
		create_region(world, player, "Chamber of Birth [Grail]", locations, npcs),
		create_region(world, player, "Chamber of Birth [Skanda]", locations, npcs),
		create_region(world, player, "Chamber of Birth [Dance]", locations, npcs),
		create_region(world, player, "Chamber of Birth [Northeast]", locations, npcs),
		create_region(world, player, "Chamber of Birth [Southeast]", locations, npcs),
		create_region(world, player, "Twin Labyrinths [Loop]", locations, npcs),
		create_region(world, player, "Twin Labyrinths [Lower]", locations, npcs),
		create_region(world, player, "Twin Labyrinths [Poison 1]", locations, npcs),
		create_region(world, player, "Twin Labyrinths [Poison 2]", locations, npcs),
		create_region(world, player, "Twin Labyrinths [Upper Grail]", locations, npcs),
		create_region(world, player, "Twin Labyrinths [Jewel]", locations, npcs),
		create_region(world, player, "Twin Labyrinths [Katana]", locations, npcs),
		create_region(world, player, "Twin Labyrinths [Poseidon]", locations, npcs),
		create_region(world, player, "Twin Labyrinths [Upper Left]", locations, npcs),
		create_region(world, player, "Endless Corridor [1F]", locations, npcs),
		create_region(world, player, "Endless Corridor [2F]", locations, npcs),
		create_region(world, player, "Endless Corridor [3F Upper]", locations, npcs),
		create_region(world, player, "Endless Corridor [3F Lower]", locations, npcs),
		create_region(world, player, "Endless Corridor [4F]", locations, npcs),
		create_region(world, player, "Endless Corridor [5F]", locations, npcs),
		create_region(world, player, "Dimensional Corridor [Lower]", locations, npcs),
		create_region(world, player, "Dimensional Corridor [Grail]", locations, npcs),
		create_region(world, player, "Dimensional Corridor [Upper]", locations, npcs),
		create_region(world, player, "Shrine of the Mother [Main]", locations, npcs),
		create_region(world, player, "Shrine of the Mother [Lower]", locations, npcs),
		create_region(world, player, "Shrine of the Mother [Seal]", locations, npcs),
		create_region(world, player, "Shrine of the Mother [Map]", locations, npcs),
		create_region(world, player, "True Shrine of the Mother", locations, npcs),
		create_region(world, player, "Gate of Time [Mausoleum Lower]", locations, npcs),
		create_region(world, player, "Gate of Time [Mausoleum Upper]", locations, npcs),
		create_region(world, player, "Gate of Time [Guidance]", locations, npcs),
		create_region(world, player, "Gate of Time [Surface]", locations, npcs),
	]

	if get_option_value(world, player, "ProvocativeBathingSuit") == 2 or is_option_enabled(world, player, "RandomizeDracuetsShop"):
		regions.extend([
			create_region(world, player, "Hell Temple [Entrance]", locations, npcs),
			create_region(world, player, "Hell Temple [Shop]", locations, npcs),
			create_region(world, player, "Hell Temple [Dracuet]", locations, npcs),
		])

	world.regions += regions

	#Internal connections within fields that don't change with ER
	connect(world, player, 'Surface [Main]', 'Surface [Ruin Path Lower]', lambda state: s.glitch_raindrop(state))
	connect(world, player, 'Surface [Ruin Path Upper]', 'Surface [Ruin Path Lower]', lambda state: state.has_any({'Feather', 'Holy Grail'}, player))
	connect(world, player, 'Surface [Ruin Path Lower]', 'Surface [Ruin Path Upper]', lambda state: state.has('Feather', player))

	connect(world, player, 'Gate of Guidance [Door]', 'Gate of Guidance [Main]')

	connect(world, player, 'Gate of Illusion [Grail]', 'Gate of Illusion [Eden]', lambda state: state.has('Holy Grail', player))
	connect(world, player, 'Gate of Illusion [Eden]', 'Gate of Illusion [Lower]', lambda state: state.has('Illusion Unlocked', player))
	connect(world, player, 'Gate of Illusion [Dracuet]', 'Gate of Illusion [Lower]', lambda state: state.has_any({'Hand Scanner', 'Holy Grail'}, player) or s.glitch_raindrop(state))
	connect(world, player, 'Gate of Illusion [Lower]', 'Gate of Illusion [Dracuet]', lambda state: state.has('Hand Scanner', player) or s.glitch_raindrop(state))
	connect(world, player, 'Gate of Illusion [Grail]', 'Gate of Illusion [Middle]', lambda state: s.glitch_lamp(state))
	connect(world, player, 'Gate of Illusion [Dracuet]', 'Gate of Illusion [Middle]', lambda state: (s.attack_far(state) or s.attack_bomb(state)) and state.has_all({'Illusion Unlocked', 'Anchor'}, player))
	connect(world, player, 'Gate of Illusion [Middle]', 'Gate of Illusion [Dracuet]', lambda state: state.has('Holy Grail', player) or (state.has_all({'Illusion Unlocked', 'Anchor'}, player) and s.attack_chest(state))) #Puzzle solves itself when you go backwards, so backtracking doesn't require attack-far
	connect(world, player, 'Gate of Illusion [Middle]', 'Gate of Illusion [Grail]')
	connect(world, player, 'Gate of Illusion [Upper]', 'Gate of Illusion [Grail]', lambda state: state.has('Holy Grail', player))
	connect(world, player, 'Gate of Illusion [Ruin]', 'Gate of Illusion [Grail]', lambda state: state.has('Birth Seal', player))
	connect(world, player, 'Gate of Illusion [Grail]', 'Gate of Illusion [Ruin]', lambda state: state.has_any({'Holy Grail', 'Birth Seal'}, player))
	connect(world, player, 'Gate of Illusion [Grail]', 'Gate of Illusion [Pot Room]', lambda state: s.glitch_raindrop(state))
	connect(world, player, 'Gate of Illusion [Pot Room]', 'Gate of Illusion [Upper]', lambda state: state.has('Feather', player))

	connect(world, player, 'Graveyard of the Giants [West]', 'Graveyard of the Giants [Grail]', lambda state: state.has('Feather', player))
	connect(world, player, 'Graveyard of the Giants [Grail]', 'Graveyard of the Giants [West]', lambda state: state.has_any({'Holy Grail', 'Feather'}, player))
	connect(world, player, 'Graveyard of the Giants [West]', 'Graveyard of the Giants [East]', lambda state: s.attack_bomb(state) and state.has('Ring', player))
	connect(world, player, 'Graveyard of the Giants [East]', 'Graveyard of the Giants [West]', lambda state: s.attack_bomb(state))

	connect(world, player, 'Temple of the Sun [Grail]', 'Temple of the Sun [Top Entrance]', lambda state: state.has("Hermes' Boots", player) or s.sun_watchtower(state))
	connect(world, player, 'Temple of the Sun [Top Entrance]', 'Temple of the Sun [Grail]', lambda state: state.has_any({'Holy Grail', "Hermes' Boots"}, player) or s.sun_watchtower(state))
	connect(world, player, 'Temple of the Sun [Top Entrance]', 'Temple of the Sun [West]', lambda state: s.sun_watchtower(state) and (s.attack_main(state) or state.has_any({'Grapple Claw', 'Feather'}, player)))
	connect(world, player, 'Temple of the Sun [Top Entrance]', 'Temple of the Sun [Main]', lambda state: state.has('Holy Grail', player) or s.sun_watchtower(state))
	connect(world, player, 'Temple of the Sun [West]', 'Temple of the Sun [Top Entrance]', lambda state: state.has('Buer Defeated', player) and s.sun_watchtower(state))
	connect(world, player, 'Temple of the Sun [Main]', 'Temple of the Sun [Top Entrance]', lambda state: s.sun_watchtower(state))
	connect(world, player, 'Temple of the Sun [Main]', 'Temple of the Sun [East]', lambda state: state.has("Hermes' Boots", player))
	connect(world, player, 'Temple of the Sun [Main]', 'Temple of the Sun [Sphinx]', lambda state: state.has_all({"Hermes' Boots", 'Feather'}, player))
	connect(world, player, 'Temple of the Sun [East]', 'Temple of the Sun [Main]', lambda state: state.has_any({'Holy Grail', "Hermes' Boots"}, player))
	connect(world, player, 'Temple of the Sun [Main]', 'Temple of Moonlight [Pyramid]', lambda state: state.has('Holy Grail', state) and (s.attack_above(state) or s.attack_s_above(state)))

	connect(world, player, 'Temple of the Moonlight [Pyramid]', 'Temple of Moonlight [Upper]')
	connect(world, player, 'Temple of the Moonlight [Pyramid]', 'Temple of Moonlight [Lower]', lambda state: s.glitch_raindrop(state))
	connect(world, player, 'Temple of the Moonlight [Upper]', 'Temple of Moonlight [Pyramid]', lambda state: s.glitch_raindrop(state))
	connect(world, player, 'Temple of the Moonlight [Lower]', 'Temple of Moonlight [Upper]', lambda state: s.attack_caltrops(state) or s.attack_shuriken(state) or s.attack_rolling_shuriken(state) or s.attack_chakram(state) or s.attack_bomb(state) or s.attack_pistol(state))
	connect(world, player, 'Temple of the Moonlight [Upper]', 'Temple of Moonlight [Eden]', lambda state: (s.attack_forward(state) or s.attack_flare_gun(state)) and (state.has('Holy Grail', player) or s.attack_chest(state)))
	connect(world, player, 'Temple of the Moonlight [Eden]', 'Temple of Moonlight [Upper]', lambda state: s.attack_chest(state))
	connect(world, player, 'Temple of the Moonlight [Eden]', 'Temple of Moonlight [Grail]', lambda state: s.attack_chest(state) and (state.has('Holy Grail', player) or s.attack_flare_gun(state)))
	connect(world, player, 'Temple of the Moonlight [Eden]', 'Temple of Moonlight [Grapple]', lambda state: state.has_any({'Holy Grail', 'Feather'}, player) or s.attack_chest(state))
	connect(world, player, 'Temple of the Moonlight [Grapple]', 'Temple of Moonlight [Map]')
	connect(world, player, 'Temple of the Moonlight [Lower]', 'Temple of Moonlight [Southeast]', lambda state: (state.has('Birth Seal', player) or s.glitch_raindrop(state)) and (s.attack_forward(state) or s.attack_flare_gun(state)))
	connect(world, player, 'Temple of the Moonlight [Grail]', 'Temple of Moonlight [Eden]', lambda state: s.attack_forward(state) or s.attack_vertical(state) or (s.attack_earth_spear(state) and state.has('Holy Grail', player)))

	connect(world, player, 'Spring in the Sky [Main]', 'Spring in the Sky [Upper]', lambda state: state.has('Helmet', player))
	connect(world, player, 'Spring in the Sky [Upper]', 'Surface [Main]', lambda state: state.has('Holy Grail', player) and (state.has('Bahamut Defeated', player) or s.glitch_lamp(state)))

	connect(world, player, 'Tower of the Goddess [Grail]', 'Tower of the Goddess [Lower]', lambda state: state.has_any({'Holy Grail', 'Feather'}, player))
	connect(world, player, 'Tower of the Goddess [Lamp]', 'Tower of the Goddess [Lower]', lambda state: s.attack_forward(state) or state.has_all({'Feather', 'Holy Grail'}, player))
	connect(world, player, 'Tower of the Goddess [Lower]', 'Tower of the Goddess [Lamp]', lambda state: state.has('Flooded Tower of the Goddess', player) and state.has_any({'Holy Grail', 'Anchor'}, player))
	connect(world, player, 'Tower of the Goddess [Lower]', 'Tower of the Goddess [Grail]', lambda state: state.has('Feather', player))
	connect(world, player, 'Tower of the Goddess [Grail]', 'Tower of the Goddess [Shield Statue]', lambda state: state.has('Plane Model', player))
	connect(world, player, 'Tower of the Goddess [Grail]', 'Tower of the Goddess [Spaulder]', lambda state: s.attack_forward(state))
	connect(world, player, 'Tower of the Goddess [Spaulder]', 'Tower of the Goddess [Grail]', lambda state: state.has('Holy Grail', player) or s.attack_forward(state))

	connect(world, player, 'Inferno Cavern [Viy]', 'Inferno Cavern [Main]', lambda state: s.state_lava_swim(state, 3) and (s.attack_forward(state) or s.glitch_catpause(state)))
	connect(world, player, 'Inferno Cavern [Main]', 'Inferno Cavern [Viy]', lambda state: s.glitch_lamp(state) and s.attack_forward(state) and (state.has('Holy Grail', player) or s.state_lava_swim(state, 3)))
	connect(world, player, 'Inferno Cavern [Lava]', 'Inferno Cavern [Main]', lambda state: state.has('Holy Grail', player) and s.state_lava_swim(state, 2))
	connect(world, player, 'Inferno Cavern [Viy]', 'Chamber of Extinction [Ankh Upper]', lambda state: state.has_all({'Viy Defeated', 'Holy Grail'}, player))

	connect(world, player, 'Tower of Ruin [Southeast]', 'Tower of Ruin [Southwest]', lambda state: s.state_mobility(state) or s.state_lava_swim(state, 1))
	connect(world, player, 'Tower of Ruin [Southwest]', 'Tower of Ruin [Southeast]', lambda state: s.state_mobility(state) or s.state_lava_swim(state, 1))
	connect(world, player, 'Tower of Ruin [Grail]', 'Tower of Ruin [Southwest]', lambda state: state.has('Holy Grail', player))
	connect(world, player, 'Tower of Ruin [Southwest]', 'Tower of Ruin [Southwest Door]', lambda state: s.attack_earth_spear(state) or s.glitch_raindrop(state))
	connect(world, player, 'Tower of Ruin [Southwest]', 'Tower of Ruin [La-Mulanese]', lambda state: state.has_all({'Thunderbird Defeated', 'Feather'}, player))
	connect(world, player, 'Tower of Ruin [Southwest]', 'Tower of Ruin [Grail]', lambda state: state.has_all({'Thunderbird Defeated', 'Feather'}, player) and s.attack_forward(state))
	connect(world, player, 'Tower of Ruin [Illusion]', 'Tower of Ruin [Grail]', lambda state: s.attack_forward(state))
	connect(world, player, 'Tower of Ruin [Spirits]', 'Tower of Ruin [Grail]', lambda state: state.has('Holy Grail', player))
	connect(world, player, 'Tower of Ruin [Medicine]', 'Tower of Ruin [Spirits]', lambda state: s.state_lava_swim(state, 3) and (state.has('Holy Grail', player) or s.state_lava_swim(state, 5)))
	connect(world, player, 'Tower of Ruin [Top]', 'Tower of Ruin [Medicine]', lambda state: state.has('Holy Grail', player))

	connect(world, player, 'Chamber of Extinction [Left Main]', 'Chamber of Extinction [Map]', lambda state: s.state_extinction_light(state) and s.glitch_raindrop(state))
	connect(world, player, 'Chamber of Extinction [Map]', 'Chamber of Extinction [Main]', lambda state: s.state_extinction_light(state) and state.has('Holy Grail', player))
	connect(world, player, 'Chamber of Extinction [Left Main]', 'Chamber of Extinction [Main]', lambda state: s.state_extinction_light(state) and state.has('Feather', player))
	connect(world, player, 'Chamber of Extinction [Main]', 'Chamber of Extinction [Left Main]', lambda state: s.state_extinction_light(state) and state.has_any({'Holy Grail', 'Feather'}, player))
	connect(world, player, 'Chamber of Extinction [Magatama Left]', 'Chamber of Extinction [Left Main]', lambda state: s.glitch_raindrop(state) and s.state_extinction_light(state))
	connect(world, player, 'Chamber of Extinction [Ankh Upper]', 'Chamber of Extinction [Teleport]', lambda state: s.glitch_raindrop(state))
	connect(world, player, 'Chamber of Birth [Southeast]', 'Chamber of Extinction [Teleport]', lambda state: s.attack_forward(state) and state.has('Feather', player))
	connect(world, player, 'Chamber of Birth [Northeast]', 'Chamber of Extinction [Map]', lambda state: s.glitch_raindrop(state) and s.attack_forward(state))
	connect(world, player, 'Chamber of Extinction [Teleport]', 'Chamber of Birth [Northeast]', lambda state: state.has('Feather', player))
	connect(world, player, 'Chamber of Extinction [Magatama Left]', 'Chamber of Extinction [Magatama]', lambda state: state.has_any({'Holy Grail', 'Feather'}, player) or s.attack_forward(state))
	connect(world, player, 'Chamber of Extinction [Magatama]', 'Chamber of Extinction [Magatama Left]', lambda state: state.has('Ox-head & Horse-face Defeated', player))
	connect(world, player, 'Chamber of Extinction [Magatama]', 'Chamber of Extinction [Magatama Right]', lambda state: state.has('Ox-head & Horse-face Defeated', player))
	connect(world, player, 'Chamber of Extinction [Magatama Right]', 'Chamber of Extinction [Magatama]', lambda state: state.has('Holy Grail', player) or (s.attack_chest(state) and state.has('Feather', player)))
	connect(world, player, 'Chamber of Extinction [Ankh Upper]', 'Chamber of Extinction [Ankh Lower]', lambda state: state.has_any({'Holy Grail', 'Feather'}, player))
	connect(world, player, 'Chamber of Extinction [Ankh Lower]', 'Chamber of Extinction [Ankh Upper]', lambda state: state.has('Feather', player))
	connect(world, player, 'Chamber of Extinction [Teleport]', 'Chamber of Extinction [Ankh Lower]', lambda state: s.glitch_raindrop(state) and state.has('Holy Grail', player))


def connect(world: MultiWorld, player: int, source: str, target: str, logic: Optional[Callable[CollectionState,bool]] = None):
	source_region = world.get_region(source, player)
	target_region = world.get_region(target, player)
	
	connection = Entrance(player, '', source_region)

	if logic:
		connection.access_rule = logic
	source_region.exits.append(connection)
	connection.connect(target_region)

def create_location(player: int, location_data: LocationData, region: Region, additional_logic: Optional[Callable]=None):
	location = Location(player, location_data.name, location_data.code, region)
	if additional_logic:
		location.access_rule = lambda state: additional_logic(state) and location_data.logic(state)
	else:
		location.access_rule = location_data.logic
	if location_data.is_event:
		location.event = True
		location.locked = True
	return location

def create_region(world: MultiWorld, player: int, region_name: str, locations_per_region: Dict[str, List[LocationData]], npcs_per_region: Dict[str,LaMulanaNPCDoor]):
	region = Region(region_name, player, world)
	if region_name in locations_per_region:
		for location_data in locations_per_region[region_name]:
			location = create_location(player, location_data, region)
			region.locations.append(location)
	if region_name in npcs_per_region:
		for npc_door in npcs_per_region[region_name]:
			for location_data in npc_door.checks:
				location = create_location(player, location_data, region, npc_door.logic)
				if is_option_enabled(world, player, "RandomizeNPCs") and not location.event:
					setattr(location, '_hint_text', "at " + location_data.name + " in " + npc_door.room_name)
				region.locations.append(location)
	return region

