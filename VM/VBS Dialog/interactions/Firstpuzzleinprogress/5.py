import sys,time

subPiece={'v': {'0': [['virus_starter_5', 's', '"So..."', '"I\'ve done some research while you were away."', 'Info', 'First puzzle in progress', 'x', '1', '0', '5']], '4': [['virus_response_10', 'v', '"Trust Me..."', '"You are sorely mistaken."', 'Info', 'Above', 'x', '', '4', '5']], '2': [['virus_response_9', 'v', '"An Interesting Find"', '"Humans have this notion that something from technology can\'t have emotions."', 'Info', 'Above', 'x', '3', '2', '5']]}, 'p': {'3': [['player_response_11', 'p', 'N/A', '"Your point?"', 'Info', 'Above', 'x', '4', '3', '5']], '1': [['player_response_10', 'p', 'N/A', '"And..."', 'Info', 'Above', 'x', '2', '1', '5']]}}

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

