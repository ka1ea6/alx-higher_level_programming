#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    return sorted(a_dictionary.items(), key=lambda x: x[1], reverse=True)[0][1]
