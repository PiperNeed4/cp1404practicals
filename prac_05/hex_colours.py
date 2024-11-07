NAME_TO_HEXADECIMAL = {'Absolute Zero': '#0048ba', 'Acid Green': '#b0bf1a', 'AliceBlue': '#f0f8ff',
                       'Alizarin crimson': '#e32636', 'Amaranth': '#e52b50', 'Amber': '#ffbf00',
                       'Amethyst': '#9966cc', 'AntiqueWhite': '#faebd7', 'AntiqueWhite1': 'ffefdb',
                       'AntiqueWhite2': '#eedfcc', 'AntiqueWhite3': '#cdc0b0'}
colour_name = input("Enter colour name: ")
while colour_name != "":
    try:
        print(NAME_TO_HEXADECIMAL[colour_name])
    except KeyError:
        print("Colour not in list")
    colour_name = input("Enter colour name: ")
