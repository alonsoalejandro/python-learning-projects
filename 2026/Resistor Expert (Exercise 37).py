list_colors = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}

list_tolerance = {
    "grey": "0.05%",
    "violet": "0.1%",
    "blue": "0.25%",
    "green": "0.5%",
    "brown": "1%",
    "red": "2%",
    "gold": "5%",
    "silver": "10%",
}

def resistor_label(colors):
    if len(colors) == 1:
        return "0 ohms"

    tolerance = list_tolerance[colors[-1]]

    if len(colors) == 4:
        value = list_colors[colors[0]] * 10 + list_colors[colors[1]]
        multiplier = list_colors[colors[2]]
        value *= 10 ** multiplier

    elif len(colors) == 5:
        value = (
            list_colors[colors[0]] * 100
            + list_colors[colors[1]] * 10
            + list_colors[colors[2]]
        )
        multiplier = list_colors[colors[3]]
        value *= 10 ** multiplier

    if value >= 1_000_000:
        value = value / 1_000_000
        unit = "megaohms"

    elif value >= 1_000:
        value = value / 1_000
        unit = "kiloohms"

    else:
        unit = "ohms"

    if value == int(value):
        value = int(value)

    return f"{value} {unit} ±{tolerance}"