import math, argparse
from rackFunctions import ways_to_draw, sum_from_spot, print_stats
number_of_lines = 28000
draws = []
alphagrams_by_probability = [] 
parser = argparse.ArgumentParser()
parser.add_argument("quant", type=int, help="Enter the number of alphagrams you want analyzed")
parser.add_argument("start", type=int, help="Enter the probability of the alphagram you wish to start with")
parser.add_argument("length", type=int, help="Enter the word length you wish to query (7 or 8)")
args = vars(parser.parse_args())
number_of_alphagrams = args['quant']
starting_alphagram = args['start']
alphagram_length = args['length']

if alphagram_length == 7:

    with open("/Users/etbrosowsky/Zyzzyva/words/saved/SevenAlphagrams.txt") as SevenAlphagrams:
        counter = 0
        for line in SevenAlphagrams:
            draws.append(round(ways_to_draw(line.rstrip())))
            counter += 1
            if counter == number_of_lines:
                break
    with open("/Users/etbrosowsky/Zyzzyva/words/saved/realsorted7s.txt") as SortedAlphagrams:
        counter = 0
        for line in SortedAlphagrams:
            alphagrams_by_probability.append(line.rstrip())
            counter +=1
            if counter == number_of_lines:
                break

if alphagram_length == 8:
    with open("/Users/etbrosowsky/Zyzzyva/words/saved/EightAlphagrams.txt") as EightAlphagrams:
        counter = 0
        for line in EightAlphagrams:
            draws.append(round(ways_to_draw(line.rstrip())))
            counter += 1
            if counter == number_of_lines:
                break
    with open("/Users/etbrosowsky/Zyzzyva/words/saved/Sorted8s.txt") as SortedAlphagrams:
        counter = 0
        for line in SortedAlphagrams:
            alphagrams_by_probability.append(line.rstrip())
            counter +=1
            if counter == number_of_lines:
                break
     
draws.sort(reverse=True)
total_draws = sum(draws)
alphagram_sum = sum_from_spot(draws, number_of_alphagrams, starting_alphagram)
print_stats(draws, total_draws, number_of_alphagrams, alphagram_sum, starting_alphagram, alphagrams_by_probability)