import ဘီစင့်

print("Myanmar programming language")
while True:
	text = input('Myanmar > ')
	if text.strip() == "": continue
	result, error = ဘီစင့်.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))
