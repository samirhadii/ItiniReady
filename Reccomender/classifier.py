from transformers import pipeline
from get_scores import get_scores

def assign_scores(preference,name_overview):
    overviews_array = []
    for overview,name in name_overview.items():
        overviews_array.append(overview)

    #classifier = pipeline(model="facebook/bart-large-mnli")
    classifier = pipeline("zero-shot-classification", model='cross-encoder/nli-deberta-v3-small')

    res = classifier(
        preference,
        overviews_array
        )

    score_dict = dict(zip(res["labels"],res["scores"]))

    name_score = get_scores(name_overview,score_dict)

    return name_score
