label interogation_2:
    # The main scene of the game, where the player returns many times
    # PLOTPOINTS: 
    
    scene black 
    with fade 
    
    play music background_music_interrogation volume 0.5 loop

    scene background_video_interogation
    with Dissolve(3.0)

    call show_dynamic_stats

    show janos idle at right
    with Dissolve(1.0)
    janos """
    So, the big one.
    
    What do you remember of August 21?

    And please don't give me any of that patriotic bullshit,

    nothing like {i}I snuggled up fondly with the memories of a great celebration and national glory{/i}
    
    As you say, no bullshit.
    """
    hide janos

    centered "You feel that there is more said than simply words."

    centered "In a split second you realize that the power of the Dark father permiates through Janos' words."

    centered "He is trying to dominate you."

    menu resist_dominate:
        "Do you try to resist?"
        "Yes {image=dice}":
            # Contest Roll
            $ roll_janos = Roll(janos_sheet.CHARISMA + janos_sheet.DOMINATE, janos_sheet.hunger, difficulty=0)
            $ roll_janos.roll()
            $ roll_pc = Roll(pc_sheet.WITS + pc_sheet.RESOLVE, pc_sheet.hunger, difficulty=roll_janos.margin_of_success)
            $ roll_pc.roll()

            if roll_pc.is_success:
                centered "He may be your elder or is it just frustration, nevertheless this is not his lucky day."
                centered "You ressist his attempt."

                $ pc_sheet.gain_willpower(1)
                call change_dynamic_stats("better")

                menu feign_compliance:
                    "Do you want to fake complience?"
                    "Yes":
                        show pc idle at right
                        pc "Here follows an account of everything that happened:"
                        hide pc

                        call end_interrogation_2
                    "No":
                        show pc idle at right
                        pc "Fuck off!"
                        hide pc

                        centered """
                        You meet an ungodly display of the nosferatu's fangs,
                        he is ready to pounce no question about it.
                        """
                        
                        call increase_janos_strikes
                        show janos idle at right
                        janos "This is strike number [janos_strikes]."
                        hide janos
                        
                        show pc idle at right
                        pc "Let me think for a moment."
                        hide pc

                        call end_interrogation_2       
                    
        "No":
            centered """
            You start to search your memories for all the details of the event
            and communicate them as accurately as possible.
            """
            call end_interrogation_2
        
label end_interrogation_2:
    stop music fadeout 1.0
    hide screen dynamic_stats
    scene black
    with fade
    return
    