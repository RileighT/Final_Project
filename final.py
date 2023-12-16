import pandas as pd 
import unittest
import re
import sqlite3
import argparse

#module 1
class Player:
    """
    A class that represents an NHL player.

    Attributes:
    - name (str): The name of the player.
    - team (str): The team to which the player belongs.
    - position (str): The playing position of the player (e.g., Forward, Defense).
    - goals (int): The number of goals scored by the player.
    - penalty_minutes (int): The total penalty minutes accumulated by the player.

    Methods:
    - None
    """
    def __init__(self, name, team, position, goals, penalty_minutes):
        self.name = name
        self.team = team
        self.position = position
        self.goals = goals
        self.penalty_minutes = penalty_minutes

class Team:
    """
    A class that represents an NHL team.

    Attributes:
    - name (str): The name of the team.
    - players (list): A list of Player objects representing the team's players.

    Methods:
    - None
    """
    def __init__(self, name, players):
        self.name = name
        self.players = players
 
#module 2
class DataHandler:
    """
    A class for handling NHL player data, including skaters and goalies.

    Attributes:
    None

    Methods:
    - read_skaters_data(file_path): Reads skaters data from a CSV file.
    - filter_skaters_by_position(skaters, position): Filters skaters based on their playing position.
    - calculate_points(skaters): Calculates total points for each skater.
    - top_players_by_points(skaters, num_players=10): Returns the top players based on points.
    - read_goalies_data(file_path): Reads goalies data from a CSV file.
    - calculate_save_percentage(goalies): Calculates save percentage for each goalie.
    - top_goalies_by_save_percentage(goalies, num_goalies=5): Returns the top goalies based on save percentage.
    """
    def __init__(self):
        pass
    def read_skaters_data(self,file_path):
        """
        Reads skaters data from a CSV file.

        Parameters:
        - file_path (str): The path to the CSV file containing skaters data.

        Returns:
        - A DataFrame containing skaters data.
        """
        skaters = pd.read_csv(file_path)
        return skaters

    def filter_skaters_by_position(self, skaters, position):
        """
        Filters skaters based on their playing position.

        Parameters:
        - skaters (pandas.DataFrame): DataFrame containing skaters data.
        - position (str): The playing position to filter by.

        Returns:
        - A filtered DataFrame containing skaters with the specified position.
        """
        return skaters[skaters['Pos'] == position]

    def calculate_points(self,skaters):
        """
        Calculates total points for each skater.

        Parameters:
        - skaters (pandas.DataFrame): DataFrame containing skaters data.

        Returns:
        - A DataFrame with an additional 'Points' column representing total points.
        """
        skaters['Points'] = skaters['G'] + skaters['A']
        return skaters[['Player Name', 'Points']]

    def top_players_by_points(self,skaters, num_players=5):
        """
        Returns the top players based on points.

        Parameters:
        - skaters (pandas.DataFrame): DataFrame containing skaters data.
        - num_players (int): The number of top players to return.

        Returns:
        - The top players based on points.
        """
        sorted_skaters = skaters.sort_values(by='Points', ascending=False)
        return sorted_skaters.head(num_players)

    def read_goalies_data(self,file_path):
        """
        Reads goalies data from a CSV file.

        Parameters:
        - file_path (str): The path to the CSV file containing goalies data.

        Returns:
        - A DataFrame containing goalies data.
        """
        goalies = pd.read_csv(file_path)
        return goalies

    def calculate_save_percentage(self,goalies):
        """
        Calculates save percentage for each goalie.

        Parameters:
        - goalies (pandas.DataFrame): DataFrame containing goalies data.

        Returns:
        - A DataFrame with an additional 'Save Percentage' column.
        """
        goalies['SavePercentage'] = goalies['SV'] / goalies['SA']
        return goalies[['Player Name', 'SavePercentage']]

    def top_goalies_by_save_percentage(self,goalies, num_goalies=5):
        """
        Returns the top goalies based on save percentage.

        Parameters:
        - goalies (pandas.DataFrame): DataFrame containing goalies data.
        - num_goalies (int): The number of top goalies to return.

        Returns:
        - The top goalies based on save percentage.
        """
        sorted_goalies = goalies.sort_values(by='SavePercentage', ascending=False)
        return sorted_goalies.head(num_goalies)

