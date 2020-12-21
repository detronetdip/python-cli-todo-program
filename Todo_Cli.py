loop=int(0)
todo=["----------All TODO----------"]
while loop!=int(4):
	cmd=input("/~~/python/CLI/todo/ $ ")
	data=cmd.split()
	if data[0]=='help':
		print("\n\n")
		print("\t COMMANDS             DESCRIPTION")
		print("\t___________________________________\n")
		print("\t  add      arg       -  Add Todo")
		print("\t  remove   index     -  Remove Todo")
		print("\t  done     index     -  Mark Done Todo")
		print("\t  remain             -  Remaining Todo")
		print("\t  complete           -  Completed Todo")
		print("\t  ls                 -  Show List")
		print("\t  help               -  Information")
		print("\t  exit               -  Exit Programm")
		print("\n\n")
	elif data[0]=='add':
		new=""
		for each in data:
			if each!='add':
				new=new+" "+each
		if new!="":
			todo.append(new)
			(f"{new} added")
		else:
			print("Few Arguments")
	elif data[0]=='done':
		try:
			if int(data[1])>len(todo):
				print("Invlid Index")
			else:
				todo[int(data[1])]=todo[int(data[1])]+" (done)"
		except:
			print("Too few argument")			
	elif data[0]=='remain':
		for each in todo:
			dif=each.split()
			try:
				dif.index("(done)")
			except:
				print(each)
	elif data[0]=='complete':
		for each in todo:
			dif=each.split()
			try:
				if dif.index("(done)"):
					print(each)
			except:
				u=0
	elif data[0]=='ls':
			cnt=0
			for each in todo:
						if cnt==0:
							print(each)
							cnt=cnt+1
						else:
							print("\t"+str(cnt)+".  "+each)
							cnt=cnt+1
	elif data[0]=='remove':
		try:
			rem=int(data[1])
			todo.remove(todo[rem])
			print("Removed")
		except:
			print("List Error, Probably List Is Empty,or too few arguments")
	elif data[0]=='exit':
		loop=int(4)
	else :
		print("Invalid Syntax error")
		print(f" {data} not defined")
		print("\n\n")
		print("\t COMMANDS             DESCRIPTION")
		print("\t___________________________________\n")
		print("\t  add      arg       -  Add Todo")
		print("\t  remove   index     -  Remove Todo")
		print("\t  done     index     -  Mark Done Todo")
		print("\t  remain             -  Remaining Todo")
		print("\t  complete           -  Completed Todo")
		print("\t  ls                 -  Show List")
		print("\t  help               -  Information")
		print("\t  exit               -  Exit Programm")
		print("\n\n")