import itertools
import operator

def get_list_product(list_of_ints):
    return reduce(operator.mul, list_of_ints, 1)


def get_input():
    output = []
    for line in open('input.txt'):
        parcel_weight = line.strip()

        output.append(int(parcel_weight))

    output.sort(reverse=True)
    return output


def get_candidate_combos(weight_list, target_weight):
    for combo_count in range(1, len(weight_list)):
        for combo in itertools.combinations(weight_list, combo_count):
            if sum(combo) == target_weight:
                yield combo


def get_remaining_parcels(weight_list, remove_list):
    output = weight_list[:]
    for weight in remove_list:
        if weight in output:
            output.remove(weight)

    return output
