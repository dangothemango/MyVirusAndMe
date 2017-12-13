import sys,time

subPiece={'v': {'0': [['virus_starter_3', 's', '"Impressed"', '"To your credit, I didn\'t think you\'d make it this far."', 'Info', 'Third puzzle started', 'x', '1', '0', '3']], '4': [['virus_response_4', 'v', '"All The World\'s A Stage"', '"I\'ll be honest, I really do..."', 'Info', 'Above', 'x', '5', '4', '3'], ['virus_response_4_1', 'v', '"All The World\'s A Stage"', '"It\'s been a long time since I\'ve had a captive audience at my disposal."', 'Info', 'Above', 'x', '5', '4', '3'], ['virus_response_4_2', 'v', '"All The World\'s A Stage"', '"So why wouldn\'t I take advantage of an opportunity when it presents itself?"', 'Info', 'Above', 'x', '5', '4', '3']], '7': [['virus_response_6', 'v', '"All The World\'s A Stage"', '"I\'m glad we\'re on the same page then."', 'Info', 'player_response_7', 'x', '', '7', '3'], ['virus_response_6_1', 'v', '"All The World\'s A Stage"', '"You\'ll find that we\'re more alike than you first anticipated."', 'Info', 'Above', 'x', '', '7', '3']], '2': [['virus_response_3', 'v', '"Impressed"', '"It would seem so. Color me impressed, for now..."', 'Info', 'player_response_3 or 4', 'x', '3', '2', '3']], '6': [['virus_response_5', 'v', '"All The World\'s A Stage"', '"If you find it so annoying, why bother asking me more questions?"', 'Info', 'player_response_6', 'x', '', '6', '3'], ['virus_response_5_1', 'v', '"All The World\'s A Stage"', '"You\'re merely indulging me by giving me a platform to speak."', 'Info', 'Above', 'x', '', '6', '3']]}, 'p': {'5': [['player_response_6', 'p', 'N/A', '"It\'s annoying."', 'Info', 'virus_response_4_2', 'Player chooses response', '6', '5', '3'], ['player_response_7', 'p', 'N/A', '"Fair enough."', 'Info', 'virus_response_4_2', 'Player chooses response', '7', '5', '3']], '3': [['player_response_5', 'p', 'N/A', '"You really like to hear yourself talk, don\'t you?"', 'Info', 'Above', 'x', '4', '3', '3']], '1': [['player_response_3', 'p', 'N/A', '"Don\'t underestimate me."', 'Info', 'virus_starter_3', 'Player chooses response', '2', '1', '3'], ['player_response_4', 'p', 'N/A', '"I\'m more capable than you think."', 'Info', 'virus_starter_3', 'Player chooses response', '2', '1', '3']]}}

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

