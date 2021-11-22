label carpark:
    # A memory of the Carpark
    # PLOTPOINTS: the mentors letter

    scene black
    with fade

    centered """
    Where did you go next?

    You hid in another appartment in your building.

    But that is not what he wants to know.

    You remember the carpark distinctly.
    """

    scene background_video_carpark
    with Dissolve(1.5)

    call show_dynamic_stats

    show pc idle at right
    pc "I waited out the daylight. At the break of night darted for the only place with answers."
    hide pc

    menu:
        "Do you tell him the truth?"

        "Tell the truth":
            show pc idle at right
            pc """
            I wanted to talk to Emilio.
            
            I was hungry for all the answers, and he was the only I could trust.

            I was sure of it.
            """
            hide pc

        "Tell a lie":
            $ roll_janos = Roll(janos_sheet.INTELLIGENCE + janos_sheet.MANIPULATION, janos_sheet.hunger, difficulty=0)
            $ roll_janos.roll()
            $ roll_pc = Roll(pc_sheet.WITS + pc_sheet.PERSUASION, pc_sheet.hunger, difficulty=roll_janos.margin_of_success)
            $ roll_pc.roll()

            if roll_pc.margin_of_success > 0:
                # Succesful lie

                show pc idle at right
                pc """
                I walked around for a few hours to clear my head.

                Then headed to Elysium, where I got word that you are looking for me.
                """            
                hide pc

            else:
                # Unsuccesful lie
                
                show pc idle at right
                pc "I walked around for a few hours to clear my head."            
                hide pc

                centered """
                He needs more.

                Come on, think!

                I need to give him details.                
                """

                show pc idle at right
                pc "I went to fireman's club. It was quite."
                hide pc

                $ janos_strikes += 1

                show janos idle at right
                janos """
                That is quite a turn of evetns.
                
                Considering that if my ghouls are to be believed,
                
                it closed down 3 years ago.

                That is strike number [janos_strikes].
                """
                hide janos

    show jnaos idle at right
    janos "So what happend in the carpark?"
    hide janos

    #TODO: CODE + STORY Insert minigame here
    

    hide screen dynamic_stats
    scene black
    with fade
    return