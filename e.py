try:
	a= int(input('enter'))
	if a<=5:
		raise NameError
	else:
		raise TypeError

	if a==5:
	  print("its 5")
	  raise NameError

except TypeError:
	print(":)")
except NameError:
	print("its 5")

except NameError:
	print("error!!!,you have choosen less than 5")
except TypeError:
	print("greater than 5")
else:
	print("no error")
finally:
	print("excution completed")