def is_popular_matching(men_match, women_match):
    men_prefs = [[2, 0, 1], [0, 1, 2], [1, 2, 0]]
    women_prefs = [[1, 0, 2], [0, 2, 1], [2, 1, 0]]

    marked_edges = set()
    for i in range(len(men_match)):
        if men_match[i] is not None and women_match[i] is not None:
            if men_prefs[i][women_match[i]] == 1 and women_prefs[women_match[i]][i] == 1:
                marked_edges.add((i, women_match[i]))

    for m in marked_edges:
        w = m[1]
        level = 0
        while w is not None:
            if w in marked_edges:
                return "unpopular"
            if women_match[w] is None:
                return "unpopular"
            level += 1
            m = (women_match[w], w)
            w = men_match[m[0]]
        if level % 2 == 0:
            return "unpopular"

    marked_edges = set()
    for i in range(len(women_match)):
        if women_match[i] is not None and men_match[i] is not None:
            if women_prefs[i][men_match[i]] == 1 and men_prefs[men_match[i]][i] == 1:
                marked_edges.add((i, men_match[i]))

    for m in marked_edges:
        m = (m[1], m[0])
        level = 0
        while m[0] is not None:
            if m in marked_edges:
                return "unpopular"
            if men_match[m[0]] is None:
                return "unpopular"
            level += 1
            w = (m[0], men_match[m[0]])
            m = (w[1], w[0])
        if level % 2 == 0:
            return "unpopular"

    return "popular"

men_match = [None, None, None]
women_match = [None, None, None]
print(is_popular_matching(men_match, women_match))  # prints "popular"
men_match = [1, 0, None]
women_match = [1, None, 0]
print(is_popular_matching(men_match, women_match))  # prints "unpopular"
