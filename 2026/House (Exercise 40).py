PARTS = [
    ("house", "that Jack built."),
    ("malt", "that lay in the"),
    ("rat", "that ate the"),
    ("cat", "that killed the"),
    ("dog", "that worried the"),
    ("cow with the crumpled horn", "that tossed the"),
    ("maiden all forlorn", "that milked the"),
    ("man all tattered and torn", "that kissed the"),
    ("priest all shaven and shorn", "that married the"),
    ("rooster that crowed in the morn", "that woke the"),
    ("farmer sowing his corn", "that kept the"),
    ("horse and the hound and the horn", "that belonged to the"),
]

def recite(start_verse, end_verse):
    verses = []

    for verse in range(start_verse - 1, end_verse):
        sentence = "This is the "

        for i in range(verse, -1, -1):
            noun, action = PARTS[i]
            sentence += noun + " "

            if i == 0:
                sentence += action
            else:
                sentence += action + " "

        verses.append(sentence)

    return verses