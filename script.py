Author = "Lettever"

@SelfCloses
def br():
	return '<br>'

def Header():
	return '<h1>This header comes from python</h1>'

def Hello(name, age):
    return f"Hello {name}, i am {age} years old"

@KeepsSpace
def pre(body):
	return f'<pre>{body}</pre>'
