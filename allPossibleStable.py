import itertools

# 4x4 preference matrices for men and women
men_prefs = [[2, 3, 1, 4], [3, 1, 4, 2], [1, 4, 3, 2], [4, 2, 3, 1]]
women_prefs = [[2, 3, 1, 4], [1, 2, 4, 3], [3, 1, 4, 2], [4, 3, 2, 1]]

def is_stable_matching(men_match, women_match):
    # Check if any man or woman prefers someone else to their current partner
    for i in range(4):
        for j in range(i+1, 4):
            if men_prefs[i][women_match[i]] < men_prefs[i][women_match[j]] and \
               women_prefs[women_match[i]][i] < women_prefs[women_match[i]][men_match.index(j)]:
                return False
            if women_prefs[j][men_match[j]] < women_prefs[j][men_match[i]] and \
               men_prefs[men_match[j]][j] < men_prefs[men_match[j]][women_match.index(i)]:
                return False
    return True

def get_stable_matchings():
    matchings = []
    for men_match in itertools.permutations(range(4)):
        for women_match in itertools.permutations(range(4)):
            if is_stable_matching(men_match, women_match):
                matchings.append((list(men_match), list(women_match)))
    return matchings

# Example usage:
matchings = get_stable_matchings()
print(f"Number of stable matchings: {len(matchings)}")
print("Stable matchings:")
for matching in matchings:
    print(f"Men's match: {matching[0]}, Women's match: {matching[1]}")
