label increase_janos_strikes:
    $ janos_strikes += 1
    if janos_strikes == janos_strikes_limit:
        call fight_janos_start # TODO: CODE add janos strike check everywher
    return