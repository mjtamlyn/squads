def natural_time(time):
    hours = time / 60
    minutes = time % 60
    string = ''
    if hours:
        string += '%s hour' % hours
        if hours > 1:
            string += 's'
        string += ' '
    if minutes:
        string += '%s minute' % minutes
        if not minutes == 1:
            string += 's'
    if not string:
        return 'None'
    return string
