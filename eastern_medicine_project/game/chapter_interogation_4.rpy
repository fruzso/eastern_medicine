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
            hide

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
                
            "Patience is a virtue":
                
                    

    
        

    

    hide screen dynamic_stats
    scene black
    with fade
    return