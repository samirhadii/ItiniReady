from places.restaurants import get_restaurants
from places.bars import get_bars
from places.shopping_malls import get_shopping
from places.cafe import get_cafes
from classifier import assign_scores
from priorize import prioritize
from places.get_places_noprice import get_places_noprice
def get_night_pq(coordinates, desired_price, radius,preferences):

    #get all nearby bars and choose one
    bars = get_bars(coordinates, desired_price, radius)

    #get all the nearby movie_theater and choose one
    movies = get_places_noprice("movie_theater",coordinates,radius)

    #merge bars dict and movies dict together for nighttime
    night_dict = {**bars,**movies}
    night_score_dict = assign_scores(preferences,night_dict)
    night_pq = prioritize(night_score_dict)
    night_place = night_pq.get()[1]
    return night_pq

def get_midday_pq(coordinates, desired_price, radius,preferences):
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
    return midday_pq

def get_lunch_pq(coordinates, desired_price, radius,preferences):
    #get all nearby restaurants and choose one 
    restaurants = get_restaurants(coordinates, desired_price, radius)
    if restaurants:
        restaurants_score_dict = assign_scores(preferences,restaurants)
        restaurant_pq = prioritize(restaurants_score_dict)
        restaurant = restaurant_pq.get()[1]
    else:
        restaurant = "No restaurants in the specified radius"
    return restaurant_pq

def get_morning_pq(coordinates, desired_price, radius,preferences):
    #get all the nearby cafes and choose one 
    cafes = get_cafes(coordinates, desired_price, radius)
    if cafes:
        cafes_score_dict = assign_scores(preferences,cafes)
        morning_pq = prioritize(cafes_score_dict)
        morning_place = morning_pq.get()[1]
    else:
        morning_place = "No bars in the specified radius"
    return morning_pq

obj = get_morning_pq("33.879892,-84.034418",1,10000,"local coffee shop")
print(obj.get())