# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 08:10:42 2025

Aufgabe 1

Schreiben Sie unter Verwendung von Listen ein Programm welches Lotto 6 aus 49 spielt. Anforderungen:

 1. Der Benutzer soll einen Lotto-Tipp abgeben: 6 Zahlen zwischen 1 und 49 sollen ueber die Konsole nacheinander eingegeben werden.
 2. Das Programm soll dann 6 Zahlen aus den Zahlen 1 bis 49 "ziehen". Beachten Sie, dass gezogene Zahlen nicht mehrfach vorkommen duerfen!
 3. Die Zahlen sollen waehrend der Ziehung in der Reihenfolge des Ziehens ausgegeben werden
 4. Nach der Ziehung sollen die gezogenen Zahlen zusaetzlich sortiert in aufsteigender Reihenfolge ausgegeben werden.
 5. Das Programm soll berechnen wie viele Richtige der Benutzer getippt hat und dies ausgeben.
 6. Bonusaufgabe: die richtig getippten Zahlen sollen sowohl waehrend der Ziehung als auch bei der sortiert ausgegebenen Ziehung farbig markiert werden

Hinweise:

 1. Schreiben Sie ein gut strukturiertes und benutzerfreundliches Programm und denken Sie auch an moegliche Fehler!
 2. Die Module NumPy und Pandas duerfen nicht verwendet werden.

