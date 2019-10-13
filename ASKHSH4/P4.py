def permutations(list):

    if len(list) == 1:      # Περιπτωση που δινεται μονο ψηφιος αριθμος
        return [list]

    if list[1:] == list[:-1]:   # Περιπτωση που δινεται αριθμος με ολα τα ψηφια ιδια
        return [list]

    permut_list = []
    for i in range(len(list)):
        first_No = list[i]

        rest_of_list = list[:i] + list[i + 1:]      # list[:i] --> starting point list[0], ending point list[i]
                                                    # list[i + 1:] --> starting point list[i+1], ending point --> the end of the list

        for nr in permutations(rest_of_list):       # nr --> next round
            permut_list.append([first_No] + nr)

    return permut_list

user_input = list(input("Enter a number"))


for a, b in enumerate(permutations(user_input), 1):
    print('{} {}'.format(a, b))