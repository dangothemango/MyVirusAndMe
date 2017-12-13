import sys,time

subPiece={'v': {'0': [['virus_starter_10', 's', '"Nearing The End"', '"Here we are. Never thought we\'d reach this point."', 'Info', 'Fifth puzzle started', 'x', '1', '0', '10'], ['virus_starter_10_1', 's', '"Nearing The End"', '"But maybe not for the same reasons as before."', 'Info', 'Above', 'x', '1', '0', '10'], ['virus_starter_10_2', 's', '"Nearing The End"', '"You\'ve proved your...ability."', 'Info', 'Above', 'x', '1', '0', '10']], '4': [['virus_response_18', 'v', '"Something About You"', '"I\'m glad."', 'Info', 'Above', 'x', '5', '4', '10'], ['virus_response_19', 'v', '"Something About You"', '"You\'ve given me a lot to reflect upon."', 'Info', 'Above', 'x', '5', '4', '10']], '2': [['virus_response_17', 'v', '"Something About You"', '"I\'d even say we\'re starting to really get on."', 'Info', 'Above', 'x', '3', '2', '10']], '6': [['virus_response_20', 'v', '"Well..."', '"I\'d hate to have to go so soon..."', 'Info', 'Above', 'x', '', '6', '10'], ['virus_response_21', 'v', '"Well..."', '"I wonder if you\'ll miss me?"', 'Info', 'Above', 'x', '', '6', '10']]}, 'p': {'5': [['player_response_20', 'p', 'N/A', '"Is that so?"', 'Info', 'Above', 'x', '6', '5', '10']], '3': [['player_response_19', 'p', 'N/A', '"I\'m flattered."', 'Info', 'Above', 'x', '4', '3', '10']], '1': [['player_response_18', 'p', 'N/A', '"I have?"', 'Info', 'Above', 'x', '2', '1', '10']]}}

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

