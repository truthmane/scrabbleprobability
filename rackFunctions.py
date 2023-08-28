import math
frequencies=[9,2,2,4,12,2,3,4,9,1,1,4,2,6,8,2,1,6,4,6,4,2,2,1,2,1]

def ways_to_draw(rack):
    ways_quantity=1
    for letter in rack:
        ways_quantity*=int(math.comb(frequencies[ord(letter) - 65],rack.count(letter))**(1/rack.count(letter)))
    return(ways_quantity)

def sum_from_spot(list, length, start):
  sum = 0
  for i in range(start, start+length):
    sum += list[i]
  return sum

def print_stats(list_of_draws, total_draws, number_of_alphagrams, alphagram_sum, alphagram_start):
    print("For alphagrams "+str(alphagram_start)+"-"+str(alphagram_start+number_of_alphagrams)+":")
    print("Percent of total alphagrams: "+str(round((number_of_alphagrams/len(list_of_draws))*100,2))+"%")
    print("Total draws for top "+ str(number_of_alphagrams)+" alphagrams: "+str(alphagram_sum))
    print("Percent of total draws: " + str(round((alphagram_sum/total_draws)*100,2))+"%")

if __name__== "__main__":
    rack = input("Rack: ")
    print(ways_to_draw(rack))