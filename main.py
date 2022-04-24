class HelloWorld:
    def __init__(self) -> None:
        self.say_hello = "Hello World"
    
    @property
    def say(self):
        return self.say_hello


def main():
    hello = HelloWorld()
    print(hello.say)


if __name__=='__main__':
    main()