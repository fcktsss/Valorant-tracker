import pandas as pd
import numpy as np

from api import response
def calculate_mean(data):
    """
    data = { 'Joueur', 'Rank', 'Hs', 'Token' }
    Calculate the mean of the 'Rank' and 'Hs' values in the data dictionary.
    """
    rank_values = [item['Rank'] for item in data]
    hs_values = [item['Hs'] for item in data]
    mean_rank = np.mean(rank_values)
    mean_hs = np.mean(hs_values)
    return mean_rank, mean_hs

calculate_mean([
    {'Joueur': 'Player1', 'Rank': 5, 'Hs': 10, 'Token': 'token1'},
    {'Joueur': 'Player2', 'Rank': 7, 'Hs': 15, 'Token': 'token2'},
    {'Joueur': 'Player3', 'Rank': 6, 'Hs': 12, 'Token': 'token3'},
    {'Joueur': 'Player4', 'Rank': 6, 'Hs': 12, 'Token': 'token4'},
    {'Joueur': 'Player5', 'Rank': 6, 'Hs': 12, 'Token': 'token5'},
        
])

