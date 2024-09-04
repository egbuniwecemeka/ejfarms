import cmd

class HelloWorld(cmd.Cmd):
    """A simple command processor"""
    def do_hello(self, line):
        print("Hello everyone")
    
    def do_EOF(self, line):
        return True
    
if __name__ == "__main__":
    HelloWorld().cmdloop()