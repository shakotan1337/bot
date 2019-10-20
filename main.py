import socket

connection_data = ('irc.chat.twitch.tv', 6667)
token = 'oauth:ey5vowbxk36tqf41u1y1wlizjwyksx'
user = 'spookytoha'
channel = '#spookytoha'
readbuffer = ''

def send_message(message):
	server.send(bytes('PRIVMSG #' + user + ' :' + message + '\r\n', 'UTF-8'))
	
server = socket.socket()
server.connect(connection_data)
server.send(bytes('PASS ' + token + '\r\n', 'utf-8'))
server.send(bytes('NICK ' + user + '\r\n', 'utf-8'))
server.send(bytes('JOIN ' + channel + '\r\n', 'utf-8'))


while True:
	response = server.recv(1024).decode('utf-8')
	print(response)
	resp_list = []
	if response == "PING :tmi.twitch.tv\r\n":
		server.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
	for line in response.split():
		resp_list.append(line)
	if resp_list[1] == 'PRIVMSG' and resp_list[3] == ':!hello':
		print('sending')
		name = resp_list[2].strip('#')
		send_message('welcome ' + name + ' HeyGuys')
