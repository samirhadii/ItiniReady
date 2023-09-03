from places.restaurants import get_restaurants
from places.bars import get_bars
from places.shopping_malls import get_shopping
from places.cafe import get_cafes
import random
from classifier import assign_scores
from priorize import prioritize
from places.get_places_noprice import get_places_noprice

def set_schedule(coordinates, desired_price, radius,preferences):
    schedule = [["8:00 AM", ""], ["9:00 AM", ""], ["10:00 AM", ""],
                ["11:00 AM", ""], ["12:00 PM", ""], ["1:00 PM", ""], ["2:00 PM", ""],
                ["3:00 PM", ""], ["4:00 PM", ""], ["5:00 PM", ""], ["6:00 PM", ""], ["7:00 PM", ""],["8:00 PM", ""]]

    #get all nearby places

    #get all the nearby cafes and choose one 
    cafes = get_cafes(coordinates, desired_price, radius)
    if cafes:
        cafes_score_dict = assign_scores(preferences,cafes)
        cafes_pq = prioritize(cafes_score_dict)
        cafe = cafes_pq.get()[1]
    else:
        cafe = "No bars in the specified radius"

    #get all nearby restaurants and choose one 
    restaurants = get_restaurants(coordinates, desired_price, radius)
    if restaurants:
        restaurants_score_dict = assign_scores(preferences,restaurants)
        restaurant_pq = prioritize(restaurants_score_dict)
        restaurant = restaurant_pq.get()[1]
    else:
        restaurant = "No restaurants in the specified radius"

    #get all nearby shops and choose one 
    shops = get_shopping(coordinates, radius)
    #get all nearby parks
    parks = get_places_noprice("park",coordinates,radius)
    #get all nearby museums
    museum = get_places_noprice("museum",coordinates,radius)
    #merge them all and choose one
    midday_dict = {**museum,**shops,**parks}
    midday_score_dict = assign_scores(preferences,midday_dict)
    midday_pq = prioritize(midday_score_dict)
    midday_place = midday_pq.get()[1]


    #get all nearby bars and choose one
    bars = get_bars(coordinates, desired_price, radius)

    #get all the nearby movie_theater and choose one
    movies = get_places_noprice("movie_theater",coordinates,radius)

    #merge bars dict and movies dict together for nighttime
    night_dict = {**bars,**movies}
    night_score_dict = assign_scores(preferences,night_dict)
    night_pq = prioritize(night_score_dict)
    night_place = night_pq.get()[1]

    
    # right now only support cafe for breakfast activity and restaurant for lunch activity
    schedule[1][1] = cafe

    schedule[4][1] = restaurant

    schedule[6][1] = midday_place

    schedule[12][1] = night_place

    return schedule



