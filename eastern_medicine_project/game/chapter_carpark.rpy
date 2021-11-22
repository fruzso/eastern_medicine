label carpark:
    # A memory of the Carpark
    # PLOTPOINTS: the mentors letter

    scene black
    with fade

    play music background_music_carpark fadein 1.0 volume 1.0 loop

    centered """
    Where did you go next?

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
            Suddenly, Emilio appeared before my eyes.

            Not the real Emilio of course. 
            """
            hide pc

            show janos idle at right
            janos "Not the ..."
            hide janos

            show pc idle at right
            pc """
            A memory. An inverse vision, if you will. 
            """
            hide pc

            show janos idle at right
            janos "And what did this memory of Emilio did, if I may ask?"
            hide janos

            show pc idle at right
            pc """
            I suddenly remember him slipping an envelope to me, whispering: Hide it. Now.

            So I naturally hid it. 

            I trust him and there was no space for questions, but he looked a bit disturbed. 

            Not disturbed as tremere look when they gibber their spells. 

            Proper disturbed.    
            """
            hide pc

            centered """ You see Janos quickly flipping through his pages. 
            He quickly scribbles something down.  
            """

            show janos idle at right
            janos "So the Tremere's name is Emilio. Tell me more."
            hide janos

            $ roll_janos = Roll(janos_sheet.CHARISMA + janos_sheet.DOMINATE, janos_sheet.hunger, difficulty=0)
            $ roll_janos.roll()
            $ roll_pc = Roll(pc_sheet.WITS + pc_sheet.RESOLVE, pc_sheet.hunger, difficulty=roll_janos.margin_of_success)
            $ roll_pc.roll()

            if roll_pc.is_success:
                # PC escapes Dominate
                centered """ You feel you touched on something important. You must have. He is trying to dominate you.
                But he must be very frustrated by now because you escape his attempt to force your mind. 

                Still the effort breaks your concentration.
                """

                scene black
                with fade

                scene background_video_interogation
                with Dissolve(3.0)            

                menu cooperation:
                    "Are you cooperating regardless?"

                    "Yes. You remember, afterall his judgment matters in this case":
                        show pc idle at right
                        pc "Alright, what do you wanna know?"
                        hide pc

                        scene black
                        with fade

                        scene background_video_carpark
                        with Dissolve(3.0)

                        jump carpark_minigame

                    "No way, it's time for him to leave me alone":
                        show pc idle at right
                        pc "That's quite enough for one night. You're gonna let me go now." 
                        hide pc
                        
                        menu run_or_fight:
                            "What do you do?"

                            "Try and escape this filthy depressing basement":
                                jump run

                            "Attack Janos":
                                jump fight_pc_start
                            
                    
                
            else:
                # PC is dominated
                centered """ You feel you touched on something important. You must have. He is trying to dominate you.
                But he must be very frustrated by now because his will crushes through all your mental defenses. 
                You have now choice but to obey. 
                """
                show pc idle at right
                pc "Alright, alright. No need to be hostile. Afterall we are not enemies, am I right?"
                hide pc
                
                show janos idle at right
                janos "That is hardly for you to decide at this moment."

                jump carpark_minigame
            
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

                show janos idle at right
                "And was this before or after you spent the night in this car?"
                hide janos

                centered """He shows you a picture of a car. That's the car. You recognize it.
                There is no question about it.""" 
                
                centered "He knows."

                centered "You start to feel the tight look in his eyes while his fangs appear once again."

                centered "It's not worth lying about this. Afterall it was just an innocent sleeping experience."
                jump carpark_minigame

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

                centered "Sigh."

                show pc idle at right
                pc """
                A memory of Emilio, a Tremere friend popped into my mind. 
                
                I remembered him slipping an envelope to me, whispering: Hide it. Now.

                So I naturally hid it. 

                I trust him and there was no space for questions, but he looked a bit disturbed. 

                Not disturbed as tremere look when they gibber their spells. 

                Proper disturbed. 
                """
                hide pc
                jump carpark_minigame


label carpark_minigame:
    show janos idle at right
    janos "I am waiting. Continue."
    hide janos

    #TODO: CODE + STORY Insert minigame here
    

    hide screen dynamic_stats
    scene black
    with fade
    return