#module 3
class TestDataHandler(unittest.TestCase):
    """
    Unit tests for the DataHandler class.

    Attributes:
    None

    Methods:
    - test_read_skaters_data(): Tests the read_skaters_data method of the DataHandler class.
    """
    def test_read_skaters_data(self):
        """
        Tests the read_skaters_data method of the DataHandler class.

        The test checks if the read_skaters_data method reads skaters data from a CSV file
        and returns a DataFrame with a length greater than 0.

        Returns:
        None
        """
        file_path = 'data/nhl-stats_1.csv'
        skaters = DataHandler.read_skaters_data(file_path)
        self.assertGreater(len(skaters), 0)

#module 4
class Analyzer:
    """
    A class for analyzing NHL player data, including skaters and goalies.

    Attributes:
    None

    Methods:
    - analyze_skaters(skaters_data): Analyzes skaters' data and returns the top forwards.
    - analyze_goalies(goalies_data): Analyzes goalies' data and returns the top goalies.
    """

    def analyze_skaters(self,skaters_data):
        """
        Analyzes the skaters data and returns the top forwards.

        Parameters:
        - skaters_data (str): File path to the skaters' data CSV file.

        Returns:
        The top forwards based on Goals percentage.
        """
        skaters_df = DataHandler.read_skaters_data(skaters_data)
        forwards = DataHandler.filter_skaters_by_position(skaters_df, 'Forward')
        top_forwards = DataHandler.top_players_by_xGoals_percentage(forwards, num_players=5)
        return top_forwards

    def analyze_goalies(self,goalies_data):
        """
        Analyzes the goalies data and returns the top goalies.

        Parameters:
        - goalies_data (str): File path to the goalies' data CSV file.

        Returns:
        Top goalies based on save percentage.
        """
        # Reading goalies data from the CSV file
        goalies_df = DataHandler.read_goalies_data(goalies_data)
        # Finding the top goalies based on save percentage
        top_goalies = DataHandler.top_goalies_by_save_percentage(goalies_df, num_goalies=3)
        return top_goalies

#module 5
class TestAnalyzer(unittest.TestCase):
    """
    Unit tests for the Analyzer class.

    Attributes:
    None

    Methods:
    - test_analyze_skaters(): Tests the analyze_skaters method of the Analyzer class.
    - test_analyze_goalies(): Tests the analyze_goalies method of the Analyzer class.
    """
    def test_analyze_skaters(self):
        """
        Tests the analyze_skaters method of the Analyzer class.

        The test checks if the analyze_skaters method correctly analyzes skaters' data
        and returns the expected number of top forwards.

        Returns:
        None
        """
        # File path to the skaters' data CSV file
        skaters_data = 'data/nhl-stats_1.csv'
        # Calling the analyze_skaters method to analyze skaters' data
        result = Analyzer.analyze_skaters(skaters_data)
        # Assertion: Check if the length of the result is equal to 5
        self.assertEqual(len(result), 5)

    def test_analyze_goalies(self):
        """
        Tests the analyze_goalies method of the Analyzer class.

        The test checks if the analyze_goalies method correctly analyzes goalies' data
        and returns the expected number of top goalies.

        Returns:
        None
        """
        # File path to the goalies' data CSV file
        goalies_data = 'data/nhl-stats_2.csv'
        # Calling the analyze_goalies method to analyze goalies' data
        result = Analyzer.analyze_goalies(goalies_data)
        # Check if the length of the result is equal to 3
        self.assertEqual(len(result), 3)

#module 6

class TestAnalyzer(unittest.TestCase):

    def test_sort_players_by_stat(self):
        players = [Player("Player1", "BOS", "Forward", 30, 40),
                   Player("Player2", "WSH", "Forward", 25, 20),
                   ]
        sorted_players = Analyzer.sort_players_by_stat(players, 'penalty_minutes')
        self.assertEqual(sorted_players[0].name, "Player2")

    def test_unique_teams(self):
        players = [Player("Player1", "COL", "Forward", 30, 40),
                   Player("Player2", "PIT", "Forward", 25, 20),
                   
                   ]
        unique_teams = Analyzer.unique_teams(players)
        self.assertEqual(len(unique_teams), 2)

    def analyze_skaters(self, skaters_data):
            skaters_df = DataHandler.read_skaters_data(skaters_data)
            forwards = DataHandler.filter_skaters_by_position(skaters_df, 'Forward')
            top_forwards = DataHandler.top_players_by_points(forwards, num_players=5)
            return top_forwards

    def analyze_goalies(self, goalies_data):
        goalies_df = DataHandler.read_goalies_data(goalies_data)
        top_goalies = DataHandler.top_goalies_by_save_percentage(goalies_df, num_goalies=3)
        return top_goalies

