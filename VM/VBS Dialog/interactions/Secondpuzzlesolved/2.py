import sys,time

subPiece={'v': {'0': [['virus_starter_2', 's', '"Keep Trying"', '"You\'re really determined to get rid of me, aren\'t you?"', 'Info', 'Second puzzle solved', 'x', '1', '0', '2'], ['virus_starter_2_1', 's', '"Keep Trying"', '"I\'d be more offended if I thought it were possible..."', 'Info', 'Above', 'x', '1', '0', '2'], ['virus_starter_2_2', 's', '"Keep Trying"', '"But it\'s not..."', 'Info', 'Above', 'x', '1', '0', '2'], ['virus_starter_2_3', 's', '"Keep Trying"', '"Even if you make progress, I\'m not going anywhere."', 'Info', 'Above', 'x', '1', '0', '2']], '2': [['virus_response_2', 'v', '"Keep Trying"', '"Good, because neither do I..."', 'Info', 'Above', 'x', '', '2', '2'], ['virus_response_2_1', 'v', '"Keep Trying"', '"You know, I like a person whose tenacious."', 'Info', 'Above', 'x', '', '2', '2'], ['virus_response_2_2', 'v', '"Keep Trying"', '"We\'re going to have some fun, aren\'t we?"', 'Info', 'Above', 'x', '', '2', '2']]}, 'p': {'1': [['player_response_2', 'p', 'N/A', '"I don\'t give up that easily."', 'Info', 'Above', 'x', '2', '1', '2']]}}

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

