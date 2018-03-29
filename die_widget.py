from ipywidgets import HBox, VBox, RadioButtons

die_n = {'Black': 3,
        'Orange': 3,
        'Blue': 3,
        'Red': 1,
        'Green': 1}

die_r = {x: RadioButtons(options=range(die_n[x] + 1), description=x) 
               for x in die_n.keys()}

bs = VBox([die_r[x] for x in die_r.keys() if 'Blue' in x])
ks = VBox([die_r[x] for x in die_r.keys() if 'Black' in x])
os = VBox([die_r[x] for x in die_r.keys() if 'Orange' in x])
r = VBox([die_r[x] for x in die_r.keys() if 'Red' in x])
g = VBox([die_r[x] for x in die_r.keys() if 'Green' in x])

output = HBox([bs, ks, os, r, g])