from time import time
import math
def genesis_f(x):
    genesis = int(time())
    return genesis
def last_feed_f(x):
    last_feed = int(time())
    return last_feed
def last_play_f(x):
    last_play = int(time())
    return last_play
def current_time_f():
    current_time = int(time())
    return current_time
def time_second_f(x):
    genesis = genesis_f(x)
    current_time = current_time_f()
    time_second = current_time-genesis
    return time_second
def time_min_f(x):
    time_second = time_second_f(x)
    time_min = time_second/60
    return time_min
def time_hour_f(x):
    time_min = time_min_f(x)
    time_hour = time_min/60
    return time_hour
def time_day_f(x):
    time_hour = time_hour_f(x)
    time_day = time_hour/24
    return time_day
def age_f(x):
    time_day = time_day_f(x)
    age = math.floor(time_day)
    return age