import itertools

# 4x4 preference matrices for men and women
men_prefs = [[2, 3, 1, 4], [3, 1, 4, 2], [1, 4, 3, 2], [4, 2, 3, 1]]
women_prefs = [[2, 3, 1, 4], [1, 2, 4, 3], [3, 1, 4, 2], [4, 3, 2, 1]]

def get_popular_matchings():
    matchings = []
    for perm in itertools.permutations(range(4)):
        is_popular = True
        for i in range(4):
            for j in range(i+1, 4):
                if (men_prefs[i][perm[j]] < men_prefs[i][perm[i]]) and \
                   (women_prefs[perm[j]][i] < women_prefs[perm[j]][perm[i]]):
                    is_popular = False
                    break
            if not is_popular:
                break
        if is_popular:
            matchings.append(list(perm))
    return matchings

# Example usage:
matchings = get_popular_matchings()
print(f"Number of popular matchings: {len(matchings)}")
print("Popular matchings:")
for matching in matchings:
    print(matching)
