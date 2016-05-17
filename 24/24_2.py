import datetime
from local_lib import *

start_time = datetime.datetime.now()

parcel_weights = get_input()
parcel_group_weight = sum(parcel_weights) / 4

# Setting lowest length and qe to length and qe of entire parcel list means less checking later on
lowest_group1_count = len(parcel_weights)
lowest_group1_qe = get_list_product(parcel_weights)

# Get first group of parcels with appropriate weight
for group1_parcels in get_candidate_combos(parcel_weights, parcel_group_weight):
    # Candidate combos are given in order shortest first and heaviest parcels first

    # If a previous combo was shorter, we're done
    if lowest_group1_count < len(group1_parcels):
        break

    # If a previous combo had a lower QE, we're done
    if lowest_group1_qe <= get_list_product(group1_parcels):
        break

    group2_candidate_parcels = get_remaining_parcels(parcel_weights, group1_parcels)

    # Get candidate second groups of parcels
    for group2_parcels in get_candidate_combos(group2_candidate_parcels, parcel_group_weight):

        group3_candidate_parcels = get_remaining_parcels(group2_candidate_parcels, group2_parcels)

        for group3_parcels in get_candidate_combos(group3_candidate_parcels, parcel_group_weight):
            # If group 1, 2 and 3 are valid, they will weigh three quarters of the total
            # Any remaining parcels will weigh one quarter of the total IE be a group of the correct weight
            # Other conditions were checked earlier, so this combo is better than the previous
            lowest_group1_count = len(group1_parcels)
            lowest_group1_qe = get_list_product(group1_parcels)

print 'Lowest group count:', lowest_group1_count
print 'Lowest quantum entanglement:', lowest_group1_qe
print 'Script took', datetime.datetime.now() - start_time
