from flask import Flask, jsonify, request

from schedule import set_schedule
from coordinates import get_coords

from get_pqs import get_morning_pq, get_lunch_pq, get_midday_pq, get_night_pq

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/get_schedule')
def test_schedule():
    street = request.args.get('street')
    city = request.args.get('city')
    state = request.args.get('state')
    zipcode = request.args.get('zipcode')
    radius = request.args.get('radius')
    desired_price = request.args.get('desired_price')
    desired_price = int(desired_price)
    preferences = request.args.get('preferences')

    coordinates = get_coords(street, city, state, zipcode)

    morning = get_morning_pq(coordinates, desired_price,radius,preferences)
    app.config['MORNING_PQ'] = morning

    lunch = get_lunch_pq(coordinates, desired_price,radius,preferences)
    app.config['LUNCH_PQ'] = lunch

    midday = get_midday_pq(coordinates, desired_price,radius,preferences)
    app.config['MIDDAY_PQ'] = midday

    night = get_night_pq(coordinates, desired_price,radius,preferences)
    app.config['NIGHT_PQ'] = night

    return get_schedule(morning,lunch,midday,night)

def get_schedule(morning, lunch, midday, night):

    schedule = [["8:00 AM", ""], ["9:00 AM", ""], ["10:00 AM", ""],
            ["11:00 AM", ""], ["12:00 PM", ""], ["1:00 PM", ""], ["2:00 PM", ""],
            ["3:00 PM", ""], ["4:00 PM", ""], ["5:00 PM", ""], ["6:00 PM", ""], ["7:00 PM", ""],["8:00 PM", ""]]
    

    schedule[0][1] = morning.get()[1]
    schedule[4][1] = lunch.get()[1]
    schedule[6][1] = midday.get()[1]
    schedule[12][1] = night.get()[1]

    json_schedule = jsonify(schedule)

    return json_schedule


@app.route('/get_next')
def get_next():
    pq_type = request.args.get('pq_type')
    pq = app.config[pq_type]
    get_next = pq.get()[1]
    return get_next


#runs flask server
if __name__ == '__main__':
    app.run(debug=True)

