import pandas as pd

columns = ['hit', 'special', 'defense', 'crit', 'crit-defense']
die = {}
die['red'] = pd.DataFrame([[0,0,0,1,0], [1,1,0,0,0], [1,1,0,0,0],
                    [1,0,0,0,0], [2,1,0,0,0], [0,0,0,0,0]], columns=columns)

die['green'] = pd.DataFrame([[0,0,0,0,1], [0,1,2,0,0], [0,1,1,0,0],
                      [0,0,1,0,0], [0,0,0,0,0], [0,0,0,0,0]], columns=columns)

die['orange'] = pd.DataFrame([[2,1,0,0,0], [1,0,0,0,0], [0,1,1,0,0],
                       [1,1,1,0,0], [0,0,1,0,0], [0,0,0,0,0]], columns=columns)

die['blue'] = pd.DataFrame([[0,1,2,0,0], [1,1,1,0,0], [1,0,1,0,0],
                     [0,0,1,0,0], [1,1,0,0,0], [0,0,0,0,0]], columns=columns)

die['yellow'] = pd.DataFrame([[1,1,1,0,0], [1,2,0,0,0], [0,1,1,0,0], 
                       [0,1,0,0,0], [0,1,0,0,0], [0,0,0,0,0]], columns=columns)

die['black'] = pd.DataFrame([[0,0,1,0,0], [0,0,1,0,0], [0,0,1,0,0],
                      [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]], columns=columns)