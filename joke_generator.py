import pyjokes

def joke_generator():
    joke = pyjokes.get_joke()
    print("Here's a joke for you:")
    print(joke)




if __name__ == "__main__":
    joke_generator()
