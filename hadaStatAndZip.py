from typing import Tuple


def stats() -> Tuple[int, int]:
    """
    Returns a tuple with format (longest game, total number of games)"""
    fr = open("data/hada.txt", "r")
    fr2 = open("data/hada.txt", "r")
    return len(max(fr.readlines(), key=len)) - 1, len(fr2.readlines())
    # the len(max(...)) part counts newline as a symbol, but it doesn't extend the length of game


def zipped_stats():
    txt = ""
    with open("data/hada.txt", "r") as file:
        last_direction = ""
        direction_count = 0
        original = file.readlines()
        for line in range(len(original)):  # Iterating through individual games
            game = " " * (line == 0)
            for move in original[line]:  # Iterating through moves in individual games
                if move == last_direction:
                    direction_count += 1
                else:
                    game += f"{last_direction} {direction_count} "
                    last_direction = move
                    direction_count = 1

            txt += game[4:] + "\n"

    with open("data/hada_copy.txt", "w") as n_file:
        n_file.write(txt)


print(*stats())
zipped_stats()
