import sys,time

subPiece={'v': {'0': [['virus_starter_8', 's', '"You Know..."', '"I will say, you\'ve grown on me."', 'Info', 'Fourth puzzle started', 'x', '1', '0', '8']], '2': [['virus_response_14', 'v', '"Indeed..."', '"You are...something else."', 'Info', 'Above', 'x', '', '2', '8'], ['virus_response_15', 'v', '"Indeed..."', '"I haven\'t quite figured it out."', 'Info', 'Above', 'x', '', '2', '8']]}, 'p': {'1': [['player_response_16', 'p', 'N/A', '"That so?"', 'Info', 'Above', 'x', '2', '1', '8']]}}

dialogItem = subPiece['v']['0']

while len(dialogItem)>0:
	print()
	if dialogItem[0][1]=='v' or dialogItem[0][1]=='s':
		for dialogBit in dialogItem:
			text = dialogBit[3].strip('"')
			for char in text:
				sys.stdout.write(char)
				sys.stdout.flush()
				time.sleep(.05)
			sys.stdout.write('\n')
		dialogItem = subPiece['p'][dialogItem[0][7]] if len(dialogItem[0][7])>0 else list()
	else:
		for i in range(len(dialogItem)):
			sys.stdout.write(str(i)+': '+dialogItem[i][3]+'	')
		sys.stdout.write('\n')
		selection = -1
		while selection<0 or selection>len(dialogItem):
			selection = int(input('Sys: Enter a number between '+str(0)+'-'+str(len(dialogItem)-1)+' '))
		sys.stdout.write('\n'+dialogItem[selection][3]+'\n')
		dialogItem = subPiece['v'][dialogItem[selection][7]] if len(dialogItem[selection][7])>0 else list()

