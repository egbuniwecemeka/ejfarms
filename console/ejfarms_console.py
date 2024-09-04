import sys, cmd
from turtle import *

class TurtleShell(cmd.Cmd):
    intro = "Welcome to ejfarms interactive shell. Type help or ? to list commands\n"
    prompt = "(ejfarms)"

    #--------- Basic commands --------
    def do_forward(self, arg):
        """ Move the cursor forward by a certain distance: """
        forward(*parse(arg))

    def do_right(self, arg):
        """ Move the cursor right by a given degree """
        right(*parse(arg))
    
    def do_left(self, arg):
        """ Move the cursor left by a given degree"""
        left(*parse(arg))
    
    def do_goto(self, arg):
        """ Move cursor to absolute position without changing orientation """
        goto(*parse(arg))
    
    def do_home(self, arg):
        """ Returm cursor to home position """
        home()
    
    def do_circle(self, arg):
        """ Draw circle with given radius """
        circle(*parse(arg))
    
    def do_position(self, arg):
        """ Prints a cursor position """
        print(f"Current position is {position()}")

    def do_heading(self, arg):
        """ Print current cursor heading in degrees """
        print(f"The heading of the cursor is {heading()}")
    
    def do_color(self, arg):
        """ Set cursor color """
        color(arg.lower())
    
    def do_undo(self, arg):
        """ Undo repetedly last cursor action """
    def do_reset(self, arg):
        """Clear screen and return cursor to default """
        reset()
    
    def do_bye(self, arg):
        """Stop and close the cursor window """
        print("Thank you for using turtle")
        self.close()
        bye()
        return True
    
    # ------ record and playback -------
    def do_record(self, arg):
        """Save future commands to filename"""
        self.file = open(arg, 'w')
    def do_playback(self, arg):
        """Playback commands from a file"""
        self.close()
        with open(arg) as f:
            self.cmdqueue.extend(f.read().splitlines())
    def precmd(self, line):
        line = line.lower()
        if self.file and 'playback' not in line:
            print(line, file=self.file)
        return line
    def close(self):
        if self.file:
            self.file.close()
            self.file = None
    
def parse(arg):
    """Convert a series of zero or more numbers to an argument tuple"""
    return tuple(map(int, arg.splt()))

if __name__ == "__main__":
    TurtleShell().cmdloop()