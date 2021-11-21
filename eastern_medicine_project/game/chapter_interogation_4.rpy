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
        "Ask him if he belives in you."
        "Yes, It's time it has ended.":
            show pc idle at right
            pc "Well, I think maybe it is time."
            hide pc

            show janos idle at right
            janos "Time?"
            hide janos

            show pc idle at right
            pc """
            Yes, time. It's time you told me what you think.
            
            Am I found guilty? Do you found me guilty?
            """
            hide pc

            jump judegement        
        "He will tell me":
            centered "It's better to let things run their natural cousrse. He will tell me when he wants. Best remain silent"

            centered "You remain silent."

    label judegement:
        centered "Janos takes his sweat time considering you and ll you have said"

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

                    if story_janos_guilty:
                        centered """
                        Thre is an evil smile on those lips.
                        They might be hanging by a thread, but they are telling a story of their own.
                        """

                        centered "A story that can only end poorly for you."

                        if story_pc_guilty:
                            centered "Shit, He knows it was you."
                        else:
                            centered "Shit, he thinks it was you."

                    else:
                        centered """
                        The nosferatu might be the ugliest thing you have ever seen, his face now, somehow gives oyu hope
                        """

                    $ pc_sheet.gain_willpower(1)
                    call change_dynamic_stats

                else:
                    centered "No hope."

                    centered "Who knows what a nosferatue's deformed features hide."

            "Patience is a virtue":
                centered "Who knows what a nosferatue's deformed features hide."
        
        centered "The nosferatu opens his abhorent lips to pass judgement."

        menu do_you_run_for_it:
            "Try to run for it"
            "Run, run, run!":
                call run_for_it

            "Take it":
                centered "PLACEHOLDER" # TODO:WRITE

        label run_for_your_life:
            centered """
            It's decided, you have to flee for oyur life.
            There will be no time to appeal to the prince.
            It is now or never
            """

            menu where_to_run:
                "Choose a direciton!"
                "Vanish into thin air (OBFUSCATE)" if pc_sheet.OBFUSCATE >= 3:
                    centered "PLACEHOLDER" # TODO:WRITE

                "I've got speed (CELERITY)" if pc_sheet.CELERITY > 0:
                    centered "PLACEHOLDER" # TODO:WRITE

                "The door might be too obvious, but that's the surprise":
                    centered "PLACEHOLDER" # TODO:WRITE

                "The window will do just fine":
                    centered "PLACEHOLDER" # TODO:WRITE

        show janos idle at right
        janos """
        As it happens, the prince gave full jurisdiction over this matter.
        So we can cut all the bullshit, etiquette and courtly diplomacy.
        The hour is nigh, and you are:
        """   
        
        if story_janos_guilty:
            janos "Guilty."
            hide janos
        else:
            janos "Not guilty."
            hide janos

            call victory # The End.

        

                
            
            


                
                    

    
        

    

    hide screen dynamic_stats
    scene black
    with fade
    return