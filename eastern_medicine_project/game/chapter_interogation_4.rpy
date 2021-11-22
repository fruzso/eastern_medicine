label interogation_4:
    # The main scene of the game, where the player returns many times
    # PLOTPOINTS: bossfight

    scene black 
    with fade 
    
    play music background_music_interrogation volume 0.5 loop

    scene background_video_interogation
    with Dissolve(3.0)

    call show_dynamic_stats

    centered "The ultimate question has arrived."

    centered "He has been toying with you for long enough."

    if story_pc_guilty:
        centered "Deep down you know that you are guilty."
    else:
        centered "Deep down you know that you are innocent."

    centered "But does he belive you?"

    menu ask_for_judgemnet:
        "Ask him if he belives you."

        "Yes, It's time it ended, pop the question.":
            show pc idle at right
            pc "Well, I think maybe it is time."
            hide pc

            show janos idle at right
            janos "Time?"
            hide janos

            show pc idle at right
            pc """
            Yes, time. It's time you told me what you think.
            
            Am I found guilty? Do YOU find me guilty?
            """
            hide pc

        "He will tell me":
            centered "It's better to let things run their natural cousrse. He will tell me when he wants. Best remain silent"

            centered "You remain silent."

            show janos idle at right
            janos "Have you enumerated all the points, arguments and circumstance that might play in your favour?"
            hide janos

            if pc_sheet.CLAN == "Malkavian":
                show pc idle at right
                pc """
                Nothing else comes to mind.
                The only other sound's the break
                Of distant waves and birds awake.
                To see you had better be blind.
                """
            else:
                show pc idle at right
                pc "Yes."
                hide pc
    
    centered "Janos takes his sweat time considering you and all you have said."

    centered "His face is a puzzle."

    menu interpret_janos:
        "Figure out what Janos thinks?"

        "Yes, I want to know with every fiber of my being":
            # Contest Roll
            $ roll_janos = Roll(janos_sheet.PERFORMANCE + janos_sheet.COMPOSURE, janos_sheet.hunger, difficulty=0)
            $ roll_janos.roll()
            $ roll_pc = Roll(pc_sheet.WITS + pc_sheet.INSIGHT, pc_sheet.hunger, difficulty=roll_janos.margin_of_success)
            $ roll_pc.roll()

            if roll_pc.is_success:
                centered "He might be an ugly mother fucker, but emotions are a universal language."

                centered "And you are fluent in it."

                if story_janos_condemns:
                    centered """
                    Thre is an evil smile on those lips.
                    They might be hanging by a thread, but they are telling a story of their own.
                    """

                    centered "A story that can only end poorly for you."

                    if story_pc_guilty:
                        centered "Shit, he knows it was you."
                    else:
                        centered "Shit, he thinks it was you."

                else:
                    centered """
                    The nosferatu might be the ugliest thing you have ever seen,
                    yet his face now gives you hope.
                    """
            else:
                centered "No hope."

                centered "Who knows what a nosferatu's deformed features hide."

        "Patience is a virtue":
            centered "Who knows what a nosferatu's deformed features hide."
    
    centered "The nosferatu opens his abhorent lips to pass judgement."

    menu do_you_run_for_it:
        "Do you try to run for it?"

        "No, I'll take it":
            centered "You wait his judgement anxiously. Every moment feels like eternity."

        "Run, run, run!":
            jump run

    show janos idle at right
    janos """
    As it happens, the prince gave me full jurisdiction over this matter.
    So we can cut all the bullshit, etiquette and courtly diplomacy.
    The hour is nigh, and you are:
    """   
    
    if story_janos_condemns:
        janos "Guilty."
        hide janos

        centered "It's to late to run."
        call fight

    else:
        janos "Not guilty."
        hide janos

        call victory # The End.

    label fight:
        centered "Janos grabs your arm."

        centered "You try to escape his grasp."

        $ roll_janos = Roll(janos_sheet.DEXTERITY + janos_sheet.BRAWL, janos_sheet.hunger, difficulty=0)
        $ roll_janos.roll()
        $ roll_pc = Roll(pc_sheet.DEXTERITY + pc_sheet.BRAWL, pc_sheet.hunger, difficulty=roll_janos.margin_of_success)
        $ roll_pc.roll()

        if roll_pc.is_success:
            show pc idle at right
            pc "Hah!"
            hide pc

            centered "Your muscles cleverly obey your commands and you escape his grasp."

        else:
            show pc idle at right
            pc "Shit!"
            hide pc

            centered "His grasp hold firm."
    
    label fight_2:
        centered "PLACEHOLDER" # TODO:WRITE
            

    hide screen dynamic_stats
    scene black
    with fade
    return

label run:
    centered """
            It's decided, you have to flee for your life.
            There will be no time to appeal to the prince.
            It is now or never.
            """

            menu where_to_run:
                "Choose a direciton!"
                "Vanish into thin air (OBFUSCATE)" if pc_sheet.OBFUSCATE >= 4:
                    centered "Thank the Dark Father, you have to power to vanish from the eye."
                    
                    # Rousecheck
                    if not pc_sheet.rouse_check():
                        call change_dynamic_stats("worse")                   

                    $ roll_janos = Roll(janos_sheet.WITS + janos_sheet.AWARENESS, janos_sheet.hunger, difficulty=0)
                    $ roll_janos.roll()
                    $ roll_pc = Roll(pc_sheet.WITS + pc_sheet.OBFUSCATE, pc_sheet.hunger, difficulty=roll_janos.margin_of_success)
                    $ roll_pc.roll()

                    if roll_pc.is_success:
                        centered "You vanish in front of Janos' eyes."

                        if janos_sheet.AUSPEX > 1:
                            $ roll_janos = Roll(janos_sheet.WITS + janos_sheet.AUSPEX, janos_sheet.hunger, difficulty=0)
                            $ roll_janos.roll()
                            $ roll_pc = Roll(pc_sheet.WITS + pc_sheet.OBFUSCATE, pc_sheet.hunger, difficulty=roll_janos.margin_of_success)
                            $ roll_pc.roll()

                            centered "You sense that is looking for you with dark power of sight"

                            if roll_pc.is_success:
                                centered "But it is to no point. He cannot find you."
                                call victory
                            else:
                                centered "Shit. He's got you"
                                call fight_2                              

                        else:
                            call victory

                    else:
                        centered "You begin to fade in front of Janos' eyes, but the nosferatu cannot be fouled."
                        call defeat_violent


                "I've got speed (CELERITY)" if pc_sheet.CELERITY > 0:
                    centered "PLACEHOLDER" # TODO:WRITE

                "The door might be too obvious, but that's the surprise":
                    centered "PLACEHOLDER" # TODO:WRITE

                "The window will do just fine":
                    centered "PLACEHOLDER" # TODO:WRITE
    