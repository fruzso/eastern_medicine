label haven:
    # A memory of the PC's haven
    # PLOTPOINTS: Fight with the S.I. Agents

    scene black
    with fade

    show janos idle at right
    janos """
    So, the big one.
    
    What do you remember of August 21?

    And please don't give me any of that patriotic bullshit,

    nothing like - I snuggled up fondly with the memories of a great celebration and national glory - 
    
    As you say, no bullshit.
    """
    hide janos

    pause(1.0)

    "Hearing Janos' words, you feel transported back to August 21."

    "You remember yesturday."

    "Yes, the day."

    "Around midday, when all slef respecting kindred should be in the deathlike slumber of torpor."

    "You were in your lightproof haven."

    scene background_video_haven
    with Dissolve(2.0)

    call show_dynamic_stats

    show pc idle at right
    pc "I was doing what all godfearing kindred would be doing. Laying in torpor."
    hide pc

    show janos idle at right
    janos """
    Let us not bring God in the picture, just yet.

    How did you know that your haven has been breached?
    """
    hide janos

    menu sensing_the_intrusion:
        "It was a piece of the door, landing in my...":
            $ story_violent_arrival = True

            show pc idle at right
            pc """
            It was a piece of the door, landing in my abdomen.

            Pain can be a pretty handy wake-up call, you see.
            """
            hide pc

            $ pc_sheet.lose_health(1)
            call change_dynamic_stats
            if pc_sheet.health == 0:
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

            $ pc_sheet.lose_willpower(1)
            call change_dynamic_stats
            if pc_sheet.WILLPOWER = 0:
                call lost_willpower
            
            hide pc

        "I had a vision" if pc_sheet.AUSPEX >= 2:
            $ story_si_vision = True

            show pc idle at right
            if pc_sheet.CLAN == "Malkavian":
                pc """
                It was not the first time that my dreams brought me ... How should I say, that even you would understand...

                Hm...
                
                You have heard of visions, soothsaying, portents and the like, right?"""
                hide pc

                show janos idle at right
                janos "Yes, naturally."
                hide janos

                "/you notice that Janos would like to say something else, but he chooses to remain silent/"

                show pc idle at right
                pc """
                Let's just say that I had a feeling that it would be a terribly good idea to kick in the door.
                
                But that is just not my style.

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
                hide janos

                show pc idle at right
                pc "well, I did."
                hide pc

                "/You lose 1 point of willpower./"
                if pc_sheet.WILLPOWER = 0:
                    call lost_willpower


    show janos idle at right
    janos "So, you were awake. What happened next?"
    hide janos

    menu comming_to_terms_with_reality:
        "What happened next?"
        "I knew something was wrong" if not story_violent_arrival:
            show pc idle at right
            pc "There was no question question about it, something sinister was going on."
            hide pc

            show janos idle at right
            janos """
            Yes
            
            Please, do share.
            """
            hide janos

            show pc idle at right
            pc "I had little information you see, so I waited."
            hide pc

        "I couldn't believe it" if not story_si_vision:
            show pc idle at right
            pc """
            It was my haven. Unpenetrated for [pc_sheet.AGE] years.
            
            That is not something everyone can tell.

            It was still quite unbelievable that an attack on it was immanent.

            Yet I mustered all my resolve and started to stratagize.
            """
            hide pc

        "I was shocked":
            show pc idle at right
            pc """
            Believe it or not, I was completely shoched.

            It took a few good seconds to gather myself and face what was comming.

            You could say that I fucked it up.

            But here we are. Quite right. In the end we are here.
            """
            hide pc
    
    menu first_encounter:
        "How did it start?"
        "I went on the offensive":
            show pc at right
            pc """
            They were attacking my haven. So naturally it was fuck the masquerade time.

            Grabbed the first weapon I could get my hands on from my emergency staff.

            My apartment was...
            """

            menu gear_up:
                "My apartment was..."
                "Full of gear":
                    show pc idle at right
                    pc """
                    I am a [pc_sheet.ASSUMED_GENDER] who likes to be prepared, you see

                    I firmly believe that the attack is the best form of defence

                    in any case it never hurts if you have an arsenal at the ready bellow the nightstand.
                    """
                    hide pc

                    menu weapon_choice_heavy:
                        "you grabbed a..."
                        "Uzi machinegun":
                            "PLACEHOLDER"

                        "pistol":
                            "PLACEHOLDER"

                        "Ceremonial sword":
                            "PLACEHOLDER"


                        "nothing, I am the weapon":
                            "PLACEHOLDER"
                        
                    
                "Not made for war":
                    show pc idle at right
                    pc """
                    I mean, I did not really think I had anything to fear.

                    Trully, is it not your job, actually, to stop all sort of shit like this form going on.

                    Anyway, no use crying over spilt milk.

                    Or blood.
                    """
                    hide pc
                    

        "I went on the defensive":
            "PLACEHOLDER"
            #block of code to run
        
    

    hide screen dynamic_stats
    scene black
    with fade
    return