label increase_janos_strikes:
    $ janos_strikes += 1
    if janos_strikes == janos_strikes_limit:
        call fight_janos_start # TODO: CODE add janos strike check everywher
    return

label check_janos_alive:
    if janos_sheet.health <= 0:
        cenetred """
        In one infinitessimal moment, the heat of the battle dissapears,

        leaving a pile of insignificant dust in the shape of Janos before you on the floor.

        Great.

        You have killed the sheriff
        """
        call victory
