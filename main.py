"""this project is for the state handling ,preview and sorting"""
# creating an intercative enviroment using python &
# pylint for checking spellings and namecase handling

states = {
    "Alabama": {"capital": "Montgomery", "state_bird": "Yellowhammer", "state_flower": "Camellia",
                "population": "4908620"},
    "Alaska": {"capital": "Juneau", "state_bird": "Willow Ptarmigan",
               "state_flower": "Forget Me Not", "population": "734002"},
    "Arizona": {"capital": "Phoenix", "state_bird": "Cactus Wren",
                "state_flower": "Saguaro Cactus Blossom", "population": "7378490"},
    "Arkansas": {"capital": "Little Rock", "state_bird": "Mockingbird",
                 "state_flower": "Apple Blossom", "population": "3039000"},
    "California": {"capital": "Sacramento", "state_bird": "California Valley Quail",
                   "state_flower": "California Poppy", "population": "39937500"},
    "Colorado": {"capital": "Denver", "state_bird": "Lark Bunting",
                 "state_flower": "White and Lavender Columbine", "population": "5845530"},
    "Connecticut": {"capital": "Hartford", "state_bird": "Robin", "state_flower": "Mountain Laurel",
                    "population": "3563080"},
    "Delaware": {"capital": "Dover", "state_bird": "Blue Hen",
                 "state_flower": "Peach Blossom", "population": "982895"},
    "Florida": {"capital": "Tallahassee", "state_bird": "Mockingbird",
                "state_flower": "Orange Blossom",
                "population": "21993000"},
    "Georgia": {"capital": "Atlanta", "state_bird": "Mockingbird",
                "state_flower": "Orange Blossom",
                "population": "10736100"},

}

import pandas as pd

column = ['state', 'Capital', 'state Bird', 'State Flower']

df = pd.DataFrame(states)

bar_dict = {}

for key, values in states.items():
    bar_dict[key] = values['population']


def main():
    """Main """
    action = input("What do you wish to do \nshow ,update ,exit,search \n")

    if action == "search":
        search()

    elif action == "show":
        show()
    elif action == "exit":
        print(" ---exiting ...")
    elif action == "update":
        update()
    else:
        show_bar_population()
        print(" ---exiting ...")


def search():
    """handles searching through the dictionary all the states"""
    action = input("what do you want to search? \n")

    if action in states:
        print("Capital :" + str(states[action]['capital']))
        print("State population: " + str(states[action]['population']))
        print("Flower :" + str(states[action]['state_flower']) + "\n")
    else:
        print(str(action) + " does not exist in the database")
    print("---search completed --- \n \n")
    main()


def show():
    """handles showing all the states"""
    frame = pd.DataFrame(states)
    print(frame)
    main()


def update():
    """handles searching and updating the specific value given"""
    print("\n ---- Updating ---- \n")

    current_state = input("Type the state \n")

    update_population = input("Type the new total population")

    if current_state in states:
        states[current_state]['population'] = update_population
        print("__state updated successfully__")
    else:
        print("___the state was not found")
    main()


def show_bar_population():
    """bar population"""
    import matplotlib.pyplot as plt
    names = list(bar_dict.keys())
    values = list(bar_dict.values())
    plt.bar(range(len(bar_dict)), values, tick_label=names)
    plt.show()


main()
