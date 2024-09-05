import cmd

class HelloOfficers(cmd.Cmd):
    """A simple command line interpreter"""
    officers = ['Emeka', 'Moshood', 'Mike', 'Dayo']

    def do_greeting(self, staff):
        """Greet Staff"""
        if staff and staff in self.officers:
            officer = "Hello {staff}"
        elif staff:
            officer = "Hello ", + staff
        else:
            officer = "Hello everyone"
        print(officer)
    
    def complete_greet(self, line, text, begidx, endidx):
        if not text:
            completed = self.officers[:]
        else:
            completed = [name for name in self.officers if name.startswith(text)]
        return completed
    
    
    def do_EOF(self):
        return True
    

if __name__ == "__main__":
    HelloOfficers().cmdloop()