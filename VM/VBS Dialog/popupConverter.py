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
	for subPiece in subPieces:
		output+='result = MsgBox("'+ subPiece[2].strip('"') +'", vbOk+vbExclamation, "'+ subPiece[1].strip('"') +'")\n\n'

	filename = './popups/' + subPiece[4].replace(' ','') + (('/'+subPiece[5].replace(' ','')) if subPiece[5]!='x' else '') + '/' +str(piece)+'.vbs'
	os.makedirs(os.path.dirname(filename), exist_ok=True)
	with open(filename, 'w+') as f:
		f.write(output)