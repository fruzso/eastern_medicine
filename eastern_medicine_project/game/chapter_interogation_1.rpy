label interogation_1:
    # The main scene of the game, where the player returns many times
    # PLOTPOINTS: 
    
    scene black 
    with fade 
    centered "You follow the footsteps of Janos through what must be a dark corridor."
    
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

    centered """
    Your eyes easily find the only chair singled out in the middle of the damp room, 
    but you hesitate. The nosferatu's pale figure draws away your attention.
    """

    menu emotional_reading:
        "Study his emotions":
            centered "In a split second you catalogue his features, mannerisms and faint flickers of emotion in his eyes."

            $ roll = Roll(pc_sheet.WITS + pc_sheet.INSIGHT, pc_sheet.hunger, difficulty=3)
            $ roll.roll()

            if roll.margin_of_success > -1:
                centered "He is an open book to you."

                centered "He may be playing the tough guy, but you sense that something else is bothering him inside"
            else:
                centered """
                He is hard to read. However hard you try to figure out 
                what is going on behind his deformed features, it is to no avail.
                """

        "Who gives a fuck":
            jump seating_choice

    menu seating_choice:

        "Sit down":
            $ pc_seated = True

            show pc idle at right
            pc "Well, if this is the best the house can offer, I don't mind if I do."

            centered "You sit down and take your time to adjust in the chair"

            pc "Never mind the squeks and the wait."
            hide pc

            show janos idle at right
            janos "Are you sitting comfortably?"
            hide janos

            show pc idle at right
            pc "You could say that."
            hide pc

        "Remain standing":
            $ pc_seated = False

            show pc idle
            pc "Thanks, but no thanks. I prefere to stand."

            centered "You remain standing."
            hide pc
            
            show janos idle at right
            janos "Suit yourself. But we are going to be here for some time."
    
    if not pc_seated:
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
    -When- would reveal a bit more, perhaps.
    
    Yet again, you are not here to ask questions.

    Not the smart ones, anyway.
    """
    hide janos

    show pc idle at right
    pc "Have we started on the tourture yet?"
    hide pc

    show janos idle at right
    janos "You would know if we did, I assure you. In any case, there is a point to your persistence, I confess."

    if pc_sheet.CLAN == "Malkavian":
        hide janos

        show pc idle at right
        pc """
        Dead ladies and gentlemen of the jury,

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
        pc """
        Followed by what?
        
        Kindred?

        People?

        Or maybe time?

        My past always follows me,

        sometimes my future too.
        """
        hide pc

        show janos idle at right
        janos """
        Please refrain from toying with me.

        Followed by the kine. Specifically covert operatives.
        """
        hide janos

    show pc idle at right
    pc "Rcently?"
    hide pc

    show janos idle at right
    janos "Shall we say in the last 3 weeks."
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

            Let us get back on point.
            """
            hide janos

        # USE: Dominate 1 - Compell
        "Compell him to talk plainly (DOMINATE)" if pc_sheet.DOMINATE > 0:
            centered "You try to catch his gaze"

            # Simple Roll
            $ roll_pc = Roll(pc_sheet.DEXTERITY + pc_sheet.AWARENESS, pc_sheet.hunger, difficulty=5)
            $ roll_pc.roll()

            if roll_pc.is_success:
                centered  "You meet Janos' eyes for a brief moment, but enough to utter the words:"

                # Contest Roll
                $ roll_janos = Roll(janos_sheet.WITS + janos_sheet.RESOLVE, janos_sheet.hunger, difficulty=0)
                $ roll_janos.roll()
                $ roll_pc = Roll(pc_sheet.CHARISMA + pc_sheet.DOMINATE, pc_sheet.hunger, difficulty=roll_janos.margin_of_success)
                $ roll_pc.roll()
                
                if roll_pc.is_success:
                    show pc idle at right
                    pc "Talk to me plainly!"
                    hide pc

                    show janos idle at right
                    janos """
                    Such a simple thing to do.
                    
                    One sentence, I believe, should suffice.

                    I advise you do not waste more energy on such attempts.

                    I might not be so forgiving, next time.
                    """
                    hide janos

                else:
                    centered "You feel your words missing their aim mid-air."

                    centered "Perhaps its noise comming in, or simply you lack the charisma to stand up to the sheriff at the moment" #TODO:AUDIO que in nosie comming in

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
        "Present your fangs to mmake a point" if pc_sheet.PRESENCE >= 3:
            centered "You open wide and put on an intimigating display of your fangs, while focusing all your supernatural effect on Janos."

            $ pc_sheet.rouse_check() # TODO: HUNGERCHECK

            # Contest Roll
            $ roll_janos = Roll(janos_sheet.COMPOSURE + janos_sheet.RESOLVE, janos_sheet.hunger, difficulty=0)
            $ roll_janos.roll()
            $ roll_pc = Roll(pc_sheet.CHARISMA + pc_sheet.PRESENCE, pc_sheet.hunger, difficulty=roll_janos.margin_of_success)
            $ roll_pc.roll()
            
            if roll_pc.is_success:
                centered "Your display of vampiric prowess instills supernatural fear in Janos' eyes."

                centered "It's such a powerful effect as you are used to, but it will do."

                show janos idle at right
                janos """
                Maybe there is more to you than what meets the eye.

                I am big enough to admit, that we might have started this little tete-at-tete on the wrong foot.

                Therefore let us assume a tone more fit for civilized creatures.
                """
                hide janos

                centered "A simple victory, but it means a lot, against the sheriff."
                $ pc_sheet.gain_willpower(1)
                call change_dynamic_stats

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
                call change_dynamic_stats

    show janos idle at right
    janos "Where were you on the 20th of August?"
    hide janos

    menu august_20:
        "Tell a lie":
            $ roll_janos = Roll(janos_sheet.INTELLIGENCE + janos_sheet.MANIPULATION, janos_sheet.hunger, difficulty=0)
            $ roll_janos.roll()
            $ roll_pc = Roll(pc_sheet.WITS + pc_sheet.PERSUASION, pc_sheet.hunger, difficulty=roll_janos.margin_of_success)
            $ roll_pc.roll()

            if roll_pc.margin_of_success > 0:
                # Succesful lie
                #TODO:AUDIO que in fireworks

                show pc idle at right
                pc """
                It was a particulary bright evening, I remember it well.
                
                I was atop a corporate tower - forgive me, I forget which money-hungry conglomerate was it this time.
                
                But I tell you something, you cannot beat the view these fat cats afford their peons.
                
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
                "You have a story prepared just for this question."

                "It's time to tell it."
                
                #TODO:AUDIO que in fireworks

                show pc idle at right
                pc """
                It was a particulary bright evening, I remember it well. As if it was yesturday.
                
                I was atop a corporate tower - forgive me, I forget which money-hungry conglomerate was it this time.
                
                But I tell you something, you cannot beat the view these fat cats afford their peons.
                
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
                call change_dynamic_stats

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