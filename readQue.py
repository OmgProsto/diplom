
def lst_que(test):
	with open (f"txt/questions{test}.txt", encoding='utf-8') as f:
		lst = eval(f.read())
		f.close()
	return lst


def createQue(test, que, var1, var2, var3, ans):
	with open (f"txt/questions{test}.txt", encoding='utf-8') as f:
		lst = eval(f.read())
		f.close()

	with open (f"txt/questions{test}.txt", 'w', encoding='utf-8') as f:
		lst.append([que, var1, var2, var3, ans])
		f.write(str(lst))
		f.close()
	return lst


def removeQue(test):
	with open (f"txt/questions{test}.txt", encoding='utf-8') as f:
		lst = eval(f.read())
		f.close()

	with open (f"txt/questions{test}.txt", 'w', encoding='utf-8') as f:
		lst.pop()
		f.write(str(lst))
		f.close()
	return lst

def countQue(test):
	with open (f"txt/questions{test}.txt", encoding='utf-8') as f:
		lst = eval(f.read())
		f.close()
	return len(lst)