label haven:
    # A memory of the PC's haven
    # PLOTPOINTS: Fight with the S.I. Agents

    scene black
    with fade
    
    play music background_music_haven volume 0.5 loop

    centered "Hearing Janos' words, you feel transported back to August 21."

    centered "You remember yesterday."

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
        janos """Let us not bring God in the picture, just yet."""
        hide janos

        if pc_sheet.CLAN == "Malkavian":
            show pc idle at right
            pc "Fang God!"
            hide pc

            show janos idle at right
            janos "..."
            hide janos

            show pc idle at right
            pc "C'mon, no reaction?"
            hide pc
        else:
            show pc idle at right
            pc "Never picked you for a religious vampire."
            hide pc
        
        show janos idle at right
        janos """
        How did you know that your haven has been breached?
        """
        hide janos
        return

    label haven_violent_arrival:
        $ story_violent_arrival = True

        show pc idle at right
        pc """It was a piece of the door landing in my abdomen.

        Pain can be a pretty handy wake-up call."""
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
        pc "Emilio."
        hide pc

        if story_mention_emilio:
            show janos idle at right
            janos "We seem to be comming back to him."
        else: 
            show janos idle at right
        
        $ story_mention_emilio = True

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

            centered "You notice that Janos would like to say something else, but he chooses to remain silent"

            show pc idle at right
            pc """
            Let's just say that I had a feeling that it would be a terribly good idea to kick in the door.
            
            But that is just not my style.

            So, I had a pretty good idea what was going on.
            """
            hide pc

            show janos idle at right
            janos "You still had to wake up."
            hide janos

            show pc idle at right
            pc """Quite so.
            
            It was no picnic, I have to admit.

            But when you know, you know, you know.
            """
            hide pc

            show janos idle at right
            janos "To be honest, I don't."
            hide janos

            show pc idle at right
            pc "Well, I did."
            hide pc

            $ pc_sheet.lose_willpower(1)
            call show_dynamic_stats
        
        else:
            pc """
            I don't usually dream, you see. 

            But that day I had these very clear visions entering my mind. 

            Visions of an armed S.W.A.T. team gearing up in front of my apartment door.  

            Not what the doctor would recommend. 
            """
            hide pc
          
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
                pc "There was no question about it, something sinister was going on."
                hide pc

                show janos idle at right
                janos """
                Yes.
                
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

                Yet I mustered all my resolve and started to strategize.
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
        They were attacking my haven. So I thought it was fuck the masquerade time.

        Grabbed the first weapon I could get my hands on from my emergency stash."""
        hide pc
        
        return

    label haven_full_of_gear:
        $ story_weapon = "Uzi"

        show pc idle at right
        pc """
        I am a [pc_sheet.ASSUMED_GENDER] who likes to be prepared, you see.

        I firmly believe that the attack is the best form of defence.

        In any case it never hurts if you have an arsenal at the ready below the nightstand.

        My choice fell on my trusted uzi-machine gun.
        """
        hide pc

        show janos idle at right
        janos "My my, we are keeping up to date with technology."

        if pc_sheet.CLAN == "Toreador":
            janos "It's to be expected with your clan, tough."
        hide janos

        $ story_remaining_si -= 2
        show pc idle at right
        pc "The good thing about modern construction is that they use shit for materials."

        play sound machine_gun_longer
        
        pc "I fired a volley in the walls, connecting to the neighbour."

        pc "It was drywall."

        play sound wall_breaking
        
        pc "Did not need more than a gentle push, and there I was saying hi to a nice downtown family next door."

        pc "I got behind the bastards' back."

        play sound machine_gun_single
        queue sound death_scream_2
        queue sound machine_gun_single
        queue sound death_scream_3

        pc "Took out two without any complications. That's what I call surgical precision."
        hide pc

        return

    label haven_empty:
        show pc idle at right
        $ story_weapon = "knife"
        pc """
        I mean, I did not really think I had anything to fear.

        Truly, is it not your job, actually, to stop all sorts of shit like this form going on.

        Anyway, no use crying over spilt milk.

        Or blood.

        So my weapon of choice was a kitchen knife.

        Good thing, I had a ghoul living there with me back then at the fall of the iron curtain.
        """
        hide pc

        show janos idle at right
        janos "Sounds more like something you would bring to a rural pig killing."
        hide janos

        return

    label haven_agents_in_the_room_intro:
        centered "And there you were in the living room."

        centered "First comes a blinding flash."

        hide screen dynamic_stats

        scene white
        with fade

        play sound flashbang_low

        centered """{color=#000000}Smoke covers everything, as the trained agents of the second inquisition storm the room, all [story_remaining_si] of them.{/color} 
        """
        return

    label haven_attack_closest:
        call haven_reveal_the_room
        
        show agent idle at left
        centered """There is no time to waste.
        
        You pounce at the closest agent.
        """
        hide agent

        # Roll to attack
        $ roll_pc = Roll(pc_sheet.DEXTERITY, pc_sheet.BRAWL, difficulty=3)
        $ roll_pc.roll()

        if roll_pc.is_success:
            play sound smash_and_grunt
            queue sound death_scream_2
            centered "You've got one of them."
            
            $ story_remaining_si -= 1

            if story_remaining_si >= 1:
                show agent idle at right
                agent "Man. Down, I repeat man down."
                hide agent
            else:
                centered "That was the last of them."
        else:
            show pc idle at center
            centered """Daaamn!
            
            These motherfuckers have got serious training.
            
            You try to pin him to the ground, but he gets the better of you."""
            hide pc

            $ pc_sheet.lose_health(1)
            call change_dynamic_stats("worse")

        return

    label haven_cover:
        call haven_reveal_the_room
        centered """You try to rely on your familiarity with the location, 
        
        remembering where everything is supposed to be as you take cover.
        
        It is still the day so staying awake has its own challanges. {image=dice}"""
        
        # Roll willpower to stay awake
        $ roll_pc = Roll(pc_sheet.willpower, pc_sheet.hunger, difficulty=5)
        $ roll_pc.roll()

        if roll_pc.is_success:
            centered "But nothing can break your will."
        else:
            centered "It's hard to stay alive and standing, let alone jump to the spot you have found."

            $ pc_sheet.lose_willpower(1)
            call change_dynamic_stats("worse")

        # Roll manuevering to find a good sport
        $ roll_pc = Roll(pc_sheet.DEXTERITY + pc_sheet.AWARENESS, pc_sheet.hunger, difficulty=5)
        $ roll_pc.roll()

        centered "You take cover behind the half blown-up table."
        if roll_pc.is_success:
            centered """It's not much, but it will do.
            
            You spot a man approaching."""

            show agent idle at left
            $ story_remaining_si -= 1
            play sound smash_and_grunt

            centered """You quickly grab his leg and tear him to the ground."""

            hide agent
       
        else:
            centered """It's not good for shit.

            You suffer 2 shots to the arm."""

            play sound machine_gun_single

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

        show pc idle at right
        if roll_pc.is_success and story_weapon == "Uzi": # Still using the last roll.
            centered "Noone can dodge 20 bullets per magazine when lunched from the back of their necks"
            $ story_remaining_si -= 3
            
            play sound machine_gun_single
            queue sound death_scream_1
            queue sound machine_gun_single
            queue sound death_scream_2
            queue sound machine_gun_single
            queue sound death_scream_3

            centered "3 agents fall to the ground almost simultanously."

        if roll_pc.is_success and story_weapon == "Knife":
            centered "A kitchen knife is good enough if stand close enough to count the hairs on the backs of their necks."
            $ story_remaining_si -= 2
            play sound knife_slash
            queue sound death_scream_1
            queue sound death_scream_3
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
        play sound gunfight
        
        centered "Quickly dashing around the room you spray them with all the bullets God created and more."
        
        # Roll Shoot
        $ roll_pc = Roll(pc_sheet.DEXTERITY + pc_sheet.FIREARMS, pc_sheet.hunger, difficulty=3)
        $ roll_pc.roll()

        if roll_pc.margin_of_success <= 0:
    
            centered """
            Who are we kidding, you are no trained marksman.
            
            For all your attempts, none of them fall to the ground.

            They, on the other hand, know how to handle a gun.
            """

            $ pc_sheet.lose_health(story_remaining_si)
            call change_dynamic_stats("worse")

        elif roll_pc.margin_of_success == 1:
            $ story_remaining_si -= 1
            
            play sound machine_gun_single
            
            centered "[roll_pc.margin_of_success] agent falls to the ground."
            
            play sound death_scream_2

            $ pc_sheet.lose_health(1)
            call change_dynamic_stats("worse")

        else:
            $ story_remaining_si -= roll_pc.margin_of_success
            
            play sound machine_gun_single
            queue sound death_scream_2
            queue sound machine_gun_single
       
            centered "[roll_pc.margin_of_success] agents fall to the ground almost simultanously."
            play sound death_scream_3
            
        return

    label haven_reveal_the_room:
        scene background_video_haven
        with Dissolve(2.0)

        call show_dynamic_stats

        return
                          
    label haven_outro:
        show pc idle at center
        if not story_remaining_si == 0:
            centered """The smell of blood mixed with new age gunpowder fills everything.

            Your nostrils widen up, you could literally eat up the air when all hell truly breaks out."""
            play sound beast_roar
            queue sound gunfight
            
            hide pc

            show pc idle at right
            pc """
            I cannot truly describe to you what happened next.

            I was in control throughout the whole thing.

            I tore them to pieces.
            """
            hide pc

            centered """In your mind you can still see
            
            the disconnected images of bone, fangs, gunshot wounds, etc...

            One thing is for sure, when the whole thing ended, you don't find anyone alive."""

            $ pc_sheet.get_hungry(2)
            $ pc_sheet.lose_health(story_remaining_si)
            call change_dynamic_stats("worse")
        
        show pc idle at right
        pc "I have to admit..."

        menu:
            "How are you feeling?"

            "Proud":
                pc """I feel fuckin' proud. Not everyone could have done what I did.
                
                Team [pc_sheet.NAME]: 1

                Team bothersome motherfuckers: 0

                Fuck yeah!"""
                hide pc

            "Ashamed":
                pc "I have to admint, this will remain as a stain on my soul forever. Considering everything, still, it was too brutal."
                hide pc

        show janos idle at right
        janos """We have more important questions to address.
        
        Let's continue..."""
        call end_haven

label end_haven:             
    stop music fadeout 1.0
    hide screen dynamic_stats
    scene black
    with fade
    return