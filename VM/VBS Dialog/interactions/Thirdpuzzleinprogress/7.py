import sys,time

subPiece={'v': {'0': [['virus_starter_7', 's', '"At It Again?"', '"Ever determined are you?"', 'Info', 'Third puzzle in progress', 'x', '1', '0', '7']], '4': [['virus_response_13', 'v', '"How You Say..."', '"Hats off to you, for your effort."', 'Info', 'Above', 'x', '', '4', '7']], '2': [['virus_response_12', 'v', '"Intriguing"', '"Yes, it would seem so..."', 'Info', 'Above', 'x', '3', '2', '7']]}, 'p': {'3': [['player_response_15', 'p', 'N/A', '"Really?"', 'Info', 'Above', 'x', '4', '3', '7']], '1': [['player_response_14', 'p', 'N/A', '"That\'s me."', 'Info', 'Above', 'x', '2', '1', '7']]}}

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

