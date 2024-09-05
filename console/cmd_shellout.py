import cmd
import os

class ShellEnbled(cmd.Cmd):

    last_output = ""

    def do_shell(self, line):
        "Run a shell command"
        print(f"The shell command run is {line}")
        output = os.popen(line).read()
        print(output)
        self.last_output = output
    
    def do_echo(self, line):
        """Print the input, replacing $out with output of last shell command"""
        print(f"{line.replace('$out', self.last_output)}")
    
    def do_EOF(self, line):
        return True
    

if __name__ == "__main__":
    ShellEnbled().cmdloop()