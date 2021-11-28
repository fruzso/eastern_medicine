label interogation_4:
    # The main scene of the game, where the player returns many times
    # PLOTPOINTS: bossfight

    scene black 
    with fade 
    
    play music background_music_interrogation volume 0.5 loop

    scene background_video_interogation
    with Dissolve(2.0)

    call show_dynamic_stats

    call bossfight_intro

    menu: # Ultimately every option leads to fight / run / victory
        "Ask him if he belives you."
        "Yes, It's time it ended, pop the question.":
            call bossfight_ask_for_judgement #
            call bossfight_intermission_1 #
            menu:
                "Figure out what Janos thinks?"
                "Yes, I want to know with every fiber of my being {image=dice}":
                    call bossfight_read_janos #
                    call bossfight_intermission_2 #
                    call bossfight_judgement #
                "Patience is a virtue":
                    centered "Who knows what a nosferatu's deformed features hide."
                    call bossfight_intermission_2 #
                    menu:
                        "Do you try to run for it?"
                        "No, I'll take it":
                            centered "You wait his judgement anxiously. Every moment feels like eternity."
                            call bossfight_judgement #
                        "Run, run, run!":
                            call run #
                        "I am no coward, fight!":
                            call fight_pc_start #

        "He will tell me":
            call bossfight_wait #
            call bossfight_intermission_1 #
            menu:
                "Figure out what Janos thinks?"
                "Yes, I want to know with every fiber of my being {image=dice}":
                    call bossfight_read_janos #
                    call bossfight_intermission_2 #
                    call bossfight_judgement #
                "Patience is a virtue":
                    centered "Who knows what a nosferatu's deformed features hide."
                    call bossfight_intermission_2 #
                    menu:
                        "Do you try to run for it?"
                        "No, I'll take it":
                            centered "You wait his judgement anxiously. Every moment feels like eternity."
                            call bossfight_judgement #
                        "Run, run, run!":
                            call run # Goes to run -> bossfight
                        "I am no coward, fight!":
                            call fight_pc_start # Goes to bossfight

label bossfight_intro:
    centered "The ultimate question has arrived."

    centered "He has been toying with you for long enough."

    if story_pc_guilty:
        centered "Deep down you know that you are guilty."
    else:
        centered "Deep down you know that you are innocent."

    centered "But does he belive you?"
    return

label bossfight_ask_for_judgement:
    show pc idle at right
    with Dissolve(1.0)
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
    return

label bossfight_wait:
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
    
    return
        
label bossfight_intermission_1:
    centered "Janos takes his sweat time considering you and all you have said."

    centered "His face is a puzzle."

    return

label bossfight_read_janos:
    # Contest Roll
    $ roll_janos = Roll(janos_sheet.PERFORMANCE + janos_sheet.COMPOSURE, janos_sheet.hunger, difficulty=0)
    $ roll_janos.roll()
    $ roll_pc = Roll(pc_sheet.WITS + pc_sheet.INSIGHT, pc_sheet.hunger, difficulty=roll_janos.margin_of_success)
    $ roll_pc.roll()

    if roll_pc.is_success:
        centered "He might be an ugly mother fucker, but emotions are a universal language."

        centered "And you are fluent in it."

        if story_janos_condemns:
            centered """Thre is an evil smile on those lips.
            They might be hanging by a thread, but they are telling a story of their own.
            
            A story that can only end poorly for you."""

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
        centered """No hope.
        
        Who knows what a nosferatu's deformed features hide."""
    return

label bossfight_intermission_2:
    centered "The nosferatu opens his abhorent lips to pass judgement."
    return

label bossfight_judgement:
    show janos idle at right
    janos """
    As it happens, the prince gave me full jurisdiction over this matter.
    So we can cut all the bullshit, etiquette and courtly diplomacy.
    The hour is nigh, and you are:
    """

    #TODO: CODE Evalute janos' judgement   
    
    if story_janos_condemns:
        janos "Guilty."
        hide janos

        centered "It's to late to run."
        call janos_hits_1 # Goes to bossfight

    else:
        janos "Not guilty."
        hide janos

        call victory # The End.