#module 7
class Goalie(Player):
    def __init__(self, name, country, saves, goals_allowed):
        super().__init__(name, country, position="Goalie", goals=0, penalty_minutes=0)
        self.saves = saves
        self.goals_allowed = goals_allowed

#module 8
class DataHandler:

    def extract_team_code(player_info):
        match = re.search(r'\(([A-Z]+)\)', player_info)
        if match:
            return match.group(1)
        return None

#module 9 - GIT Hub. I am incoperating this module by uplaoding my progress and final into git hub

#module 10
class DataHandler:
    def create_dataframe(players):
        return pd.DataFrame(players)

#module 11
class DataHandler:
    def create_database(players):
        conn = sqlite3.connect('nhl_players.db')
        c = conn.cursor()

        c.execute('CREATE TABLE IF NOT EXISTS players (name TEXT, country TEXT, position TEXT, goals INTEGER, penalty_minutes INTEGER)')
        
        for player in players:
            c.execute('INSERT INTO players VALUES (?, ?, ?, ?, ?)', (player.name, player.country, player.position, player.goals, player.penalty_minutes))

        conn.commit()
        conn.close()

def goal_scorers_analysis(data_handler,skaters_data):
    skaters_df = data_handler.read_skaters_data(skaters_data)
    top_scorers = data_handler.top_players_by_points(skaters_df, num_players=10)
    print("\nTop Goal Scorers:")
    print(top_scorers)

def goalies_analysis(goalies_data):
    goalies_df = DataHandler.read_goalies_data(goalies_data)
    top_goalies = DataHandler.top_goalies_by_save_percentage(goalies_df, num_goalies=5)
    print("\nTop Goalies:")
    print(top_goalies)

def team_analysis(skaters_data, goalies_data):
    team_name = input("Enter the team name: ")
    skaters_df = DataHandler.read_skaters_data(skaters_data)
    goalies_df = DataHandler.read_goalies_data(goalies_data)
    
    team_players = DataHandler.filter_players_by_team(skaters_df, team_name)
    team_goalies = DataHandler.filter_goalies_by_team(goalies_df, team_name)

    print(f"\nPlayers from {team_name}:")
    print(team_players)

    print(f"\nGoalies from {team_name}:")
    print(team_goalies)

def hitters_analysis(skaters_data):
    skaters_df = DataHandler.read_skaters_data(skaters_data)
    top_hitters = DataHandler.top_players_by_stat(skaters_df, 'Hits', num_players=10)
    print("\nTop Hitters:")
    print(top_hitters)

def penalty_minutes_analysis(skaters_data):
    skaters_df = DataHandler.read_skaters_data(skaters_data)
    top_penalty_minutes = DataHandler.top_players_by_stat(skaters_df, 'PIM', num_players=10)
    print("\nPlayers with the Highest Penalty Minutes:")
    print(top_penalty_minutes)

#module 12
def main():
    parser = argparse.ArgumentParser(description="NHL Data Analysis")
    parser.add_argument("analysis type", choices=["-tgs", "-bg", "-pbt", "-bh", "-hpm"],
                        help="Specify the type of analysis (top goal scorers, best goalies, players by team, biggest hitters, highest penalty minutes)")

    args = parser.parse_args()

    skaters_data = 'data/nhl-stats_1.csv'
    goalies_data = 'data/nhl-stats_2.csv'

    if args == "-tgs":
        goal_scorers_analysis(skaters_data)
    elif args == "-bg":
        goalies_analysis(goalies_data)
    elif args == "-pbt":
        team_analysis(skaters_data, goalies_data)
    elif args == "-bh":
        hitters_analysis(skaters_data)
    elif args == "-hpm":
        penalty_minutes_analysis(skaters_data)
    else:
        print("Invalid choice. Please select a valid option.")

def skaters_analysis(skaters_data):
    skaters_df = DataHandler.read_skaters_data(skaters_data)
    skaters_df['Points'] = skaters_df['G'] + skaters_df['A']
    top_goal_scorers = skaters_df.sort_values(by='Points', ascending=False).head(10)
    print("\nTop 10 Goal Scorers:")
    print(top_goal_scorers[['Player Name', 'Points']])

if __name__ == "__main__":
    main()
