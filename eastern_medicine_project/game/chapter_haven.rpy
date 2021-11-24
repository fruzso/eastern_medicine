init python:
    renpy.music.register_channel("haven", "music", True)

label haven:
    # A memory of the PC's haven
    # PLOTPOINTS: Fight with the S.I. Agents

    scene black
    with fade
    
    play music background_music_haven1 volume 0.5 loop
    # play haven background_music_haven volume 0.5

    centered "Hearing Janos' words, you feel transported back to August 21."

    centered "You remember yesturday."

    centered "Yes, the day."

    if pc_sheet.CLAN == "Malkavian":
        centered "Dreaming of a spier, fleshed out from darkness pulling medical strings with its leg over a hazy landscape."
    else:
        centered "Dreamless, as always."

    centered "You were in your lightproof haven, lying in torpor."

    scene background_video_haven
    with Dissolve(2.0)

    call show_dynamic_stats

    show pc idle at right
    pc "I was doing what all godfearing kindred were: Laying in torpor."
    hide pc

    show janos idle at right
    janos """
    Let us not bring God in the picture, just yet.

    How did you know that your haven has been breached?
    """
    hide janos

    call haven_intro
    menu:
        "It was a piece of the door, landing in my...":
            call haven_violent_arrival
            call haven_interlude_1
            call haven_interlude_2
            call haven_agents_in_the_living_room

        "I am friends with the Tremere...":
            call haven_friends_with_the_tremre
            call haven_interlude_1
            call haven_interlude_2
            menu:
                "My apartment was..."
                "Full of gear":
                    call haven_full_of_gear
                    call haven_agents_in_the_living_room
                "Not made for war":
                    call haven_empty
                    call haven_agents_in_the_living_room

        "I had a vision" if pc_sheet.AUSPEX >= 2:
            call haven_vision
            call haven_interlude_1
            call haven_interlude_2
            menu:
                "My apartment was..."
                "Full of gear":
                    call haven_full_of_gear
                    call haven_agents_in_the_living_room
                "Not made for war":
                    call haven_empty
                    call haven_agents_in_the_living_room

    jump haven_outro

    label haven_intro:
        "PALCEHOLDER"
        return

    label haven_violent_arrival:
        $ story_violent_arrival = True

        show pc idle at right
        pc """It was a piece of the door, landing in my abdomen.

        Pain can be a pretty handy wake-up call, you see."""
        hide pc

        $ pc_sheet.lose_health(1)
        call change_dynamic_stats("worse")

        show janos idle at right
        janos "Carry on, no need to spare the details."
        hide janos

        return
        
    label freinds_with_the_tremere:
        show pc idle at right
        pc "I am friends with the Tremere, so I had an associate install wards and rituals just in case of something like this."
        hide pc

        show janos idle at right
        janos "Name, please."
        hide janos

        show pc idle at right
        pc "Emilio"
        hide pc

        if story_mention_emilio:
            show janos idle at right
            janos "We seem to be comming back to him."
        else: 
            show janos idle at right

        janos "Carry on, no need to spare the details."
        hide janos

        show pc idle at right
        pc """
        First I sensed an incredible power pulling something out of me.

        But the stange thing was, that it was not pulling around my heart.

        It grabbed me with a thousand tiny muscles everywhere, where blood was circulating within.

        Even with the pain, it took considerable effort to wake up.            
        """

        $ pc_sheet.lose_willpower(1)
        call change_dynamic_stats("worse")
        
        hide pc

        return

    label haven_vision:
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

            centered "you notice that Janos would like to say something else, but he chooses to remain silent"

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

            $ pc_sheet.lose_willpower(1)
            call show_dynamic_stats
          
    label haven_interlude_1:
        show janos idle at right
        janos "So, you were awake. What happened next?"
        hide janos

        return

    label haven_interlude_2:
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

                You could say that I fucked up.

                But here we are. Quite right. In the end we are here.
                """
                hide pc

        show pc idle at right
        pc """
        They were attacking my haven. So naturally it was fuck the masquerade time.

        Grabbed the first weapon I could get my hands on from my emergency staff.

        My apartment was...
        """
        hide pc
        
        return

    label haven_full_of_gear:
        $ story_weapon = "Uzi"

        show pc idle at right
        pc """
        I am a [pc_sheet.ASSUMED_GENDER] who likes to be prepared, you see

        I firmly believe that the attack is the best form of defence

        in any case it never hurts if you have an arsenal at the ready bellow the nightstand.

        My choice fell on my trusted uzi-machine gun.
        """
        hide pc

        show janos idle at right
        janos "My my, we are keeping up to date with technology"

        if pc_sheet.CLAN == "Toreador":
            janos "To be expected with your clan, tough"
        hide janos

        $ story_remaining_si -= 2
        show pc idle at right
        pc """The good thing about modern construction is that they use shit for materials.
        
        I fired a volley in the walls, connecting to the neighbour.
        """

        #TODO: AUDIO uzi gunfire sounds

        pc """It was drywall.
        
        Did not need more than gentle push, and there I was saying hi to a nice downtown family."""

        #TODO: AUDIO small scale wall demolition

        pc """I got behind the bastards back.

        Took out two without any complications. That's what I call surgical preicsion.
        """
        hide pc

    label haven_empty:
        show pc idle at right
        $ story_weapon = "knife"
        pc """
        I mean, I did not really think I had anything to fear.

        Trully, is it not your job, actually, to stop all sort of shit like this form going on.

        Anyway, no use crying over spilt milk.

        Or blood.

        So my weapon of choice was a kitchen knife.

        Good thing, I had a ghoul live there with me back than at the fall of the iron curtain.
        """
        hide pc

        show janos idle at right
        janos "Sounds more like something you would bring to a rural pig killing."
        hide janos

        return

    label haven_agents_in_the_living_room:
        "PLACEHOLDER"

        return
                    
    label haven_outro:
        "PALCEHOLDER"

        return         

    hide screen dynamic_stats
    scene black
    with fade
    return