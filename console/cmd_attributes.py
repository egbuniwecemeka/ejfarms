import cmd

class EjFarms(cmd.Cmd):
    """A simple command line interpreter"""

    prompt = "prompt:"
    intro = "My farm's command interpreter"

    doc_header = "doc_header"
    misc_header = "misc_header"
    undoc_header = "undoc_header"

    ruler = "_"

    def do_prompt(self, line):
        "Change the interactive prompt"
        self.prompt = line + ':'
    
    def do_EOF(self, line):
        "Exit"
        return True
    

if __name__ == "__main__":
    EjFarms().cmdloop()