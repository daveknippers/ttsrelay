
import socket, sys, json, time
import discord

from options import player_colour_mapping, replace_map, disregard_details, channel_id, b20_user_id

from tokens import TOKEN

client = discord.Client()

def post_msg(msg,colour=None):
	for line in msg.split('\n'):
		# maybe these should be filtered out elsewhere
		if disregard_details and len(line) >= 2 and line[:2] == '||':
			continue
		# this here's pretty gnarly.
		# when i fire a message off, i can't get TTS to accept a second message.
		# i'm pretty sure it's because it's waiting for a connection/read from the
		# editor on port 39998. the solution is to connect and disconnect every time 
		# we want to send a message instead. don't judge me, you'd do the same thing.
		server_address = ('localhost', 39999)
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect(server_address)
		if colour == None:
			msg = {"messageID": 3,
				"guid":"-1",
				"script":'printToAll("{}")'.format(line)}
		else:
			msg = {"messageID": 3,
				"guid":"-1",
				"script":'printToAll("{}","{}")'.format(line,colour)}

		print(msg['script'])	
		
		msg = json.dumps(msg)
		msg_bytes = str.encode(str(msg))

		sock.send(msg_bytes)
		#data = sock.recv(1024)
		sock.close()

@client.event
async def on_message(msg):
	'''
	roll_channel = discord.utils.get(client.get_all_channels(), name='rolls')
	for msg_id in msg_ids:
		msg = await roll_channel.fetch_message(msg_id)
	'''
	if msg.author.id == b20_user_id and msg.channel.id == channel_id:
		parse_msg(msg)


# this isn't elegant but i could't figure out how to convert 
# a nested dict to a nested defaultdict
def read_field(d,key):
	try:
		val = d[key]
		for word,sub in replace_map.items():
			val = val.replace(word,sub)
		return val
	except KeyError:
		return None
	

def parse_msg(msg):
	for embed in msg.embeds:
		embed = embed.to_dict()
		
		statement = [''] # start with an empty line
		
		title = read_field(embed,'title')
		
		try:
			author = embed['author']
			if (name := read_field(author,'name')):
				colour = player_colour_mapping[name]
				statement.append(name)
			else:
				colour = player_colour_mapping.default_factory()
		except KeyError:
			author = None	
			colour = player_colour_mapping.default_factory()

		if title != None:
			statement.append(title)

		if author != None:
			try:
				field = author['fields']
				for field in fields:
					if (field_name := read_field(field,'name')):
						statement.append(field_name)
					if (field_value := read_field(field,'value')):
						statement.append(field_value)
			except KeyError:
				pass
				
		try:
			fields = embed['fields']
			for field in fields:
				if (field_name := read_field(field,'name')):
					statement.append(field_name)
				if (field_value := read_field(field,'value')):
					statement.append(field_value)
		except KeyError:
			pass
		
		if (description := read_field(embed,'description')):
			statement.append(description)
			
		statement = '\n'.join(statement)
		post_msg(statement,colour)

@client.event
async def on_ready():
	print('ttsrelay is relaying')
	
client.run(TOKEN)
