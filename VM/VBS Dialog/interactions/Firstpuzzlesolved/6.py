import sys,time

subPiece={'v': {'0': [['virus_starter_6', 's', '"I Must Ask..."', '"Have you ever considered that you aren\'t as intelligent as you think?"', 'Info', 'First puzzle solved', 'x', '1', '0', '6']], '2': [['virus_response_11', 'v', '"..."', '"Nevermind."', 'Info', 'player_response_12 or 13', 'x', '', '2', '6']]}, 'p': {'1': [['player_response_12', 'p', 'N/A', '"Projecting?"', 'Info', 'virus_starter_6', 'Player chooses response', '2', '1', '6'], ['player_response_13', 'p', 'N/A', '"Why?"', 'Info', 'virus_starter_6', 'Player chooses response', '2', '1', '6']]}}

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