@author: jannis kuestner
"""
import random
import math
import time
import re

from colorama import Fore, Style                                                                    

# picture of a lotto machine
LOTTO_MACHINE = f"""  
{Fore.YELLOW}               00000000000               {Style.RESET_ALL}
{Fore.YELLOW}           0000     0     0000           {Style.RESET_ALL}
{Fore.YELLOW}        000         0         000        {Style.RESET_ALL}
{Fore.YELLOW}      00     {Style.RESET_ALL}(09){Fore.YELLOW}   0            00      {Style.RESET_ALL}
{Fore.YELLOW}   00    {Style.RESET_ALL}(18){Fore.YELLOW}       0               00   {Style.RESET_ALL}
{Fore.YELLOW}  00                0      {Style.RESET_ALL}(10){Fore.YELLOW}      00  {Style.RESET_ALL}
{Fore.YELLOW} 00                 0            {Style.RESET_ALL}(14){Fore.YELLOW} 00 {Style.RESET_ALL}
{Fore.YELLOW}00                  0     {Style.RESET_ALL}(01){Fore.YELLOW}         00{Style.RESET_ALL}
{Fore.YELLOW}00   {Style.RESET_ALL}(16){Fore.YELLOW}           0                  00{Style.RESET_ALL}
{Fore.YELLOW}0            {Style.RESET_ALL}(07){Fore.YELLOW}   0                   0{Style.RESET_ALL}
{Fore.YELLOW}0                  000          {Style.RESET_ALL}(05){Fore.YELLOW}    0{Style.RESET_ALL}
{Fore.YELLOW}0              000     000              0{Style.RESET_ALL}
{Fore.YELLOW}00         000             000         00{Style.RESET_ALL}
{Fore.YELLOW}00     000                     000     00{Style.RESET_ALL}
{Fore.YELLOW} 00 00          {Style.RESET_ALL}(02){Fore.YELLOW}               00 00 {Style.RESET_ALL}
{Fore.YELLOW}  00       {Style.RESET_ALL}(11){Fore.YELLOW}                      00  {Style.RESET_ALL}
{Fore.YELLOW}   00                     {Style.RESET_ALL}(41){Fore.YELLOW}      00   {Style.RESET_ALL}
{Fore.YELLOW}      00                         00      {Style.RESET_ALL}
{Fore.YELLOW}        000      0     0      000        {Style.RESET_ALL}
{Fore.YELLOW}        0  0000  0     0  0000 0         {Style.RESET_ALL}
{Fore.YELLOW}       0       000     000      0        {Style.RESET_ALL}
{Fore.YELLOW}      0          0     0         0       {Style.RESET_ALL}
{Fore.YELLOW}     0           0     0          0      {Style.RESET_ALL}
{Fore.YELLOW}    00000000000000     0000000000000     {Style.RESET_ALL}
{Fore.YELLOW}                 0     0                 {Style.RESET_ALL}
{Fore.YELLOW}                 0     0                 {Style.RESET_ALL}"""


class Lotto6Of49():
    """Game for playing Lotto 6 of 49, with multiple round possible.
    Picture of lotto machine can be displayed during draw.
    
    Start game with play() method.
    
    Demands user input and checks it.
    Draws 6 numbers out of 49.
    Does some nice printing."""
    def __init__(self, lotto_machine=False):
        """Initialize game variables.
        Initialize class for pretty printing.
        Definition of graphic and text messages."""
        # game variables        
        self.__guess = [] # list of guessed numbers from user
        self.__balls = list(range(1, 50)) # balls to draw from
        self.__draws = [] # list of drawn numbers
        self.__result = 0 # number of correct guess numbers

        # class for pretty printing
        # initialize with width and space for consistent appearance
        self.__pp = PrettyPrint(width=47, space=2) # ideal width for picture
        
        # definition of graphic and text messages
        self.__lotto_machine = lotto_machine # string when given, else False
        self.__titles = {
            "game": f"{Fore.YELLOW}Lotto 6 of 49{Style.RESET_ALL}",
            "invalid": f"{Fore.RED}Invalid user input{Style.RESET_ALL}",
            "guess": f"{Fore.YELLOW}Your Guess{Style.RESET_ALL}",
            "draw": f"{Fore.YELLOW}Drawing 6 of 49{Style.RESET_ALL}",
            "result": f"{Fore.YELLOW}Final Result{Style.RESET_ALL}",
            "exit": f"{Fore.YELLOW}User Exit{Style.RESET_ALL}"
            }    
        self.__messages = {
            "game": """Instructions:
            You can choose 6 numbers between 1 and 49. Insert your number and press enter to go on to the next.
            If you want to exit, just press "e".""",
            "exit": "Game was terminated by user!",
            "invalid": "Please enter a valid number between 1 and 49 or press \"e\" to exit."
            }
        self.__ends = {
            "game": f"{Fore.YELLOW}Game On!{Style.RESET_ALL}",
            "guess": f"{Fore.YELLOW}Good Luck!{Style.RESET_ALL}",
            "draw": f"{Fore.YELLOW}Draw Complete!{Style.RESET_ALL}",
            "win": "You Won! Keep Winning!",
            "lose": "You Lost. Try Again!",
            "exit": f"{Fore.YELLOW}Game Over!{Style.RESET_ALL}"
            }
                      
    def __check_input(self, user_input):
        """Checks user input.
        Returns True, if the input is new intger between 1 and 49.
        Else returns False."""
        # using isdecimal() to check if input is a number
        #   NOTE: "1.0" is false, because of ".", so only integers are True
        #   NOTE: NOT using isdigit() because it would allow "²"
        #   NOTE: isdecimal() allows arabic numbers, which is fine, because 
        #         int() can handle them too. So try to insert e.g. ٤ :)
        if user_input.isdecimal():
            user_int = int(user_input)
            # checking if number is new and between 1 and 49
            return ((user_int not in self.__guess) and (1 <= user_int <= 49))
        # return false, if it's not an integer
        return False
        
    def __format_latest_draws(self, i=-1):
        """Returns formatted string.
        Takes index as optional input, default is '-1' for last draw.
        Draws from i to end are formatted as balls, e.g. (2) (5) (9).
        Makes balls green for correct guesses.
        """
        # no error handling done, because not dependent on user input
        formatted_draws = ""
        
        # iterate through draws
        for draw in self.__draws[i:]:
            # highlight correct guess
            if draw in self.__guess:
                # make it green
                draw = Fore.GREEN + f"({draw:02d})\x1b[0m" + Style.RESET_ALL
            else:
                draw = f"({draw:02d})"
            
            # add to formatted draws
            formatted_draws = " ".join([formatted_draws, draw])
        
        return formatted_draws

    def __print_result_message(self):
        """Prints sorted draw and number of correct guesses.
        Highlights correct guesses and result."""
        # color
        color = Fore.GREEN if self.__result else Fore.RED
        reset = Style.RESET_ALL # just so code line does not ge too long
        
        # message
        #   draws
        draws = self.__format_latest_draws(i=0)
        
        #   result
        numbers = "numbers" if self.__guess != 1 else "number"
        result = f"You guessed {color}{self.__result}{reset} {numbers} correct!"

        #   complete text
        result_message = draws + "\n\n" + result
        
        # end
        end_text = self.__ends["win"] if self.__result else self.__ends["lose"]
        end = color + end_text + reset
        
        # print result
        self.__pp.print_message(
            title=self.__titles["result"],
            message=result_message, # all draws
            end=end,
            alignment="center",
            )
               
    def __get_input_guess(self):
        """Requests input number between 1 and 49 until six were given or
        user pressed 'e' to exit.
        Returns True for six valid numbers and False for exit."""
        while len(self.__guess) < 6:
            # get input number
            user_input = input(f"Guess {len(self.__guess)+1}/6: ")
            
            # check if user wants to exit
            if user_input == "e":
                return False
            # check if user has provided a valid input
            elif self.__check_input(user_input):
                self.__guess.append(int(user_input)) # append number to guess
            # Demand a valid input from user
            else:
                self.__pp.print_message(
                    title=self.__titles["invalid"],
                    message= self.__messages["invalid"],
                    alignment="center"
                    )                
        
        # sort guess
        self.__guess.sort()
        
        return True
            
    def __draw_6of49(self):
        """Draws six random numbers between 1 and 49.
        Prints each number after draw.
        Sorts numbers and calculated result after last draw."""
        # NOTE: Printing for draw is done 'manually' with pretty_print()
        #       instead of print_message() because of instructions to print
        #       draws during drawing. Instructions were interpreted literally.
        #       Could be optimised --> draw all, prepare message, use 
        #       print_message()
        
        # prefix
        #   a little space
        print("")
        
        #   print draw title
        self.__pp.pretty_print(
            text=self.__titles["draw"],
            alignment="center",
            fill_char="-"
            )
        
        #   print lotto machine if available
        if self.__lotto_machine:
            # need strip=False to keep spaces on left side of lotto machine
            self.__pp.pretty_print(self.__lotto_machine, strip=False)
        
        #   print drawing text
        self.__pp.pretty_print(text="") # empty line
        self.__pp.pretty_print(text="Drawing...") # drawing...
        self.__pp.pretty_print(text="") # empty line
        
        # draw six numbers
        for n_balls in [49, 48, 47, 46, 45, 44]: # clearer than: range(44, 50)[::-1]
            # pass some time to make it more realistic
            time.sleep(2)
            
            # get random index (random.randint: int 1 <= N <= n)
            rand_index = random.randint(0, n_balls - 1) # index starts with 0
                       
            # extract draw with index from balls and append to draws
            self.__draws.append(self.__balls.pop(rand_index))
            # print draw
            self.__pp.pretty_print(
                text=self.__format_latest_draws(),
                alignment="center"
                    )
        
        # suffix
        self.__pp.pretty_print(text="") # empty line
        # print end of draw
        self.__pp.pretty_print(
            text=self.__ends["draw"],
            alignment="center",
            fill_char="-"
            )
        
        # sort draws
        self.__draws.sort()
        
        # calculate result
        self.__result = len((set(self.__guess) & set(self.__draws)))

    def __reset(self):
        """Sets game variables back to start value for a new game."""
        self.__guess = [] # list of guessed numbers from user
        self.__balls = list(range(1, 50)) # balls to draw from
        self.__draws = [] # list of drawn numbers
        self.__result = 0 # number of correct guess numbers  

    def play(self):
        """Play Lotto6Of49.
        
        Prints instructions.
        Gets user input.
        Draws 6 numbers of 49.
        Prints result.
        
        Can be terminated with 'e' during user input for guess or with anything
        other than 'y' during next round query."""
        while True:
            # print intro
            self.__pp.print_message(
                title=self.__titles['game'],
                message=self.__messages['game'],
                end=self.__ends["game"]
                )
            
            # get user guess
            is_playing = self.__get_input_guess()
            
            # draw numbers if user didn't exit
            if is_playing:
                # print user guess
                self.__pp.print_message(
                    title=self.__titles["guess"],
                    message=" ".join(f"{number:02d}" for number in self.__guess),
                    end=self.__ends["guess"],
                    alignment="center"
                    )
                
                time.sleep(2) # pass some time, so the user can view his guess
                
                # draw numbers
                self.__draw_6of49() 
                
                time.sleep(1) # smoother game flow
                
                # print result
                self.__print_result_message()

                time.sleep(1) # smoother game flow
                
                # check if user wants to play another game                
                # Only continue if user pressed y
                # Don't continue if user pressed anything other, doesn't have
                # to be 'n'. It's a feature not a bug
                if input("New Game (y/n): ") == "y":
                    self.__reset() 
                    continue
            
            # exit message    
            self.__pp.print_message(
                title=self.__titles["exit"],
                message=self.__messages["exit"],
                end=self.__ends["exit"],
                alignment="center"
                )
            break


# normally I would save this in a file with the name 'pretty_print.py' and 
# import the class with 'from pretty_print import PrettyPrint as pp'
# but to make it easier to execute I decided against it

# NOTE: PrettyPrint() is designed to be independent from Lotto6Of49().
#       But it is a new class that I created for this task. As such it has no
#       claim to have a complete error handling. I made sure it works for this 
#       use case, but as it is independent from any user input I focused on 
#       other tasks at hand :)
class PrettyPrint():
    """Provides two methods for pretty printing.
    1. pretty_print() for simple lines
    2. print_message() for complete messages
    """
    def __init__(self, width, space):
        """Initialize format variables width and space.
        Define regular expression for ansi color an style codes, to be able to
        extract them from strings."""
        # format variables
        self.__width = width # total width
        self.__space = space # minimal space from text to one side
        
        # regular expression !only! for ansi color and style codes
        # e.g. green = \x1b[32m or reset = \x1b[0m
        # \x1b for ESC character (always the same)
        # \[ for "[" which is the start bracket
        # [0-9;]* for digits or semicolons
        # m for "m", Marks end for color and text styles (always the same)
        self.__ansi_color_regex = re.compile("\x1b\[[0-9;]*m")

    def __text_len(self, text):
        """Takes a string as input.
        Returns the length of the string without ansi color/style codes.
        E.g. '\x1b[32m(05)\x1b[0m --> '(05) --> 4'"""
        return len(self.__ansi_color_regex.sub('', text))

    def __calc_gaps(self, line_width, alignment):
        """Returns left and right gap for given alignment."""
        # |<gap_left><text><gap_right>|
        # self.__width = 1 + gap_left + line_width + gap_right + 1
        # self.__width = gap_left + line_width + gap_right + 2
        if alignment == 'left':
            gap_left = self.__space
            gap_right = self.__width - (line_width + gap_left + 2)
        elif alignment == 'center':
            gap = (self.__width - (line_width + 2)) / 2
            gap_left = math.ceil(gap) # floor --> a little more to the right
            gap_right = math.floor(gap) # e.g. gap = 13 --> left = 7, right = 6
        elif alignment == 'right':
            gap_right = self.__space
            gap_left = self.__width - (line_width + gap_right + 2)
        else:
            gap_left = self.__space
            gap_right = self.__space
        
        return (gap_left, gap_right)

    def __format_line(self, text, gap_left, gap_right, fill_char=" "):
        """Returns a string in the following format:
        |+gap_left++text++gap_right+|.
        Gap is filled with fill_char, default=' '"""
        return f"|{fill_char*gap_left}{text}{fill_char*gap_right}|"

    def __format_long_line(self, text, alignment, fill_char, strip):
        """Takes a long string as input. Auto linebreaks. 
        Returns a list of formatted stings."""
        # split line in words
        if strip:
            text = text.strip()

        # handle single words, so they won't be split into characters
        if " " in text:
            words = text.split()
        else:
            words = text
        
        lines = [] # new lines
        line = words[0] # current line
        
        # add all words to a line
        for word in words[1:]:
            # + 3 for  2*| and 1*' ' (for space between words)
            total_width = self.__text_len(line + word) + self.__space*2 + 3
            
            # check if line gets to wide
            if total_width <= self.__width: 
                line += f" {word}" # append word
                
                # check if last word --> line needs to be appended
                if word != words[-1]:
                    continue
            
            # calc gaps
            gap_left, gap_right = self.__calc_gaps(self.__text_len(line), alignment)
                    
            # append formatted line
            lines.append(
                self.__format_line(
                    text=line,
                    gap_left=gap_left,
                    gap_right=gap_right,
                    fill_char=fill_char
                    )
                )
                
            # set word as line for new line
            line = word
                
        # return formatted lines
        return lines

    def __format_text(self, text, alignment, fill_char, strip):
        """Takes a string as input. Inserts a linebreak after one line is full.
        Returns formatted lines."""
        # handle empty text
        if not text:
            text = fill_char
        
        # split text in predefined lines
        lines = text.splitlines()
        
        formatted_lines = [] # list of formatted lines
        
        # format each line
        for line in lines:
            if strip:
                line = line.strip()
            if not line:
                line = " "
            # calculate width
            line_width = self.__text_len(line)
            total_width = line_width + self.__space*2 + 2 # +2 for 2*|
            
            # check if formatted line would fit the width
            if total_width <= self.__width:
                # calculate gap
                gap_left, gap_right = self.__calc_gaps(line_width, alignment)
                
                # format line
                formatted_line = self.__format_line(
                    text=line,
                    gap_left=gap_left,
                    gap_right=gap_right,
                    fill_char=fill_char,
                    )
                
                # append line
                formatted_lines.append(formatted_line)
            else:
                # auto linebreak line and add line to list
                formatted_lines += self.__format_long_line(
                    text=line,
                    alignment=alignment,
                    fill_char=fill_char,
                    strip=strip
                    )
            
        return formatted_lines
        
    def pretty_print(self, text, alignment='left', fill_char=" ", strip=True):
        """Takes a string as input.
        Prints sting in following format: |+gap_left++text++gap_right+|.
        Alignment can be 'left', 'center', 'right'.
        Character to fill spaces can be chosen.
        Strip can be disabled to print pictures."""      
        # format lines
        formatted_lines = self.__format_text(
            text=text,
            alignment=alignment,
            fill_char=fill_char,
            strip=strip
            )
        
        # print lines
        print('\n'.join(line for line in formatted_lines))
    
    def print_message(self, title, message, end="", alignment="left"):
        """Takes two stings as mandatory input.
        Prints centered text with '-' as fill character for 'title' and 'end'.
        Prints leftbound text for 'message'.
        'end' is optional, prints row with '-', when no text is given."""
        print("")
        self.pretty_print(text=title, alignment='center', fill_char='-')
        self.pretty_print(text="") # empty line
        self.pretty_print(text=message, alignment=alignment)
        self.pretty_print(text="") # empty line
        self.pretty_print(text=end, alignment='center', fill_char='-')
        print("")


# execute the game
# game = Lotto6Of49() # without image
game = Lotto6Of49(lotto_machine=LOTTO_MACHINE) # with image
game.play() #start game
    
