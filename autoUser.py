
def users(surname, group, test = 1):
	with open (f"txt/users{test}.txt", 'r+', encoding='utf-8') as f:
		lst = eval(f.read())

		for i in range(len(lst)):
			if lst[i][0] == surname and lst[i][1] == group:
				if lst[i][2]: lst[i][2] -= 1
				f.seek(0)
				f.write(str(lst))
				f.close()
				return lst[i][2], lst[i][3]

		lst.append([surname, group, 2, 0])
		f.seek(0)
		f.write(str(lst))
		f.close()
		return 2, 0


def que_user(surname, group, test = 1):
	with open (f"txt/users{test}.txt", 'r', encoding='utf-8') as f:
		lst = eval(f.read())

		for i in range(len(lst)):
			if lst[i][0] == surname and lst[i][1] == group:
				return lst[i][2], lst[i][3]

		f.close()
		return 3, 0


def upd_res(surname, group, res, test = 1):
	with open (f"txt/users{test}.txt", 'r+', encoding='utf-8') as f:
		lst = eval(f.read())

		for i in range(len(lst)):
			if lst[i][0] == surname and lst[i][1] == group:
				lst[i][3] = res
				f.seek(0)
				f.write(str(lst))
				f.close()
				return 0


def check(test = 1):
	with open (f"txt/users{test}.txt", 'r', encoding='utf-8') as f:
		lst = eval(f.read())
	return lst


def sbrosFile(test = 1):
	with open (f"txt/users{test}.txt", 'w', encoding='utf-8') as f:
		lst = '[]';
		f.write(str(lst))
		f.close()




		