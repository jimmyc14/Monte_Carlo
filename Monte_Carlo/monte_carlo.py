import numpy as np
import pandas as pd

class Die:
    '''
    class to make and edit a Die with n faces and weights

    '''

    def __init__(self, faces):
        '''
        init function: creates a die with n sides and automatically populates
        weights (initializes them to 1.0)

        input: number of faces of the die. Must be a numpy array

        output: The Die object
        '''
        
        if type(faces) != np.ndarray:
            raise TypeError("values for 'faces' argument must by a np.arrary!")
            
        if len(np.unique(faces)) != len(faces):
            raise ValueError("array's values are not distinct!")

        self.weights = np.ones(len(faces))

        self.die_face_weight = pd.DataFrame(self.weights, faces)


    def change_weight(self, face, weight):
        '''
        change weight of specific face of die

        2 inputs: face value to be changed (int, float, or str) must be valid face
                weight to be assigned, must be valid int, float or castable to numeric
        '''

        if face not in self.die_face_weight.index:
            raise IndexError("face value passed does not exist on die")

        try:
            weight = float(weight)
        except ValueError:
            raise TypeError("cannot cast weight value data type!")
            
        if (type(weight) not in [int,float]) and (weight < 0.0):
            raise TypeError("weight value is not correct data type or is below 0")

        self.die_face_weight.loc[face] = weight

    def roll_die(self, rolls = 1):
        '''
        roll the die one or more times

        input: amount of times die is rolled as an int(default: 1)

        output: returns list of the value(s) that were rolled, unless there is only one roll, in which it is an int
        '''
        sides = list(self.die_face_weight.index)

        roll_result = self.die_face_weight.sample(rolls, replace =True, weights = self.die_face_weight[0])
        
        if len(roll_result.index) == 1:  #I know this output isnt a list, but makes downstream work so much easier
            return(roll_result.index[0])
        return(list(roll_result.index))

    def current_state(self):
        '''
        returns the current state of the die dataframe

        no input

        output: the current state (dataframe) of the die
        '''

        return(self.die_face_weight)

class Game:
    '''
    Game made up of rolling one or more Die (from the Die Class), one or more times

    the Dies played have the same number of faces, but not necessarily the same weight
    '''

    def __init__(self, die_list):
        '''
        init the game

        input: list of die objects to play with

        output: The Game object
        '''
        
        self.die_list = die_list

    def play(self, games_to_play):
        '''
        play the game, rolls all the die in the list given in init however
        many times the user inputs

        input: integer of the amount of games to play
        '''

        #save results in list of lists, then turn into dataframe
        game_results = []
        
        for i in range(games_to_play):
            game_result = []
            for j in range(len(self.die_list)):
                game_result.append(self.die_list[j].roll_die())
            
            game_results.append(game_result)
        
        self.game_result_df = pd.DataFrame(game_results)

    def show_results(self, form = 'wide'):
        '''
        function to show results of the last game played

        input: form in which the user would like to view the results (default: "wide"), must be string

        output: the dataframe of the results of the game(s) played, type of pandas dataframe
        '''

        if form not in ['wide', 'narrow']:
            raise ValueError("form of results must be 'wide' or 'narrow' (defaulted to wide)")
        
        if form == 'wide':
            return(self.game_result_df)
        elif form == 'narrow': #elif not really needed due to value checking before

            narrow = self.game_result_df.stack()
            narrow.index = narrow.index.set_names(["Game","Die"])
            narrow = narrow.reset_index()
            
            return(narrow)

class Analyzer:
    '''

    This class analyzes the results of a game object

    '''

    def __init__(self, game):
        '''
        init the analyzer
    
        input: Game object from the game class

        output: Analyzer object
        '''
        
        if type(game) != Game:
            raise ValueError("Object is not the correct type, must be Game object!")
        
        self.the_game = game.show_results()
    
    def jackpot(self):
        '''
        see if there are any jackpots in the game
    
        no input, uses game from init
    
        output: int of number of jackpots in the game
        '''
    
        jackpots = 0
        for i in range(len(self.the_game)):
            if len(np.unique(self.the_game.loc[i])) == 1:
                jackpots += 1
        
        return(jackpots)

    def face_counts(self):
        '''
        total count of all the face values in a game

        no input

        output: dataframe of the total counts for each roll event in a game, type of pandas dataframe
        '''

        face_count_df = pd.DataFrame()
        
        for i in range(len(self.the_game)):
            unique, count = np.unique(self.the_game.loc[i], return_counts=True)
            df1 = pd.DataFrame([count], columns = unique)

            face_count_df = pd.concat([face_count_df, df1], ignore_index = True)
        face_count_df = face_count_df.fillna(0).astype(int)

        return(face_count_df)

    def combo_count(self):
        '''
        count of unique combinations in each roll

        no input

        output: unique combinations counts for each roll event in game, output pandas dataframe
        '''
        all_combos = []
        
        for i in range(len(self.the_game)):
            combo = np.sort(self.the_game.loc[i])
            all_combos.append(combo)
        unique, count = np.unique(all_combos, axis=0, return_counts = True)

        combo_df = pd.DataFrame({'Count': count}, index=pd.MultiIndex.from_arrays(unique.T))

        return(combo_df)

    def permutations(self):
        '''
        count of unique permutations in each roll

        no input

        output: unique permutations counts for each roll event in game, output pandas dataframe
        '''
        
        vals = self.the_game.value_counts()
        perm_df = pd.DataFrame(vals)
        return(perm_df)
