init python:
    renpy.music.register_channel("noise_carpark", "music", True)

label carpark:
    # A memory of the Carpark
    # PLOTPOINTS: the mentors letter

    scene black
    with fade

    play music background_music_carpark fadein 1.0 volume 1.0 loop
    play noise_carpark background_noise_carpark fadein 1.0 volume 0.5 loop
    
    show pc idle at right
    pc """ I needed a place to stay where they couldn't find me.

    And I couldn't have risked going to any of my friends. 
    """
    hide pc

    centered """
    You remember the carpark distinctly. 
    
    It was a little more than 4 blocks away.
    """

    scene background_video_carpark
    with Dissolve(1.5)

    call show_dynamic_stats

    menu:
        "Do you tell him about the carpark?"

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
            janos "And what did this memory of Emilio do, may I ask?"
            hide janos

            show pc idle at right
            pc "I remembered him slipping an envelope into my pocket back in the hospital, quickly whispering: Hide it. Now."
            hide pc
            
            show janos idle at right
            if story_mention_emilio:
                janos "Hmm. Maybe I should rather be questioning Emilio."
                hide janos
            else:
                call increase_janos_strikes
                janos """
                Quite a revelation we are witnessing.

                Hmm...

                I am uncertain as to wheather you have realized this little slip of the tounge

                or rather, inconsistency. 

                Tsk, tsk, tsk, failing to mention a meeting with a fellow kindred during interrogation.

                Strike number [janos_strikes].
                """
                hide janos

                show pc idle at right
                pc "Scaaary."
                hide pc
            
            show pc idle at right
            pc """
            So I naturally hid the envelope. 

            He enjoys my complete trust and there was no space for questions, even tough he looked a bit disturbed. 

            Not disturbed as tremere look when they gibber their spells. 

            Properly disturbed.    
            """
            hide pc

            centered """ You see Janos quickly flipping through his pages. 
            He quickly scribbles something down.  
            """

            show janos idle at right
            janos "So this Emilio, the Tremere... Again. Do not even dare to leave the seemingly most insignificant of detail out! {image=dice}"
            hide janos

            $ roll_janos = Roll(janos_sheet.CHARISMA + janos_sheet.DOMINATE, janos_sheet.hunger, difficulty=0)
            $ roll_janos.roll()
            $ roll_pc = Roll(pc_sheet.WITS + pc_sheet.RESOLVE, pc_sheet.hunger, difficulty=roll_janos.margin_of_success)
            $ roll_pc.roll()

            if roll_pc.is_success:
                # PC escapes Dominate
                centered """ You feel you touched on something important. You must have.
                
                He is trying to dominate you.
                
                But he must be very frustrated by now because you escape his attempt to force your mind. 

                Still the effort breaks your concentration, for a moment you forget where you were in the story.
                """

                scene black
                with fade

                scene background_video_interogation
                with Dissolve(3.0)            

                menu cooperation:
                    "Are you cooperating regardless?"

                    "Yes. Afterall it's his judgment what matters in this case":
                        show pc idle at right
                        pc "Alright, I'll tell you more."
                        hide pc

                        scene black
                        with fade

                        scene background_video_carpark
                        with Dissolve(3.0)

                        jump carpark_minigame

                    "No way, it's time for him to leave me alone":
                        centered """ You feel that is has been grossly overstepping his jurisdiction to say the least
                        
                        You decide not to take his aggression anymore.
                        
                        It's tiem to stand your ground."""

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
                centered """ You feel you touched on something important. You must have. 
                
                He is trying to dominate you.

                But he must be very frustrated by now because his will crushes through all your mental defenses.

                You have now choice but to obey. 
                """

                show pc idle at right
                pc "Alright, alright. No need to be hostile. Afterall we are not enemies, right?"
                hide pc
                
                show janos idle at right
                janos "I shall reserve the right to make that judgement."
                hide janos

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
                janos """And was this before or after you spent the night in this car?
                """
                hide janos

                centered """He shows you a picture of a car. That's the car. You recognize it.
                There is no question about it.
                
                He knows.
                
                You start to feel the tight look in his eyes while his fangs appear once again.
                
                It's not worth lying about this further.
                """
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
                pc "I went to fireman's club. It was, I am not even sure how to describe it. You know how it is."
                hide pc

                call increase_janos_strikes
                show janos idle at right
                janos """
                That is quite a turn of events.
                
                Considering that if my ghouls are to be believed,
                
                it closed down 3 years ago.

                That is strike number [janos_strikes].
                """
                hide janos

                centered "Sigh."

                show pc idle at right
                pc """
                So,

                a memory of Emilio, a Tremere friend popped into my mind. 
                
                I remembered him slipping an envelope into my pocket at the hospital, whispering: Hide it. Now.

                So I naturally hid it. 

                I trust him and there was no space for questions, but he looked a bit disturbed. 

                Not disturbed as tremere look when they gibber their spells. 

                Proper disturbed. 
                """
                hide pc

                show janos idle at right
                if story_mention_emilio:
                    janos "Hmm. Maybe I should rather be questioning Emilio."
                    hide janos
                else:
                    call increase_janos_strikes

                    janos """
                    Quite a revelation we are witnessing.

                    Hmm...

                    I am uncertain as to wheather you have realized this little slip of the tounge.

                    Tsk, tsk, tsk, failing to mention a meeting with a fellow kindred during interogation.

                    Strike number [janos_strikes].
                    """
                    hide janos

                    show pc idle at right
                    pc "Scaaary."
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
            
            You know, in case an emergency arises.
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
    There was an address in the envelope, written on a torn piece of paper.

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
    pc "Excuse me for not reading your mind."
    hide pc 

    show janos idle at right
    janos "Damn it, what was in the letter?"
    hide janos

    show pc idle at right
    pc """
    First of all, an address.

    I realized this is not a coincidence, so I went there as fast as I could.

    But it turned out to be a carpark. 
    """
    hide pc

    centered "As you are reciting your memories you remember however hard you tried getting to the car you simply couldn't."
    
    show pc idle at right
    pc """
    This cannot be right. There must be something more to this, something invisible to the naked eye...

    I know what to do. {image=dice}
    """
    hide pc
    
    $ roll_pc = Roll(pc_sheet.WITS + pc_sheet.AUSPEX, pc_sheet.hunger, difficulty=4)
    $ roll_pc.roll()

    if roll_pc.is_success:
        show pc idle at right
        centered """
        As you liberate your sense you suddenly see the geometric lines, circles and symbols
        
        so familiar by now, casually drawn on the wall.
        """
    else:
        $ pc_sheet.lose_willpower(1)
        call change_dynamic_stats("worse")

        show pc idle at right
        centered """You are pretty sure you need to see something here,
        
        but nothing gives.
        
        Maybe you are still too much in shock, maybe you cannot do this in one sitting...

        You try several times,
        
        when finally, you start seeing them:

        The geometric lines, circles and symbols so familiar by now casually drawn on the wall!
        """
        hide pc

    show pc idle at right 
    pc "I used to see tons of these back then while working with Emilio."
    hide pc

    centered """Now, this is what you gain from being open to some that others would just call usurpers.
    
    Pretty karmic - one could say if one believed in karma.
    
    Although it is not too likely that another life would wait for you.
    
    Maybe another death.
    """

    show janos idle at right 
    janos """
    That's most interesting. 
    
    So may I ask, how did those little scribbles let you in the car? 

    Please do continue to fascinate me. 
    """
    hide janos

    show pc idle at right
    pc """

    I remembered I needed three words spelled out in my blood to unlock Emilio's seal.

    That was there just to provide a safe place for me to stay - I was sure by then. 

    It would have been uncharacteristic of the Tremere not to have left me with some guidence.
    """
    hide pc

    show janos idle at right 
    janos """
    So did Emilio come himself to guide you personally through this little workshop of his? 
    """
    hide janos

    show pc idle at right 
    pc "Daah, he'd given me the letter!"
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
    show pc idle at right
    pc """ That's where I found refuge.

    Once I felt confident enough, I went to Elysium, where I got word that you'd been looking for me.
    """
    hide pc

    show janos idle at right
    janos "And here we are."
    hide janos

    show pc idle at right
    pc "Here we are."
    hide pc

    hide screen dynamic_stats

    stop music fadeout 1.0
    stop noise_carpark fadeout 1.0
    scene black
    with fade
    return