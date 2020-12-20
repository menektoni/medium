'''
    Custom log that will print info and save it in a csv file.
     It extends the default python log.
     It also have a function to get a fancy string from time in seconds.
'''




def fancy_string_time_from_seconds(input_seconds):
    """
        It converts a time in seconds into a string that is beautiful to read

        Args:
            input_seconds:  time in seconds

        Returns:
            a fancy string like 1h 21m 42s
    """

    # Parse if needed
    try:
        input_seconds = float(input_seconds)

    except ValueError:
        return None

    #extract hours and minutes
    minutes, seconds = divmod(input_seconds, 60)
    hours, minutes = divmod(minutes, 60)

    #only print what it is not 0
    if hours > 0:
        return "%dh %dm %02ds" % (hours, minutes, seconds)

    if minutes > 0:
        return "%dm %02ds" % (minutes, seconds)

    return "%.2fs" % seconds
