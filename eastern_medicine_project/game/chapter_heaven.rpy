label heaven:
    # A memory of the PC's heaven
    # PLOTPOINTS: Fight with the S.I. Agents

    scene black
    with fade

    show janos idle at right
    janos """
    So, the big one.
    
    What do you remember of August?

    And please don't give me any of that patriotic bullshit,

    nothing like - I foundled the memories of a great celebration and national glory- 
    """
    hide janos

    pause(1.0)

    "You remember yesturday."

    "Yes, the day."

    "Around midday, when all slef respecting kindred should be in the deathlike slumber of torpor."

    "You were in your lightproof heaven."

    scene background_video_heaven
    with Dissolve(2.0)

    show pc idle at right
    pc "I was doing what all godfearing kindred would be doing. Laying in torpor."
    hide pc

    show janos at right
    janos """
    Let us not bring God in the picture, just yet.

    How did you know that your heaven has been breached?
    """
    hide janos

    menu heave_defance:
        "It was a piece of the door, landing in my...":
            show pc idle at right
            pc """
            It was a piece of the door, landing in my abdomen.

            Pain can be a pretty handy wake-up call, you see.
            """
            hide pc

            $ pc_sheet.lost_health(1)
            "/You lose 1 point of health./"
            if pc_sheet.health = 0:
                call lost_health

            show janos idle at right
            janos "Carry on, no need to spare the details."
            hide janos

        "I am friends with the Tremere...":
            show pc idle at right
            pc "I am friends with the Tremere, so I had an associate install wards and rituals just in case of something like this."
            hide pc

            show janos at right
            janos "Name, please."
            hide janos

            show pc idle at right
            pc "Ede Kovacs"
            hide pc

            show janos idle at right
            janos "Carry on, no need to spare the details."
            hide janos

            show pc idle at right
            pc """
            First I sensed an incredible power pulling something out of me.

            But the stange thing was, that it was not pulling aroudn my heart.

            I grabbed me with a thousand tiny muscles everywhere, where blood was circulating within.

            Even with the pain, it took considerable effort to wake up.            
            """

            "/You lose 1 point of willpower./"
            if pc_sheet.WILLPOWER = 0:
                call lost_willpower
            
            hide pc

        "I had a vision" if pc_sheet.AUSPEX >= 2:
            show pc idle at right
            if pc_sheet.CLAN == "Malkavian":
                pc """
                It was not the first time that my dreams brought me
                
                How should I say, that even you would understand.
                
                You have heard of visions, soothsaying, portents and the like, right?"""
                hide pc

                show janos idle at right
                janos "Yes, naturally."
                hide janos

                "/you notice the Janos would like to say something else, chooses to remain silent/"

                show pc idle at right
                pc """
                Let's just say that I had a feeelign that it woudl be a terribly good idea to kick in the door.
                
                That is just not my style.

                So, naturally I had a pretty good idea what was going on.
                """

                show janos idle at right
                janos "You still had to wake up."
                hide janos

                show pc idle at right
                pc """
                quite so.
                
                It was no picnic I have to admit.

                But when you know, you know, you know.
                """
                hide pc

                show janos idle at right
                janos "To be honest, I don't."
                hide

                show pc idle at right
                pc "well, I did."
                hide pc


                "/You lose 1 point of willpower./"
                if pc_sheet.WILLPOWER = 0:
                    call lost_willpower


    show janos idle at right
    janos "So, you were awake. What happened next?"
    hide janos    





    scene black
    with fade
    return