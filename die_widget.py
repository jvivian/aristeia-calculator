from ipywidgets import HBox, VBox, RadioButtons, Accordion

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

def aristeia_dice_widget():
    a = create_die_widgets()
    d = create_die_widgets()
    accordion = Accordion(children=[display_widgets(a), display_widgets(d)])
    accordion.set_title(0, 'Attacker')
    accordion.set_title(1, 'Defender')
    return accordion

def dict_from_accordion(accordion):
    a = {x.description: x for x in accordion.children[0].children}
    d = {x.description: x for x in accordion.children[1].children}
    return a, d