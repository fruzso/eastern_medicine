label carpark:
    # A memory of the Carpark
    # PLOTPOINTS: the mentors letter

    scene black
    with fade

    play music background_music_carpark fadein 1.0 volume 1.0 loop

    centered """
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
            I suddenly remember him slipping an envelope to me in the hospital, whispering: Hide it. Now.

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
            janos "So the Emilio, the Tremere... Again. Tell me more. {image=dice}"
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
            
        "Tell a lie {image=dice}":
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
                
                I remembered him slipping an envelope in the hospital, whispering: Hide it. Now.

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

    show pc idle at right
    pc """
    After I went home I took out the envelope from my pocket.

    -In case of emergency-

    is what it said.
    """

    menu open_envelope:
        "Did you open it then?"
        "Obviously":
            pc "Obviously I opened it right away."
            hide pc

            show janos idle at right
            janos "Would you say that you were in an emergency at that point then?"
            hide janos
            
            show pc idle at right
            pc """
            No not really. 
            
            But I like to know my options. 
            
            You know, in case an emergency arises."
            """

        "Tried to resist {image=dice}":
            $ roll_pc = Roll(pc_sheet.willpower, n_hunger_dice=0, difficulty=5)
            $ roll_pc.roll()
            
            if roll_pc.is_success:
                show pc idle at right
                pc """
                I am a curious creature but as I said:
                    
                I trust my Tremere friend. 

                I opened it when I left the building that night. 
                """
              
            else:
                show pc idle at right
                pc """
                I was too curious to resist.
                """
                

    pc """
    There was an address on the other side of the envelope.

    And inside there was a letter. 

    At first I thought it was just a friendly note.
    """
    hide pc

    show janos idle at right
    janos """
    I would be happy if you refrained from telling me all the unnecessary steps you took inside that labyrinth of your damned mind.
    """
    hide janos 

    show pc idle at right
    pc "Excuse me for not reading your mind for your wishes about the details."
    hide pc 

    show janos idle at right
    janos "What was in the letter?"
    hide janos

    show pc idle at right
    pc """
    An address.

    I realized this is not a coincidence, so I went there as fast as I could.

    But it turned out to be a carpark. 
    """
    hide pc

    centered "As you are reciting your memories you remember that however much you tried to get to the car you just couldn't."
    
    show pc idle at right
    pc """
    This cannot be right - I thought. There must have been something deeper hidden here, something invisible for the bare eyes...

    But not to the seeing one. {image=roll}
    """
    hide pc
    
    $ roll_pc = Roll(pc_sheet.WITS + pc_sheet.AUSPEX, pc_sheet.hunger, difficulty=4)
    $ roll_pc.roll()
    if roll_pc.is_success:
        show pc idle at right
        pc """
        As I turned on my vision I suddenly saw those geometric lines and circles 
        
        so familiar to me by now drawn onto the wall.
        """
    else:
        $ pc_sheet.lose_willpower(1)
        call change_dynamic_stats("worse")

        show pc idle at right
        pc """
        I was pretty sure I needed to see something there but I was too shocked still to focus my powers in one sitting.

        I tried several times with breaks when finally, I started to see them.

        Those geometric lines and circles so familiar to me by now drawn onto the wall!
        """
        hide pc

    show pc idle right 
    pc "I used to see tons of these back then while working with Emilio."
    hide pc

    centered "Now, this is what you gain from being open to some that others would just call usurpers."
    
    centered "Pretty karmic - one could say if one believed in karma."
    
    centered "Although it is not too likely that another life would wait for you."
    
    centered "Maybe another death."

    show janos idle at right 
    janos """
    That's most interesting. 
    
    So may I ask, how did those little scribbles let you in the car? 

    Please do continue to fascinate me. 
    """
    hide janos

    show pc idle at right
    pc """
    I remembered that particular magic ward. 
    
    I remembered I needed three words spelled out in my blood to unlock Emilio's seal.

    That was there just to provide a safe place for me to stay - I was sure by then. 

    It would be uncharacteristic of the Tremere not to have left me with some guidence.
    """
    hide pc

    show janos idle at right 
    janos """
    So did Emilio come himself to guide you personally through this little workshop of his? 
    """
    hide janos

    show pc idle at right 
    pc "The letter!"
    hide pc

    $ hit_count = 0
    
    call screen letter(choice="letter_choice_1")
    
    menu letter_choice_1:
        "The first word"

        "Take another look at the letter":
            call screen letter(choice="letter_choice_1")
        "Marylin the nosferatu":
            jump letter_choice_2
        "Magnet":
            $ hit_count += 1
            jump letter_choice_2
        "Power":
            jump letter_choice_2

    menu letter_choice_2:
        "The second word"

        "Take another look at the letter":
            call screen letter(choice="letter_choice_2")
        "Safety":
            $ hit_count += 1
            jump letter_choice_3
        "Friend":
            jump letter_choice_3
        "Mistress":
            jump letter_choice_3

    menu letter_choice_3:
        "The third word"

        "Take another look at the letter":
            call screen letter(choice="letter_choice_3")
        "Feather":
            $ hit_count += 1
        "Cain":
            pass
        "Protector":
            pass

    centered "You rip open a vein on your forearm and begin to paint."
    if hit_count == 3:
        centered """
        The three words shine bright in your bloody handwriting.
        
        The doors of the car, as if by magic flung open.

        It's not home, but sure as hell, it's nice to spend the remainder of the day in a light-tight wagon.
        """
    else:
        $ pc_sheet.get_hungry(3 - hit_count)
        call change_dynamic_stats("worse")

        centered """
        The three words look pale and ugly in your bloody handwriting.
        
        You cannot get closer to the car, the wards' defences hold fast.

        You take a considerable amount of time and blood to figure out the words.

        Finally, you get in.

        At least you can wait out the day.
        """

    hide screen dynamic_stats
    scene black
    with fade
    return