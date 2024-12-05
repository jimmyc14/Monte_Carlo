# Monte Carlo

A simple Monte Carlo simulator that uses a die to play a game, and then analyze it. 

There are 3 classes in this module, a Die class, a Game class, and a Analyzer class. 

The general flow of usage is as follows:

Create Die -> Play Game -> Analyze Game

A Die can have n number of sides, and weights can be applied to a specific face after to change the odds of the die.

# Installing the Package

``` pip install MonteCarlo ```

# Example of Use

## Die Class Example

The following example shows how to create 2 die, one that represents a coin, and one that represents a 6-sided die. 

```
import numpy as np

from Monte_Carlo import monte_carlo

# create die face arrays
die1_face = np.array([1,2]) # a coin
die2_face = np.array([1,2,3,4,5,6]) # 6 sided die

die1 = monte_carlo.Die(die1_face) # Create Die object, weights are initized to 1.0 for all sides
die2 = monte_carlo.Die(die2_face)

die1_state = die1.current_state() #save current state of the Die Object
die2_state = die2.current_state()

print(die1_state)
print(die2_state)
```

Output:

```
     0
1  1.0
2  1.0
     0
1  1.0
2  1.0
3  1.0
4  1.0
5  1.0
6  1.0
```

## Game Class Example

The following code creates 2 Die objects representing a 6 faced die, then creates a Game object from those Die. We then roll the die 4 times within that game and show the results. 

```
import numpy as np

from Monte_Carlo import monte_carlo

die1_face = np.array([1,2,3,4,5,6]) # 6 sided die
die2_face = np.array([1,2,3,4,5,6])

die1 = monte_carlo.die(die1_face) # Create Die object, weights are initized to 1.0 for all sides
die2 = monte_carlo.die(die2_face)

game1 = monte_carlo.Game([die1, die2]) # creating Game object. Number of faces/sides of die objects must be the same 

game1.play(4) # play the game 4 times. Will roll each die 4 times. 

print(game1.show_results()) # show the results of the played game above as a pandas dataframe
```

Output:

```
   0  1
0  1  6
1  6  1
2  4  2
3  3  5
```

## Analyzer Class Example

The following code replays a game created in the previous example 4 times, then creates an Analyzer object from that game. It then checks to see if there are any jackpots, and shows the face counts for the game. 

```
game1.play(4) # using the same game as above play the game 4 more times. Will roll each die 4 times. 
print(Game1.show_results()) # show the results of the played game above

analyze1 = monte_carlo.Analyzer(game1) # create an analyzer object from the previous game1

print(analyze1.jackpot()) # checks the game object for any jackpots i.e. the die rolled the same number in a play

print(analyze1.face_counts()) # shows the totals for the unique values rolled each play
```

Output:

```
   0  1
0  1  5
1  3  3
2  1  1
3  5  2

2

   1  5  3  2
0  1  1  0  0
1  0  0  2  0
2  2  0  0  0
3  0  1  0  1
```
As seen from the output above, our game had 2 jackpots in roll 1 (3,3) and roll 2(1,1).

# API

## Die

### init

Called when object is created. Creates the Die object from a numpy list of values that serve as the name of the face. The length of the list is the number of faces. Automatically initalizes weights for each face to 1.0

        '''
        init function: creates a die with n sides and automatically populates
        weights (initializes them to 1.0)

        input: number of faces of the die. Must be a numpy array

        output: The Die object
        '''
Input: A numpy array with the faces of the die. 

Output: The Die object

Usage :
```
die1 = monte_carlo.Die(np.array([1,2,3,4]))
```

### change_weight

Used to change the weight value of a specific face on a die. Has 2 inputs, one with the unique name of the face (int, float, or string) and the weight to be changed (int,float, or castable string). 

        '''
        change weight of specific face of die

        2 inputs: face value to be changed (int, float, or str) must be valid face
                weight to be assigned, must be valid int, float or castable to numeric
        '''
Inputs: The unique name of the face (int, float, or string), and the weight to be changed (int,float, or castable string). 

No Output

