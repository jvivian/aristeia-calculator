import random

from ipywidgets import Checkbox, VBox, Accordion

core = ['Hexxar',
        'Lunah',
        'Gata',
        '8-Ball',
        'Mistubishi',
        'Wild Bill',
        'Maximus',
        'Lunah',
        'Pavarti']

sof = ['Valkyrie',
       'Hannibal',
       'Senor Massacre',
       'Laxmee']

sm = ['Taowu',
      'Kosmo',
      'Mutair',
      'Mendoza']

hf = ['Eclypse',
      'Dart',
      'Bixie',
      'Prysm']

maps = ['Blitz',
        'Carnage',
        'Conquest',
        'King of the Hill',
        'Scorched Erf']


def generate_initial_teams(aristos):
    """Generate two teams """
    aristos = set(aristos)
    first_team = random.sample(aristos, 4)
    second_team = random.sample(
        aristos.difference(set(first_team)), 4)
    print('1st Team: {}\n2nd Team: {}'.format(first_team, second_team))
    return set(first_team), set(second_team)


def create_checkbox(team):
    return VBox([Checkbox(description=x) for x in team])


def create_mulligan(team1, team2):
    check1 = create_checkbox(team1)
    check2 = create_checkbox(team2)
    accord = Accordion(children=[check1, check2])
    accord.set_title(0, 'Team 1')
    accord.set_title(1, 'Team 2')
    return accord, check1, check2


def run_mulligan(aristos, team1, check1, team2, check2):
    aristos = set(aristos)
    # Identify who to mulligan
    c1 = [x.description for x in check1.children if x.value == True]
    c2 = [x.description for x in check2.children if x.value == True]

    # Reset teams and release mulligans back into pool
    team1 = set(team1).difference(set(c1))
    team2 = set(team2).difference(set(c2))
    pool = aristos.difference(team1.union(team2))

    # Randomize new teams
    team1 = team1.union(set(random.sample(pool, len(c1))))
    team2 = team2.union(set(random.sample(pool.difference(team1), len(c2))))

    print('1st Team: {}\n2nd Team: {}'.format(team1, team2))
    # return team1, team2


def pick_map(maps):
    return random.choice(maps)
