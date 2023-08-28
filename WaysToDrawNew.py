import math, argparse
from rackFunctions import ways_to_draw, sum_from_spot, print_stats
number_of_lines = 22000
draws = []
parser = argparse.ArgumentParser()
parser.add_argument("quant", type=int, help="Enter the number of alphagrams you want analyzed")
parser.add_argument("start", type=int, help="Enter the probability of the alphagram you wish to start with")
args = vars(parser.parse_args())
number_of_alphagrams = args['quant']
starting_alphagram = args['start']

with open("/Users/etbrosowsky/Zyzzyva/words/saved/SevenAlphagrams.txt") as SevenAlphagrams:
    counter = 0
    for line in SevenAlphagrams:
        draws.append(round(ways_to_draw(line.rstrip())))
        counter += 1
        if counter == number_of_lines:
            break

draws.sort(reverse=True)
total_draws = sum(draws)
alphagram_sum = sum_from_spot(draws, number_of_alphagrams, starting_alphagram)
print_stats(draws, total_draws, number_of_alphagrams, alphagram_sum, starting_alphagram)