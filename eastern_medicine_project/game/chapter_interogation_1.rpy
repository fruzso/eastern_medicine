label interogation_1:
    # The main scene of the game, where the player returns many times
    # PLOTPOINTS: 
    
    scene black 
    with fade 
    centered "You follow Janos' footsteps through what must be a dark corridor under a public square."
    
    play sound "sounds/interrogation_footsteps_and_door.mp3"
    pause(10.0)
    
    scene background_video_interogation
    with Dissolve(3.0)
    pause(5.0)

    play music background_music_interrogation volume 0.5 loop

    call show_dynamic_stats

    show janos idle at right
    janos "Take a seat!"
    hide janos

    centered "You consider the room, knowing inside that you are:"

    menu pc_guilty:
        "You are"
        "Guilty":
            $ story_pc_guilty = True
            centered """
            A few rationalizations of your crime run through your head.
            In the end all what matters is if you can get away with it.
            And why couldn't you?
            It was the right thing to do anyway.
            """
            
        "Innocent":
            $ story_pc_guilty = False
            centered "You take pride and comfort in the knowledge that you are innocent."

    show janos idle at right
    janos "Did you say something?"
    hide janos

    show pc idle at right
    pc "Nothing."
    hide pc  
        
    centered """
    Your eyes easily find the only chair singled out in the middle of the damp room, 
    but you hesitate. The nosferatu's pale figure draws in your attention.
    """

    menu emotional_reading:
        "Study his emotions {image=dice}":
            centered """
            In a split second you catalogue his features, 
            mannerisms and faint flickers of emotion in his eyes.
            """

            $ roll_pc = Roll(pc_sheet.WITS + pc_sheet.INSIGHT, pc_sheet.hunger, difficulty=3)
            $ roll_pc.roll()

            if roll.margin_of_success > -1:
                centered "He is an open book to you."

                centered """
                He may be playing the tough guy, but you sense that something else is bothering him inside,
                probably you are not his biggest worry tonight.
                """
            else:
                centered """
                He is difficult to read. However hard you try to figure out 
                what is going on behind his deformed features, it is to no avail.
                """

        "Who gives a fuck":
            jump seating_choice

    menu seating_choice:

        "Sit down":
            $ story_seated = True

            show pc idle at right
            pc "Well, if this is the best the house can offer, I don't mind if I do."

            centered """
            You sit down and take your time to adjust in the chair.
            Never mind the squeks.
            
            Janos can wait a little.
            """
            hide pc

            show janos idle at right
            janos "Are you sitting comfortably?"
            hide janos

            menu:
                "Comfortably":
                    show pc idle at right
                    pc "Comfortably enough."
                    hide pc
                "Uncomfortably":
                    show pc idle at right
                    pc "uncomfortably enough to want toget over this"
                    hide pc

        "Remain standing":
            $ story_seated = False

            show pc idle
            pc "Thanks, but no thanks. I prefere to stand."

            centered "You remain standing."
            hide pc
            
            show janos idle at right
            janos "Suit yourself. But we are going to be here for some time."
            hide janos
    
    show janos idle at right
    janos "Let's begin. Shall we?!"
    hide janos

    show pc idle at right
    pc "By all means. We don't wanna' be here all night, do we?"
    hide pc

    show janos idle at right
    janos "The young are always so hasty, and trouble follows posthaste"
    hide janos

    show pc idle at right
    pc "Where the fuck did you learn to speak?"
    hide pc

    show janos idle at right
    janos """
    {i}When{/i} would reveal a bit more, perhaps.
    
    Yet again, you are not here to ask questions.

    Not the smart ones, anyway.
    """
    hide janos

    show pc idle at right
    pc "Have we started on the tourture yet?"
    hide pc

    show janos idle at right
    janos "You would know if we did, I assure you. In any case, there is a point to your persistence, I confess."
    hide janos

    if pc_sheet.CLAN == "Malkavian":
        show pc idle at right
        pc """
        {i}Dead{/i} ladies and gentlemen of the jury,

        the prosecution rests.

        Job fuckin' well done.
        """
        hide pc

        show janos idle at right
        janos "Are you finished?"
        hide janos

        show pc idle at right
        pc "Eternally."
        hide pc

        show janos idle at right
        janos "That will be enough."
        hide janos

        show pc idle at right
        pc "..."
        hide pc

        show janos idle at right   

    show janos idle at right
    janos "Have you been followed?"
    hide janos

    if pc_sheet.CLAN == "Malkavian":
        show pc idle at right
        pc "Followed by what?"

        menu:
            "Kindred?":
                pc """
                Kindred?
                
                You?
                """
                hide pc
            "People?":
                pc "People? The kine?"
                hide pc
            "Or maybe time?":
                pc """
                Or maybe time?
                
                My past always follows me,

                sometimes my future too.
                """
                hide pc

    show janos idle at right
    janos """
    Please refrain from toying with me.

    Followed by the kine. Specifically baldes in the dark.
    """
    hide janos

    show pc idle at right
    pc "{i}blades in the dark?"
    hide pc

    show janos idle at right
    janos "Covert operatives of various government organizations jumbled together."
    hide janos

    show pc idle at right
    pc "Recently?"
    hide pc

    show janos idle at right
    janos "Shall we say in the last 3 days."
    hide janos

    show pc idle at right
    pc "Not that I know of."
    hide pc

    show janos idle at right
    janos """
    What the fuck do you know then?!

    If such a trifle of cognitive effort mars on the verge of your intellect

    till and plough and leave the nob'ler art of sacrefice to the worthy and the leaned.
    """
    hide janos

    menu irritated:
        "How do you react?"
        "Do nothing":
            show pc idle at right
            pc "..."
            hide pc

        "Ask for a dictionary":
            show pc idle at right
            pc """
            Could you be a lamb, and pass me a dictionary.
            
            I'm sure you carry one at all times.
            """
            hide pc

            show janos idle at right
            janos """
            Not that I know of.
            
            Yet, in a way you are right.

            Education is wasted on you.

            To the point.
            """
            hide janos

        # USE: Dominate 1 - Compell
        "Compell him to talk plainly {image=dice}" if pc_sheet.DOMINATE > 0:
            centered "You try to catch his gaze"

            # Simple Roll
            $ roll_pc = Roll(pc_sheet.DEXTERITY + pc_sheet.AWARENESS, pc_sheet.hunger, difficulty=5)
            $ roll_pc.roll()

            if roll_pc.is_success:
                centered  "You meet Janos' eyes for a brief moment, but it's enough to utter the words:"

                # Contest Roll
                $ roll_janos = Roll(janos_sheet.WITS + janos_sheet.RESOLVE, janos_sheet.hunger, difficulty=0)
                $ roll_janos.roll()
                $ roll_pc = Roll(pc_sheet.CHARISMA + pc_sheet.DOMINATE, pc_sheet.hunger, difficulty=roll_janos.margin_of_success)
                $ roll_pc.roll()
                
                if roll_pc.is_success:
                    $ janos_strikes =+1

                    menu:
                        "Talk to me plainly":
                            show pc idle at right
                            pc "Talk to me plainly!"
                            hide pc

                            show janos idle at right
                            janos """
                            Such a simple thing to do.
                            
                            One sentence, I believe, should suffice.

                            I advise you do not waste more energy on such attempts.

                            I might not be so forgiving, next time. Strike number [janos_strikes]
                            """
                            hide janos

                        "Silence":
                            show pc idle at right
                            pc "Silence"
                            hide pc 

                            centered "Janos immediately stops talking, whilest staring deeply in your eyes."

                            show janos idle

                            centered """
                            Yet slowly you grow uneasy, as his unyielding eyes are fixed on you.
                            
                            You begin to worry about the many repurcussions your actions might have.
                            
                            And finally you find an apologetic tone.
                            """                         

                            show pc idle at right
                            pc "Please, forgive me. Let's continue our talks."
                            hide pc

                            show janos idle at right
                            janos """
                            You caught me off-guard. A better creature might even congratulate you on it
                            
                            and only arrange for your final destruction later.
                            
                            But not I.
                            
                            I'll simply say:
                                
                            This is strike [].
                            """
                            hide janos
                else:
                    play sound "sounds/outside_alarm.mp3" fadein 1.0
                    centered "You feel your words missing their aim mid-air."

                    centered "Perhaps its noise comming in, or simply you lack the charisma to stand up to the sheriff at the moment"

                    show pc idle at right
                    pc "Talk to me plainly!"
                    hide pc

                    $ janos_strikes += 1

                    show janos idle at right
                    janos """
                    That's quite a lot of hubris comming from someone of your age.

                    That's strike [janos_strikes].

                    Let's continue
                    """
                    hide janos  

                    centered "You feel a world of shame creaping in your mind."
            else:
                centered "This is not the Nosferatu's first rodeo."

                centered "He moves his eyes quickly just enough to make any further attempts impossible."

        # USE: Prsence 3 - Dread Gaze
        "Present your fangs to mmake a point {image=dice}" if pc_sheet.PRESENCE >= 3:
            centered """
            You open wide and put on an intimigating display of your fangs,
            while focusing all your supernatural effect on Janos.
            """

            #Rouse check
            if not pc_sheet.rouse_check():
                call change_dynamic_stats("worse") 

            # Contest Roll
            $ roll_janos = Roll(janos_sheet.COMPOSURE + janos_sheet.RESOLVE, janos_sheet.hunger, difficulty=0)
            $ roll_janos.roll()
            $ roll_pc = Roll(pc_sheet.CHARISMA + pc_sheet.PRESENCE, pc_sheet.hunger, difficulty=roll_janos.margin_of_success)
            $ roll_pc.roll()
            
            if roll_pc.is_success:
                centered "Your display of vampiric prowess instills supernatural fear in Janos' eyes."

                centered "It's not such a powerful effect as you are used to, but it'll do."

                show janos idle at right
                janos """
                Maybe there is more to you than what meets the eye.

                I am big enough to admit, that we might have started this little tete-at-tete on the wrong foot.

                Let us assume a tone more fit for civilized creatures.
                """
                hide janos

                centered "A simple victory, but it means a lot, against the sheriff."
                $ pc_sheet.gain_willpower(1)  
                call change_dynamic_stats("better")

            else:
                centered "Your display of vampiric prowess does not move its target."

                show janos idle at right
                janos """
                Please.

                There is no need for such hostility.

                And I am only going to say this once. Put those away.

                Let us assume a tone more fit for civilized creatures.
                """
                hide janos

                centered  "You put your fangs away in shame."
                $ pc_sheet.lose_willpower(1)
                call change_dynamic_stats("worse")

    show janos idle at right
    janos "Where were you on the 20th of August?"
    hide janos

    menu august_20:
        "Tell a lie {image=dice}":
            $ roll_janos = Roll(janos_sheet.INTELLIGENCE + janos_sheet.MANIPULATION, janos_sheet.hunger, difficulty=0)
            $ roll_janos.roll()
            $ roll_pc = Roll(pc_sheet.WITS + pc_sheet.PERSUASION, pc_sheet.hunger, difficulty=roll_janos.margin_of_success)
            $ roll_pc.roll()

            if roll_pc.margin_of_success > 0:
                # Succesful lie
                play sound "sounds/fireworks.mp3" fadein 1.0

                show pc idle at right
                pc """
                It was a particulary bright evening, I remember it well.
                
                I was atop a corporate tower - forgive me, I forget which money-hungry conglomerate was it this time.
                
                But I tell you something, you cannot beat the view these fat cats afford their underlings.
                
                There I was, taking in the night sky, and the sparkling dimonds on it.
                """            
                hide pc

                show janos idle at right
                janos "Knowing your kind, I am surprised that you do not put in a word for a national holiday every day."
                hide janos

                show pc idle at right            
                pc "What a dismal idea. Nothing could devalue the experience anymore."
                hide pc

            else:
                # Unsuccesful lie
                centered "You have a story prepared just for this question."

                centered "It's time to tell it."
                
                play sound "sounds/fireworks.mp3" fadein 1.0
                
                show pc idle at right
                pc """
                It was a particulary bright evening, I remember it well. As if it was yesturday.
                
                I was atop a corporate tower - forgive me, I forget which money-hungry conglomerate was it this time.
                
                But I tell you something, you cannot beat the view these fat cats afford their underlings.
                
                There I was, taking in the night sky, and the sparkling dimonds on it.
                """            
                hide pc

                show janos idle at right
                janos "And that's where you met Cecilia?"
                hide janos

                centered "This is a tough one."

                centered "But why not?"

                show pc idle at right
                pc "Yes."
                hide pc

                show janos idle at right
                janos "Curious. What would an underpaid nurse do atop a Fortune 500 company's private party?"
                hide Janos

                centered "Shit."
                $ pc_sheet.lose_willpower(1)
                call change_dynamic_stats("worse")

                show pc idle at right
                pc "I thought she was a doctor."
                hide pc


        "Tell the truth":

            show pc idle at right
            pc "I was in the hospital."
            hide pc

            show janos idle at right
            janos "The hospital?"
            hide janos
        
            show pc idle at right
            pc "I didn't go there to see the doctor."
            hide pc
            
            stop music fadeout 1.0
            hide screen dynamic_stats
            scene black
            with fade
            return