# name_overview is a dict in the format name:overview
# score_dict is a dict in the format overview:score
def get_scores(name_overview,score_dict):
    name_score = {}
    for key in score_dict:
        namescore_key = name_overview[key]
        namescore_value = score_dict[key] 
        name_score[namescore_key] = namescore_value
    return name_score
#returns the dictionary in the format needed for the priority queue 
