#!/usr/bin/python3

# SIMON GAME - by peroh
# Last update: 8/14/2020

import random
import sys; print('PYTHON VERSION: ' + sys.version + ' (Python 3 or more is required)')
import re
import os; clear = lambda : os.system("cls")
from time import sleep
from colorama import init, Fore, Back, Style
init() # Initiate colorama library

class Simon:
    def __init__(self, squares_=4):
        self.sequence = []
        self.squares = squares_
        
    def print_sequence(self):
        print(self.sequence)
        
    def seq_add(self, num):
        self.sequence.append(str(num)) # TO-DO: error handling
        
    def seq_get(self):
        return self.sequence

    def seq_compare(self, usr_list):
        if usr_list == self.sequence:
            return True
        else:
            return False
    
    def seq_difference(self, usr_list):
        dct = {} # Define dictionary
        for i in range(0, len(usr_list)):
            if str(usr_list[i]) == str(self.sequence[i]):
                dct[i] = True
            else:
                dct[i] = False
        return dct

class Game:
        
    def __init__(self):
        # - Visual settings

        # -- Colors
        self.cl_color_prefix = Fore.WHITE
        self.cl_color_print = Fore.GREEN
        self.cl_color_log = Fore.CYAN
        self.cl_color_delete = Fore.RED
        self.cl_color_input = Fore.MAGENTA
        
        # -- Prefix
        self.cl_prefix = self.cl_color_prefix + Style.BRIGHT + "=" + Fore.RESET + Style.RESET_ALL
        self.cl_print_prefix = self.cl_prefix + self.cl_color_print + "+ " + Fore.RESET
        self.cl_log_prefix = self.cl_prefix + self.cl_color_log + "? " + Fore.RESET
        self.cl_delete_prefix = self.cl_prefix + self.cl_color_delete + "- " + Fore.RESET
        self.cl_input_prefix = self.cl_prefix + self.cl_color_input + "> " + Fore.RESET
        
        # Misc
        self.cl_show_log = True # Log flag
        self.running = True
        
    def g_print_log(self, msg): # Log message
        if (self.cl_show_log): print(self.cl_log_prefix + msg)
     
    def g_input(self): # Get user input
        inp = str(input(self.cl_input_prefix))
        return inp
        
    def g_print(self, msg, newline=True, usePrefix = True): # Print message
        if (newline):
            if (usePrefix):
                print(str(self.cl_print_prefix + msg))
            else:
                print(msg)
        else:
            if (usePrefix):
                print("a")
            else:
                print(msg)

    def g_prinput(self, msg): # Print and get input
        self.g_print(msg)
        inp = self.g_input()
        return inp
        
    def g_clear(self, lines): # Clears console
        clear()
        return None

    def g_clear_prompt(self, seconds=3): # Display a countdown then clear console
        for x in range (seconds, 0, -1):
            msg = self.cl_delete_prefix + "Clearing in " + str(x)
            sys.stdout.write('\r'+msg)
            sys.stdout.flush()
            sleep(1)
        self.g_clear(10)
        return None

    def g_processInput(self, usr_input): # Clears input of console input artifacts
        self.g_print_log("Dirty input: " + str(usr_input))
        clean_input = usr_input.strip("(").strip(")").split(", ")
        self.g_print_log("Clean input: " + str(clean_input))
        return clean_input
        
    def g_startGame(self, squares=4):
        self.g_print_log("Starting game...")
        simon = Simon(squares) # Initiate Simon object
        while(self.running):
            gen_sq = random.randint(1, squares) # Select random square
            simon.seq_add(gen_sq) # Append square to sequence
            self.g_print(str(Back.GREEN + "Simon shows square " + str(gen_sq) + Back.RESET))
            self.g_clear_prompt()
            usr_input = self.g_prinput("Type the sequence (separated by commas)")
            clear_input = self.g_processInput(usr_input)
            if (simon.seq_compare(clear_input)):
                # Correct sequence
                self.g_print("Right answer!")
                continue
            else:
                # Incorrect sequence
                self.g_print("\nYou lost!")
                diff = dict(simon.seq_difference(clear_input))
                self.g_print_log("User input: " + str(clear_input))
                self.g_print_log("Sequence: " + str(simon.seq_get()))
                self.g_print("Sequence was ")
                for k in diff:
                    if (diff[k] == True):             #REMEMBER TO CHECK KEY
                        print(Back.GREEN + str(simon.seq_get()[k]), end='')
                    if (diff[k] == False):
                        print(Back.RED + str(simon.seq_get()[k]), end='')
                    print(Back.RESET)
                break

def main():
    random.seed() # Generate random seed for number generator
    
    eng = Game() # Initiate game engine object

    eng.g_startGame() # Starts a match

if __name__ == "__main__":
    main()
