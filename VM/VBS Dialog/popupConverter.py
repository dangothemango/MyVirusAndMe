import os

file = 'popup.tsv'


with open(file,'r') as f:
	global listOfStuff
	listOfStuff = f.readlines()

pieces={}

for line in listOfStuff:
	line = line.strip()
	line = line.split('\t')
	if not line[-1] in pieces:
		pieces[line[-1]]=list()
	pieces[line[-1]].append(line)

for piece in pieces:
	subPieces = pieces[piece]
	output =''
	trigger=''
	subTrigger = ''
	for subPiece in subPieces:
		if trigger == '':
			trigger = subPiece[4].replace(' ','')
		if subTrigger=='':
			subTrigger=subPiece[5].replace(' ','')
		output+='result = MsgBox("'+ subPiece[2].strip('"') +'", vbOk+vbExclamation, "'+ subPiece[1].strip('"') +'")\n\n'

	filename = './popups/' + trigger + (('/'+subTrigger) if subTrigger!='x' else '') + '/' +str(piece)+'.vbs'
	os.makedirs(os.path.dirname(filename), exist_ok=True)
	with open(filename, 'w+') as f:
		f.write(output)