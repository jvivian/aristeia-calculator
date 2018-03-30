from ipywidgets import HBox, VBox, RadioButtons

die_n = {'Black': 3,
        'Orange': 3,
        'Blue': 3,
        'Red': 1,
        'Green': 1,
        'Yellow': 3}

def create_die_widgets():
    return  {x: RadioButtons(options=range(die_n[x] + 1), description=x) 
             for x in die_n.keys()}

def display_widgets(d):
    return HBox([y for x, y in sorted(d.iteritems())])