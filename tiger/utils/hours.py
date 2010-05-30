from datetime import datetime
from django.conf import settings
from pytz import timezone


DOW_MONDAY = 0
DOW_TUESDAY = 1
DOW_WEDNESDAY = 2
DOW_THURSDAY = 3
DOW_FRIDAY = 4
DOW_SATURDAY = 5
DOW_SUNDAY = 6
DOW_CHOICES = (
    (DOW_MONDAY, 'Monday'),
    (DOW_TUESDAY, 'Tuesday'),
    (DOW_WEDNESDAY, 'Wednesday'),
    (DOW_THURSDAY, 'Thursday'),
    (DOW_FRIDAY, 'Friday'),
    (DOW_SATURDAY, 'Saturday'),
    (DOW_SUNDAY, 'Sunday'),
)

def is_available(timeslots, tz):
    server_tz = timezone(settings.TIME_ZONE)
    site_tz = timezone(tz)
    now = server_tz.localize(datetime.now())
    timeslots = timeslots.filter(dow=now.weekday())
    if not timeslots.count():
        return False
    for timeslot in timeslots:
        start_dt = site_tz.localize(datetime.combine(datetime.now(), timeslot.start))
        stop_dt = site_tz.localize(datetime.combine(datetime.now(), timeslot.stop))
        if start_dt < now < stop_dt:
            return True
    return False

def calculate_hour_string(timeslots):
    # this implementation is a little naive, but let's just assume our customers
    # don't keep ridiculous hours
    timeslots = timeslots.order_by('dow')
    times = {}
    for timeslot in timeslots:
        time_range = '%s-%s' % (timeslot.pretty_start, timeslot.pretty_stop)
        if times.has_key(time_range):
            times[time_range].append(timeslot.dow)
        else:
            times[time_range] = [timeslot.dow]
    time_dict = dict(DOW_CHOICES)
    time_strings = []
    abbr_length = 3
    time_list = times.items()
    time_list.sort(key=lambda obj: obj[1][0])
    for k, v in time_list:
        # test if the dow ints are consecutive
        if v == range(v[0], v[-1] + 1) and len(v) > 1:
            s = '%s-%s %s' % (time_dict[v[0]][:abbr_length], time_dict[v[-1]][:abbr_length], k)
        else:
            s = '%s %s' % ('/'.join(time_dict[n][:abbr_length] for n in v), k)
        time_strings.append(s)
    hours_string = ', '.join(time_strings)
    return hours_string