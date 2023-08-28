import math
from rackFunctions import ways_to_draw, sum_from_spot, print_stats
number_of_lines = 22000
draws = []
number_of_alphagrams=int(input("Number of alphagrams: "))
starting_alphagram=int(input("Starting alphagram: "))-1

with open("/Users/etbrosowsky/Zyzzyva/words/saved/SevenAlphagrams.txt") as SevenAlphagrams:
    alphagrams_list = []
    counter = 0
    for line in SevenAlphagrams:
        alphagrams_list.append(line.rstrip())
        counter += 1
        if counter == number_of_lines:
            break

for rack in alphagrams_list:
    draws.append(round(ways_to_draw(rack)))

draws.sort(reverse=True)
total_draws = sum(draws)
alphagram_sum = sum_from_spot(draws, number_of_alphagrams, starting_alphagram)
print_stats(draws, total_draws, number_of_alphagrams, alphagram_sum)