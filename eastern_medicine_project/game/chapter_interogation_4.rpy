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

        "Yes, I want to know with every fiber of my being {image=dice}":
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
            call run

        "I am no coward, fight!":
            call fight_pc_start

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
        centered "His filthy hand is already clutching your wrist."
        call fight_janos_start

    else:
        janos "Not guilty."
        hide janos

        call victory # The End.

    hide screen dynamic_stats
    scene black
    with fade
    return