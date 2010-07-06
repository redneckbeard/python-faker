import random
import datetime as py_datetime

def _truncated_gauss(a, b, mu, sigma):
    while 1:
        x = random.gauss(mu, sigma)
        if a <= x <= b:
            return x

def datetime(start, end=None, distribution = lambda max: random.randrange(max)):
    """ Returns random datetime between `start` and `end` """
    end = end or py_datetime.datetime.now()
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = distribution(int_delta)
    return (start + py_datetime.timedelta(seconds=random_second))

def datetime_gauss(start, end, average_k=0.5, scope=3):
    """ Returns random datetime between `start` and end with gauss distribution """
    gauss = lambda max: _truncated_gauss(0, max, max*average_k, max/scope)
    return datetime(start, end, gauss)

def birthday(average=25, min=16, max=70, scope=6):
    """ Returns random birthday.
    Parameters are average age, min age, max age and scope.
    Bigger scope -> dates are closer to average. """
    today = py_datetime.datetime.now()
    start = today - py_datetime.timedelta(days=365*max)
    end = today - py_datetime.timedelta(days=365*min)
    k = 1 - float(average-min)/(max-min)
    return datetime_gauss(start, end, k, scope)
