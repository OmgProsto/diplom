
def lst_que(test):
	with open (f"txt/questions{test}.txt", encoding='utf-8') as f:
		lst = eval(f.read())
		f.close()
	return lst