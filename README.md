# Lab 01 - Snakes Cafe

**Author**: Kassie Bradshaw
**Version**: 1.0.0

## Collaborations and Credit

* Help from TA Ben Hill
* Collaborated with Garfield Grant
* [For help with verification in terms of case-sensitivity](https://stackoverflow.com/questions/50563844/access-python-dictionary-with-case-insensitive-string)

## Overview

Command line utility which will mimic the functionality of a point of sale restaurant system using basic Python tools and understanding of the basics of the language.

### Feature Tasks & Requirements

* [x] When run, the program should print an intro message and the menu for the restaurant
* [x] The restaurant's menu should include appetizers, entrees, desserts, and beverages
* [x] The program should prompt the user for an order
* [x] When a user enters an item, the program should print an acknowledgement of their input
* [x] The program should tell the user how to exit
* [x] The program's content should match included sample exactly
  * [x] Actually, there's one tiny spot that should be different - see if you can spot it.
  * [x] The ```>``` character represents user input line and should be printed out with a trailing space

### Stretch Goals

* [x] Print out a summary of complete order
* [x] Only allow ordering items on the menu
* [ ] Allow ordering items not on menu but give custom reply

## Getting Started

Inside your terminal's working folder type/run:

* ```poetry new snakes-cafe```
* ```cd snakes-cafe```
* ```poetry add --dev black --allow-prereleases```
* ```touch snakes_cafe/snakes_cafe.py```
* ```mv README.rst README.md```
* ```git init```
* ```git add .```
* ```git commit -m "first commit"```

On GitHub, create an empty repository called: ```snakes-cafe```

* Do not initialize with README, license or gitignore.
* The next screen on GitHub will have a "Quick Setup" section with a URL available to copy. Copy it.

Return to your terminal and type:

* ```git remote add origin the_url_you_copied_that_ends_with_git```
* ```git push -u origin master``` [or ```main``` depending on your branch name conventions]

## Change Log

06/05/2021:

* Initial commit
  * Lab started
* 2nd commit
  * Decorator function, decorated intro & order prompt
  * Rendering lists of menu items
  * Taking user input for order and returning a prompt
  * Rewrote code using dedent and a dictionary

06/06/2021:

* 3rd Commit
  * Removed decorator functions for simplicity
  * Removed list_menu function now that I'm rendering menu in a dictionary rather than as lists
  * Added prompt when user tries to order something that's not on the menu
  * Case-insensitive verification comparing user's input to menu, and to user's current order
  * Created prompt notifying user of entire order upon quitting, and a custom message if they didn't order anything

[PR for this lab submission](https://github.com/kassiebradshaw/snakes-cafe/pull/1)

[Python Submission Instructions Link](https://codefellows.github.io/code-401-python-guide/reference/submission-instructions/labs/)