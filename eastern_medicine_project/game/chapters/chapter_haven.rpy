label haven:
    # A memory of the PC's haven
    # PLOTPOINTS: Fight with the S.I. Agents

    scene black
    with fade
    
    play music background_music_haven volume 0.5 loop

    centered "Hearing Janos' words, you feel transported back to August 21."

    centered "You remember yesturday."

    centered "Yes, the day."

    if pc_sheet.CLAN == "Malkavian":
        centered "Dreaming of a spider, fleshed out from darkness pulling medical strings with its leg over a hazy landscape."
    else:
        centered "Dreamless, as always."

    centered "You were in your lightproof haven, lying in torpor."

    scene background_video_haven
    with Dissolve(2.0)

    call show_dynamic_stats

    call haven_intro
    menu:
        "It was a piece of the door, landing in my...":
            call haven_violent_arrival
            call haven_interlude_1
            call haven_agents_in_the_room_intro
            menu:
                "Attack the closest one {image=dice}":
                    call haven_attack_closest
                "Try to find cover {image=dice}":
                    call haven_cover
                "Vanish {image=dice}" if pc_sheet.OBFUSCATE >= 3:
                    call haven_hidden_attack

        "I am friends with the Tremere...":
            call haven_friends_with_the_tremre
            call haven_interlude_1
            call haven_interlude_2
            menu:
                "My apartment was..."
                "Full of gear":
                    call haven_full_of_gear
                    call haven_agents_in_the_room_intro
                    menu:
                        "Shoot 'em up {image=dice}":
                            call haven_shoot_em_up
                        "Try to find cover {image=dice}":
                            call haven_cover
                        "Vanish {image=dice}" if pc_sheet.OBFUSCATE >= 3:
                            call haven_hidden_attack
                "Not made for war":
                    call haven_empty
                    call haven_agents_in_the_room_intro
                    menu:
                        "Attack the closest one {image=dice}":
                            call haven_attack_closest
                        "Try to find cover {image=dice}":
                            call haven_cover
                        "Vanish {image=dice}" if pc_sheet.OBFUSCATE >= 3:
                            call haven_hidden_attack

        "I had a vision" if pc_sheet.AUSPEX >= 2:
            call haven_vision
            call haven_interlude_1
            call haven_interlude_2
            menu:
                "My apartment was..."
                "Full of gear":
                    call haven_full_of_gear
                    call haven_agents_in_the_room_intro
                    menu:
                        "Attack the closest one {image=dice}":
                            call haven_attack_closest
                        "Try to find cover {image=dice}":
                            call haven_cover
                        "Vanish {image=dice}" if pc_sheet.OBFUSCATE >= 3:
                            call haven_hidden_attack

                "Not made for war":
                    call haven_empty
                    call haven_agents_in_the_room_intro
                    menu:
                        "Attack the closest one {image=dice}":
                            call haven_attack_closest
                        "Try to find cover {image=dice}":
                            call haven_cover
                        "Vanish {image=dice}" if pc_sheet.OBFUSCATE >= 3:
                            call haven_hidden_attack

    jump haven_outro

    label haven_intro:
        show pc idle at right
        pc "I was doing what all godfearing kindred were: Laying in torpor."
        hide pc

        show janos idle at right
        janos """
        Let us not bring God in the picture, just yet.

        How did you know that your haven has been breached?
        """
        hide janos
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
        
    label haven_friends_with_the_tremre:
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

        return

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

    label haven_agents_in_the_room_intro:
        centered "And there you were in the living room."

        centered "First comes a blinding flash"

        hide screen dynamic_stats

        scene white
        with fade

        #TODO:AUDIO put in iiiiiii sound

        centered """{color=#000000}Smoke covers everything, as the trained agents of the second inquisition storm the room, all [story_remaining_si] of them.{/color} 
        """
        return

    label haven_attack_closest:
        call haven_reveal_the_room
        
        centered """There is no time to waste.
        
        You pounce at the closest agent.
        """

        # Roll to attack
        $ roll_pc = Roll(pc_sheet.DEXTERITY, pc_sheet.BRAWL, difficulty=3)
        $ roll_pc.roll()

        if roll_pc.is_success:
            centered "You've got one of them."

            $ story_remaining_si -= 1

            if story_remaining_si >= 1:
                show agent idle at right
                agent "Man. Down, I repeat man down."
                hide agent
            else:
                centered "That was the last of them."
        return

    label haven_cover:
        call haven_reveal_the_room
        centered """You try to rely on your familiarity ith the location, remembering where everything is supposed to be as you take cover."""
        
        # Roll willpower to stay awake
        $ roll_pc = Roll(pc_sheet.willpower, pc_sheet.hunger, difficulty=5)
        $ roll_pc.roll()

        if pc_roll.is_success:
            centered "Nothing can break your will."
        else:
            centered "It's daytime. Hard to stay alive and standing, let alone jump to the spot you have found is excuciating."

            $ pc_sheet.lose_willpower(1)
            call change_dynamic_stats("worse")

        # Roll manuevering to find a good sport
        $ roll_pc = Roll(pc_sheet.DEXTERITY + pc_sheet.AWARENESS, pc_sheet.hunger, difficulty=5)
        $ roll_pc.roll()

        centered "You take cover dehind the half blown-up table."
        if pc_roll.is_success:
            centered """It's nothing much, but it will do.
            
            You spot a man approaching.
            
            Quickly grab his leg and tear him to the ground."""

            $ story_remaining_si -= 1

            #TODO: AUDIO somesoundeffect maybe?
        
        else:
            centered """It's not good for shit.

            You suffer 2 shots to the arm."""

            # TODO: AUDIO add 2 gunshots.

            $ pc_sheet.lose_health(2)
            call change_dynamic_stats("worse")

        return
    
    label haven_hidden_attack:
        call haven_reveal_the_room

        centered "It's time to become unpercievable, hidden, ghost, or even less."

        # Rousecheck
        if not pc_sheet.rouse_check():
            call change_dynamic_stats("worse")
            centered "You feel the growing hunger pulse through your veins."                   

        # Roll Vanish
        $ roll_janos = Roll(janos_sheet.WITS + janos_sheet.AWARENESS, janos_sheet.hunger, difficulty=0)
        $ roll_janos.roll()
        $ roll_pc = Roll(pc_sheet.WITS + pc_sheet.OBFUSCATE, pc_sheet.hunger, difficulty=roll_janos.margin_of_success)
        $ roll_pc.roll()

        if not roll_pc.is_success:
            centered "Damn, these mother fuckers probably went to braincamp or something."
        else:
            centered """You have become truly invisible
            
            Well, at least that is what their brain is telling them.
            
            To them, you are the ghost in the machine."""

        show agent idle at right
        agent "Search the room!"
        hide agent

        show agent idle at left
        agent "Roger, Roger"
        hide agent

        return

        show pc ide at right
        if pc_roll.is_success and story_weapon == "Uzi": # Still using the last roll.
            centered "Noone can dodge 20 bullets per magazine when lunched from the back of their necks"
            $ story_remaining_si -= 3
            #TODO: AUDIO: que in 3 uzi bullet burst sounds
            centered "3 agents fall to the ground almost simultanously."
            #TODO: AUDIO que in 3 death screams
        if pc_roll.is_success and story_weapon == "Knife":
            centered "A kitchen knife is good enough if stand close enough to count the hairs on the backs of their necks."
            $ story_remaining_si -= 2
            #TODO: AUDIO: que in knife slashes
            #TODO: AUDIO que in 2 death screams
        else:
            #any other case
            centered """You break necks,
            
            bite throats,
            
            tear of limbs and whatever you can find.
            
            At the same time you get your fair share of wounds as well."""
            $ story_remaining_si -= 2
            $ pc_sheet.lose_health(2)
            call change_dynamic_stats("worse")
        hide pc

        return

    label haven_shoot_em_up:
        call haven_reveal_the_room

        centered "Quickly daashing around the room you spray them with all the bullets God created and more."
        
        # Roll Shoot
        $ roll_pc = Roll(pc_sheet.DEXTERITY + pc_sheet.FIREARMS, pc_sheet.hunger, difficulty=3)
        $ roll_pc.roll()

        if roll_pc.margin_of_success <= 0:
            #TODO: AUDIO: gunfigh sound

            centered """
            Who are we kidding, you are no trained marksman.
            
            For all your attempts, none of them fall to the ground.

            They, on the other hand, know how to handle a gun.
            """

            $ pc_sheet.lose_health(4)
            call change_dynamic_stats("worse")

        elif pc_roll.margin_of_success == 1:
            $ story_remaining_si -= 1
            #TODO: AUDIO: que in 1 uzi bullet burst sounds
            centered "[roll_pc.margin_of_success] agent falls to the ground."
            #TODO: AUDIO que in 1 death screams

            $ pc_sheet.lose_health(1)
            call change_dynamic_stats("worse")

        else:
            $ story_remaining_si -= pc_roll.margin_of_success
            #TODO: AUDIO: que in 3 uzi bullet burst sounds
            centered "[pc_roll.margin_of_success] agents fall to the ground almost simultanously."
            #TODO: AUDIO que in death scream
            
        return

    label haven_reveal_the_room:
        scene background_video_haven
        with Dissolve(2.0)

        call show_dynamic_stats

        return
                          
    label haven_outro:
        show pc idle at right
        if not story_remaining_si == 0:
            #TODO: AUDIO Insetr frenzy sounds
            centered """ The smell of blood mixed with new age gunpowder fills the air.

            Your nostrils widen up, you could literally eat up the air, when all hell truly breaks out as you lose control,

            Disconnected images of bone, fangs, gunshot wounds swarm in your minds, yet nothing distinctive.

            One thing is for sure, when you regain conciousness, you don't find anyone alive."""

            $ pc_sheet.get_hungry(2)
            $ pc_sheet.lose_health(3)
            call change_dynamic_stats("worse")
        
        pc "I have to admit..."

        menu:
            "How are you feeling?"

            "Proud":
                pc """I feel fuckin proud. Not everyone could have done what I did.
                
                Team [pc_sheet.NAME]: 1

                Second Inquisiion: 0

                Fuck yeah!
                """
                hide pc

            "Ashamed":
                pc "I have to admint, this will remain as a stain on my soul forever. Considering everything, still, it was too brutal."
                hide pc

        show janos idle at right
        janos """We have more important questions to adress.
        
        Let's continue"""
        return         

    hide screen dynamic_stats
    scene black
    with fade
    return