Useage:
```
die1 = monte_carlo.Die(np.array([1,2,3,4]))

die1.change_weight(2, 50) # change face 2 to a weight of 50
```

### roll_die

Used to roll the Die object. Input is an int of the amount of rolls the user would like to do, and is defaulted to one. Outputs a pandas dataframe of results. 

        '''
        roll the die one or more times

        input: amount of times die is rolled as an int(default: 1)

        output: returns list of the value(s) that were rolled, unless there is only one roll, in which it is an int
        '''
Inputs: Int of the amount of rolls to do (optional, defaulted to 1)

Output: Outputs list of values from each rolls. Unless there is only one roll, in which it returns the value rolled. 

Useage:
```
die1 = monte_carlo.Die(np.array([1,2,3,4]))

print(die1.roll(5))
```
Output:
```
[1, 3, 1, 1, 2]
```

### current_state

Used to show the current state of the die object. There is no input, and it outputs the current pandas dataframe of the die faces and weights.

        '''
        returns the current state of the die dataframe

        no input

        output: the current state (dataframe) of the due
        '''

No Input

Output: Current Die state as a pandas dataframe. 

Useage: 
```
die1 = monte_carlo.Die(np.array([1,2,3,4]))

die1.change_weight(2, 50) # change face 2 to a weight of 50

print(die1.current_state()) # show state before change

die1.change_weight(2,50)

print(die1.current_state())
```
Output:
```
     0
1  1.0
2  1.0
3  1.0
4  1.0

      0
1   1.0
2  50.0
3   1.0
4   1.0
```

## Game

### init

Creates the game object. Uses a list of Die objects to do so. Die objects MUST have the same number of faces. 

        '''
        init the game

        input: list of die objects to play with

        output: The Game object
        '''
Input: list of die objects

Output: The Game object

Usage:
```
six_sided = np.array([1,2,3,4,5,6]) # 6 sided die

die1 = monte_carlo.Die(six_sided) # Create Die object, weights are initized to 1.0 for all sides
die2 = monte_carlo.Die(six_sided)
die3 = monte_carlo.Die(six_sided)

game1 = monte_carlo.Game([die1, die2, die3]) # creating Game object. Number of faces/sides of die objects must be the same
```

### play

Plays a game n number of times with the die in the game object. Inputs a int with the amount of times to roll the die. Calls from the roll_die method in Die. Saves the game internally.

        '''
        play the game, rolls all the die in the list given in init however
        many times the user inputs

        input: integer of the amount of games to play
        '''
Input: Int of the amount of times to roll the die in the game

No output

Usage:
```
game1.play(5) # will roll the 3 die from the game object made above 5 times. (15 total rolls)
```

### show_results

Used to show the results from the last played game stored in the Game object. Takes the argument for the form desired for viewing: 'wide' or 'narrow'. Defaulted to 'wide'. Outputs a pandas dataframe with game results. 

        '''
        function to show results of the last game played

        input: form in which the user would like to view the results (default: "wide"), must be string

        output: the dataframe of the results of the game(s) played, type of pandas dataframe
        '''
Input: String value of 'wide' or 'narrow' (optional, defaulted as 'wide')

Output: Pandas dataframe of last played game results. 

Usage:
```
game1.play(5)

print(game1.show_results())

print(game1.show_results('narrow'))
```
Output:
```
   0  1  2
0  4  3  6
1  3  3  1
2  3  3  3
3  1  2  1
4  5  4  6

    Game  Die  0
0      0    0  4
1      0    1  3
2      0    2  6
3      1    0  3
4      1    1  3
5      1    2  1
6      2    0  3
7      2    1  3
8      2    2  3
9      3    0  1
10     3    1  2
11     3    2  1
12     4    0  5
13     4    1  4
14     4    2  6
```

The first dataframe is the default wide view, and the second the narrow view. 

## Analyzer

### init

Created the Analyzer object using a Game object. Inputs a game object, outputs an Analyzer object. 

        '''
        init the analyzer
    
        input: Game object from the game class

        output: Analyzer object
        '''
Input: Game Class object

Ouput: Analyzer Class object

