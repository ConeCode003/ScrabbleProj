# available letters
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
# points for each letter
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# letters mapped to points
letters_to_points = {key: val for key, val in zip(letters, points)}
letters_to_points[' '] = 0
print(letters_to_points)


# getting the total points for a word
def score_word(word):
    point_total = 0
    for letter in word:
        point_total += letters_to_points.get(letter.upper(), 0)  # enabling lower case letters
    return point_total


# testing score word
brownie_points = "broWNIE"
print(score_word(brownie_points))

# player words produced during the game
player_to_words = {
    "player1": ["BLUE", "TENNIS", "EXIT"],
    "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
    "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

# mapping points to players according to the words they produced
player_to_points = {}


def update_point_totals():
  for player, words in player_to_words.items():
    player_to_points[player] = sum(score_word(word) for word in words)


# playing the new word
def play_word(player, word):
    if player in player_to_words:
        player_to_words[player].append(word)
    else:
        player_to_words[player] = [word]


# testing
play_word("player4", "Love")

print(player_to_words)





