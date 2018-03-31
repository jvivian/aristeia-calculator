import pandas as pd

columns = ['hit', 'special', 'defense', 'crit', 'crit_defense']
die = {}
die['Red'] = pd.DataFrame([[0,0,0,1,0], [1,1,0,0,0], [1,1,0,0,0],
                    [1,0,0,0,0], [2,1,0,0,0], [0,0,0,0,0]], columns=columns)

die['Green'] = pd.DataFrame([[0,0,0,0,1], [0,1,2,0,0], [0,1,1,0,0],
                      [0,0,1,0,0], [0,0,0,0,0], [0,0,0,0,0]], columns=columns)

die['Orange'] = pd.DataFrame([[2,1,0,0,0], [1,0,0,0,0], [0,1,1,0,0],
                       [1,1,1,0,0], [0,0,1,0,0], [0,0,0,0,0]], columns=columns)

die['Blue'] = pd.DataFrame([[0,1,2,0,0], [1,1,1,0,0], [1,0,1,0,0],
                     [0,0,1,0,0], [1,1,0,0,0], [0,0,0,0,0]], columns=columns)

die['Yellow'] = pd.DataFrame([[1,1,1,0,0], [1,2,0,0,0], [0,1,1,0,0], 
                       [0,1,0,0,0], [0,1,0,0,0], [0,0,0,0,0]], columns=columns)

die['Black'] = pd.DataFrame([[0,0,1,0,0], [0,0,1,0,0], [0,0,1,0,0],
                      [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]], columns=columns)