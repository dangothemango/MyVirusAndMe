import os,time,sys

file = 'interactions.tsv'


with open(file,'r') as f:
	global listOfStuff
	listOfStuff = f.readlines()

pieces={}

for line in listOfStuff[1:]:
	line = line.strip()
	line = line.split('\t')
	if not line[-1] in pieces:
		pieces[line[-1]]=list()
	pieces[line[-1]].append(line)

organizedPieces=[]
for piece in pieces:
	subPieces = pieces[piece]
	organizedSubPiece = {'p':{}, 'v':{}}
	for subPiece in subPieces:
		if subPiece[1]=='s' or subPiece[1]=='v':
			if not subPiece[8] in organizedSubPiece['v']:
				organizedSubPiece['v'][subPiece[8]]=list()
			organizedSubPiece['v'][subPiece[8]].append(subPiece)
		else:
			if not subPiece[8] in organizedSubPiece['p']:
				organizedSubPiece['p'][subPiece[8]]=list()
			organizedSubPiece['p'][subPiece[8]].append(subPiece)
	organizedPieces.append(organizedSubPiece)

for piece in organizedPieces:
	print (piece['v']['0'])
	output = 'import sys,time\n\nsubPiece='+str(piece)+"\n\ndialogItem = subPiece['v']['0']\n\nwhile len(dialogItem)>0:\n\tprint()\n\tif dialogItem[0][1]=='v' or dialogItem[0][1]=='s':\n\t\tfor dialogBit in dialogItem:\n\t\t\ttext = dialogBit[3].strip('\"')\n\t\t\tfor char in text:\n\t\t\t\tsys.stdout.write(char)\n\t\t\t\tsys.stdout.flush()\n\t\t\t\ttime.sleep(.05)\n\t\t\tsys.stdout.write('\\n')\n\t\tdialogItem = subPiece['p'][dialogItem[0][7]] if len(dialogItem[0][7])>0 else list()\n\telse:\n\t\tfor i in range(len(dialogItem)):\n\t\t\tsys.stdout.write(str(i)+': '+dialogItem[i][3]+'\t')\n\t\tsys.stdout.write('\\n')\n\t\tselection = -1\n\t\twhile selection<0 or selection>len(dialogItem):\n\t\t\tselection = int(input('Sys: Enter a number between '+str(0)+'-'+str(len(dialogItem)-1)+' '))\n\t\tsys.stdout.write('\\n'+dialogItem[selection][3]+'\\n')\n\t\tdialogItem = subPiece['v'][dialogItem[selection][7]] if len(dialogItem[selection][7])>0 else list()\n\n"
	trigger = piece['v']['0'][0][5].replace(' ','')
	subTrigger = piece['v']['0'][0][-1]
	filename = './interactions/' + trigger + '/' +subTrigger+'.py'
	os.makedirs(os.path.dirname(filename), exist_ok=True)
	with open(filename, 'w+') as f:
		f.write(output)