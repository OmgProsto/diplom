
def text_full(nameFile):
	with open ("txt/" + nameFile, encoding='utf-8') as f:
		lst = f.read().split("#---#")
		f.close()
	return lst


def welcomeFile():	
	with open ("txt/welcome.txt", encoding='utf-8') as f:
		lst = f.read()
		f.close()
	return lst
