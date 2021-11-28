label increase_janos_strikes:
    $ janos_strikes += 1
    if janos_strikes >= janos_strikes_limit:
        call janos_hits_1 # TODO: CODE add janos strike check everywher
    return

label check_janos_alive:
    if janos_sheet.health <= 0:
        show pc at center
        centered """In one infinitessimal moment, the heat of the battle dissapears,

        leaving a pile of insignificant dust in the shape of Janos before you on the floor.

        Great.

        You have killed the sheriff"""
        hide pc
        with Dissolve(1.0)
        
        call victory
    else:
        return