Usage:
```
# using the game1 object created above
analyze1 = monte_carlo.Analyzer(game1)
```

### jackpot

Looks for jackpots within the game played. A jackpot is described as all the values rolled in a single roll of die having the same value. For example, if 3 six sided die are rolled 1 time, their values would have to all be the same. Searches the entire game for the number of jackpots. No input, output in int of the amount of jackpots. 

        '''
        see if there are any jackpots in the game
    
        no input, uses game from init
    
        output: int of number of jackpots in the game
        '''
No Input

Ouput: Int of the amount of jackpots found

Usage:
```
game1.play(5) #replay the game with 5 rolls using 3 six sided die

print(game1.show_results()) #show results of game

analyze1 = monte_carlo.Analyzer(game1) # create an analyzer object from the previous game1

print(analyze1.jackpot())
```
Output:
```
   0  1  2
0  1  1  1
1  6  2  3
2  1  4  1
3  3  1  1
4  3  5  3

1
```
From the output above, we can see that there was 1 jackpot in the game played. Looking at the results of the game above that, we can see it happened on Roll 0 (1,1,1)

### face_counts

Produces a dataframe of all the unique face values found in the game. No input, outputs as a pandas dataframe. 

        '''
        total count of all the face values in a game

        no input

        output: dataframe of the total counts for each roll event in a game, type of pandas dataframe
        '''
No input

Output: Pandas dataframe of the face value counts

Usage:
```
game1.play(5) #replay the game with 5 rolls using 3 six sided die

print(game1.show_results()) #show results of game

analyze1 = monte_carlo.Analyzer(game1) # create an analyzer object from the previous game1

print(analyze1.face_counts()) 
```
Output:
```
   0  1  2
0  2  4  1
1  6  6  2
2  2  3  4
3  3  2  3
4  5  4  6

   1  2  4  6  3  5
0  1  1  1  0  0  0
1  0  1  0  2  0  0
2  0  1  1  0  1  0
3  0  1  0  0  2  0
4  0  0  1  1  0  1
```
The first dataframe shown is the results from the game. The second dataframe is the sum of the unique values for each roll. 

### combo_count

Sums up the total combos found in the game. These are not order specific. For example (0,1) and (1,0) count as only 1 combination of numbers, 0 and 1. There is no input, outputs as a multiindexed pandas dataframe. 

        '''
        count of unique combinations in each roll

        no input

        output: unique combinations counts for each roll event in game, output pandas dataframe
        '''
No input

Output: MultiIndex pandas dataframe with every unique combination. 

Usage:
```
game1.play(5) #replay the game with 5 rolls using 3 six sided die

print(game1.show_results()) #show results of game

analyze1 = monte_carlo.Analyzer(game1) # create an analyzer object from the previous game1

print(analyze1.combo_count())
```
Output:
```
   0  1  2
0  1  1  1
1  5  1  5
2  1  5  5
3  6  2  6
4  3  3  4

       Count
1 1 1      1
  5 5      2
2 6 6      1
3 3 4      1
```
From this output, we can see that there are 4 unique combinations found, including one jackpot (1,1,1). Notice how rolls 1 and 2 had the values (5,1,5) and (1,5,5) respectively, but count as one unique combination in the 2nd dataframe. 

### permutations

Sums up the total permutations found in the game. These ARE order specific. For example (0,1) and (1,0) count as 2 different permutations. There is no input, outputs as a multiindexed pandas dataframe. 

No input

Output: MultiIndex pandas dataframe with every unique permutation. 

Usage:
```
game1.play(5) #replay the game with 5 rolls using 3 six sided die

print(game1.show_results()) #show results of game

analyze1 = monte_carlo.Analyzer(game1) # create an analyzer object from the previous game1

print(analyze1.permutations())
```
Output:
```
   0  1  2
0  1  6  4
1  1  6  4
2  6  6  1
3  1  1  2
4  5  3  2

       count
0 1 2
1 6 4      2
  1 2      1
5 3 2      1
6 6 1      1
```
Notice in our output how the permutation (1,6,4) occured twice. 
