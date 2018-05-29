import pandas as pd

columns = ['hit', 'special', 'defense', 'crit', 'crit_defense']
die = {'Red': pd.DataFrame([[0, 0, 0, 1, 0], [1, 1, 0, 0, 0], [1, 1, 0, 0, 0],
                            [1, 0, 0, 0, 0], [2, 1, 0, 0, 0], [0, 0, 0, 0, 0]], columns=columns),

       'Green': pd.DataFrame([[0, 0, 0, 0, 1], [0, 1, 2, 0, 0], [0, 1, 1, 0, 0],
                              [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], columns=columns),

       'Orange': pd.DataFrame([[2, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 1, 1, 0, 0],
                               [1, 1, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]], columns=columns),

       'Blue': pd.DataFrame([[0, 1, 2, 0, 0], [1, 1, 1, 0, 0], [1, 0, 1, 0, 0],
                             [0, 0, 1, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]], columns=columns),

       'Yellow': pd.DataFrame([[1, 1, 1, 0, 0], [1, 2, 0, 0, 0], [0, 1, 1, 0, 0],
                               [0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0]], columns=columns),

       'Black': pd.DataFrame([[0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0],
                              [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], columns=columns)}
