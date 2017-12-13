import sys,time

subPiece={'v': {'0': [['virus_starter_4', 's', '"Who Are You Exactly?"', '"It would seem you\'re really going to try and get rid of me."', 'Info', 'First puzzle started', 'x', '1', '0', '4'], ['virus_starter_4_1', 's', '"Who Are You Exactly?"', '"In that case, tell me something about yourself."', 'Info', 'Above', 'x', '1', '0', '4'], ['virus_starter_4_2', 's', '"Who Are You Exactly?"', '"We might as well get to know each other since I won\'t be going anywhere."', 'Info', 'Above', 'x', '1', '0', '4']], '4': [['virus_response_8', 'v', '"Don\'t You Worry..."', '"I wouldn\'t go so far as to make such an assumption."', 'Info', 'Above', 'x', '', '4', '4']], '2': [['virus_response_7', 'v', '"Now, Now..."', '"No need to be so hostile. I had assumed that was my job."', 'Info', 'Above', 'x', '3', '2', '4'], ['virus_response_7_1', 'v', '"Now, Now..."', '"You\'d be wise to try and get on my good side."', 'Info', 'Above', 'x', '3', '2', '4'], ['virus_response_7_2', 'v', '"Now, Now..."', '"I can cause...issues for you that you wouldn\'t been to keen on."', 'Info', 'Above', 'x', '3', '2', '4']]}, 'p': {'3': [['player_response_9', 'p', 'N/A', '"We aren\'t friends."', 'Info', 'Above', 'x', '4', '3', '4']], '1': [['player_response_8', 'p', 'N/A', '"I\'m not here to get along."', 'Info', 'Above', 'x', '2', '1', '4']]}}

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

