import cmd

class HelloUser(cmd.Cmd):
    """A simple command interpreter"""
    def do_greet(self, person):
        """Greet a named user"""
        if person:
            print(f"Hello {person}")
        else:
            print("Hello everyone!!!")
    
    def do_EOF(self, line):
        return True
    
    def postloop(self):
        print

if __name__ == "__main__":
    HelloUser().cmdloop()