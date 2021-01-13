
from collections import defaultdict

# change the string after the 'lambda' to change the
# default colour for non-colour-mapped players
#
# Valid colours:
# White
# Brown
# Red
# Orange
# Yellow
# Green
# Teal
# Blue
# Purple
# Pink
# Grey
# Black
#
# more information can be found here:
# https://api.tabletopsimulator.com/player-color/
player_colour_mapping = defaultdict(lambda: 'Grey', 
	dict([('Hecuba','Teal'),
		('Arkin','Red'),
		('Meltor','White'),
		('Cid','Blue'),
		('Grezlik','Yellow'),
		('Lannister','Brown'),
		('Gorgulash','Green')]))

# if any part of the key (the first part of the pair)
# is in a message parsed from discord, it will be mapped
# to the value (the second part of the pair)
replace_map = {':game_die:':'Dice:',
		':arrow_right:':'->',
		'**':'',
		'_':'',
		':redcircle:':'',
		':greencircle:':'',
		':zero:':'0',
		':one:':'1',
		':two:':'2',
		':three:':'3',
		':four:':'4',
		':five:':'5',
		':six:':'6',
		':seven:':'7',
		':eight:':'8',
		':nine:':'9',
		':keycapten:':'10'}

# Throw out any text line that starts with '||'
disregard_details = True

# channel id to listen in on
channel_id = 797613626356793346

# user to listen to embeds from
b20_user_id = 686200628984545309 


