init python:
    renpy.music.register_channel("music_nostalgia", "music", True)
    
label hospital:
    # A memmory of the Hospital
    # PLOTPOINTS: We learn about the stolen blood and the PC's relation to Cecila
    scene black 
    with fade 
    
    play music background_music_hospital volume 0.5 loop

    scene backgorund_video_hospital
    with Dissolve(2.0)

    centered "The memory of St. Laszlo's hospital comes back, maybe even more clearly than you would like"

    call show_dynamic_stats

    show pc idle at right
    pc "The hospital was particulary quiet that evening."
    hide pc

    show janos idle at right
    janos "Were you a frequent visitor?"

    centered "He fiddles around his notes."

    centered "Naturally, he does not share his discoveries with you."
    hide janos

    show pc idle at right
    pc "It seems that you already have the answer somewhere there, written down."
    hide pc

    show janos idle at right
    janos "I often find that the subject's verbal account illuminates the salient points of the affair in comparision to which textual evidence quite simply pales."
    hide janos

    show pc idle at right
    pc "illuminates the salient points..."
    
    centered "Janos' imapatient voice interupts you."
    hide pc

    show janos idle at right
    janos """
    Yes. It illuminates.
    
    So, illuminate

    please.

    With what frequency did you visit the hospital?
    """
    hide janos

    menu hospital_visits:
        "Tell the truth":
            jump truth_about_the_hospital

        "Tell a lie {image=dice}":
            jump lie_about_the_hospital


    label truth_about_the_hospital:
        show pc idle at right
        pc "At least once a week."
        hide pc

        show janos idle at right
        janos """
        That is quite frequent.

        Quite frequent, indeed, for someone who has no need of medical attention.

        Unless you carry only the weakest of remnants of the dark father's blood in you,
        """

        $ sire_generation = pc_sheet.GENERATION - 1

        janos """
        But you are only removed [sire_generation] times from him.

        So no danger of that.

        That leaves us with an inquery to the reason behind the frequency of your visits.
        """
        hide janos

        show pc idle at right
        pc "I was visiting someone."
        hide pc

        show janos idle at right
        janos "Who?"
        hide janos
        
    label lie_about_the_hospital:
        $ roll_janos = Roll(janos_sheet.INTELLIGENCE + janos_sheet.MANIPULATION, janos_sheet.hunger, difficulty=0)
        $ roll_janos.roll()
        $ roll_pc = Roll(pc_sheet.WITS + pc_sheet.PERSUASION, pc_sheet.hunger, difficulty=roll_janos.margin_of_success)
        $ roll_pc.roll()

        if roll_pc.margin_of_success > 0:
            jump successful_hospital_lie

        else:
            jump failed_hospital_lie

    label successful_hospital_lie:
        centered "You lay back confidently, knowing that the secret to every good lie is in the details."

        show pc idle at right
        pc """
        The hospital's location and function were not improtant to me.

        I mean, maybe they were.

        I like to visit places where people are in their purest form and hide less from all the bullshit of the world.

        There is a morbid tranquility to them, especially in the form of some of the staff.        
        """
        hide pc

        centered """
        Shit.
        
        It started so well.
        """

        show janos idle at right
        janos "So it was not only the tranquiltiy of hopsitals that drew you in?"
        hide janos

        jump blood_selling_1
           
    label failed_hospital_lie:
        centered "You try to act confidently, but you it's hard to lie to your own sheriff."

        show pc idle at right
        pc """
        I wouldn't say I visited the hospital often.

        I would go there a bit more than the others.
        """

        centered "You feel that the right words escape you."

        centered "Why does he let this drag on."

        centered "Maybe he is buying it."

        pc "You know there is a certain beuty to a place like that."

        centered "Shit. Beuty to a Hungarian hospital?"
        hide pc

        show janos idle at right
        janos "Yes, I see."
        hide janos

        show pc idle at right
        centered "Did he really buy that?!"

        centered "I must press on"
        pc "I know it is not for everybody's taste, but you need somethign to keep you going through the years"
        hide pc

        show janos idle at right
        janos """
        [pc_sheet.AGE] of them, to be exact.

        So in [pc_sheet.AGE] years you have found that it is the ethemeral beauty of underfunded hospitals that,
        
        how did you put it 'keeps you going'
        """
        hide janos

        show pc idle at right
        pc "Kinda."
        hide pc

        show janos idle at right
        janos "I think it disrespectful, when someone lies to my face."
        hide janos

        centered "Burn."
        $ pc_sheet.lose_willpower(1)
        call change_dynamic_stats("worse")

        show janos idle at right
        janos """
        So much effort without success.

        I wonder why.

        Maybe you were visiting someone on a regular basis.

        But who?
        """
        hide janos

        jump blood_selling_1
        
    label blood_selling_1:
        if not pc_sheet.CLAN == "Malkavian":
            show pc idle at right
            pc """
            You caught me.

            I have a little something going on, on the side.

            There are certain kindred who are willing to pay top-money for the right vitae.
            """
            hide pc

        else:
            # Malkavian
            show pc idle at right
            pc """
            Sometimes it was spontanoues, sometimes not,

            you know, I am here and I am there,

            sometimes I am everywhere.
            """
            hide pc

            show janos idle at right
            janos """
            May I ask, the [pc_sheet.ASSUMED_GENDER] to leave poetics in the hands of the experts
            
            and communicate only the facts.
            """
            hide janos

            show pc idle at right
            pc """
            The blood is profitable, and deep,
            
            Sweet dreams don't come to us cheap.
            """
            hide pc

            show janos idle at right
            janos "Facts. I mean, bloody facts."
            hide janos

            show pc idle at right
            pc "I just did."
            hide pc

            show janos idle at right
            janos "Are you trying to tell me that you were selling blood?"
            hide janos

            show pc idle at right
            pc "..."
            hide pc

            show janos idle at right
            janos "We will proceed with this assumption."
            hide janos

        # Blood selling convo continues for all clans

        show janos idle at right
        janos """
        And the hospital is where you got your wares.

        So, may I assume from the frequency of your visits, that business was going splendidly?
        """
        hide janos

        show pc idle at right
        pc "You, very well may."
        hide pc
        
        jump blood_selling_2

    label blood_selling_2:
        show janos idle at right
        janos "You must have had a contact on the inside."
        hide janos

        show pc idle at right
        pc "Yes."
        hide pc

        show janos idle at right
        janos "Who?"
        hide janos
            
        show pc idle at right
        pc "It was Cecilia."
        hide pc

        jump cecilia_1
    
    label cecilia_1:
        
        play music_nostalgia nostalgia volume 0.1 loop

        centered """
        Even now, under these circumstances you remember Cecilia fondly.
    
        Ther was always something elating about her presence that could shake up you up,

        even having been dead for over a century.

        You would just catch her walking on the corridors of the hospital, tending to someone's needs.
        """

        show cecilia idle at right
        cecilia "How is my dark [pc_sheet.ASSUMED_GENDER]?"
        hide cecilia

        centered "I never really liked that she adressed me so. But I couldn't bring myself to chide her."

        show pc idle at right
        pc "Not very well. I cannot stay long"
        hide pc

        show cecilia idle at right
        cecilia "I know better, than to ask why."
        hide cecilia

        centered "So much compassion."

        menu:
            "Straight to business":
                show pc idle at right
                pc """
                You are an angel, but I have to run.

                How much do you have for me tonight?
                """
                hide pc

                show cecilia idle at right
                cecilia """
                Just a few bags
                
                But I'm sure, with all the blood you're taking to those in need this will be enough now.
                """
                hide cecilia
                    
            "Say a few kind words":
                show pc idle at right
                pc "You are an angel, How do you keep such a happy face among these dire circumstances?"
                hide pc

                show cecilia idle at right
                cecilia """
                I just try to look where do they need my help, and go there.
                
                It brings its own reward.

                But I'm sure, darling you know this. With all the blood you're taking to those in need.
                """
                hide cecilia

                show pc idle at right
                pc """
                You are an angel, but I have to run.

                How much do you have for me tonight?
                """
                hide pc

                show cecilia idle at right
                cecilia "Just a few bags"
                hide cecilia

        show pc idle at right
        pc "The usual place?"
        hide pc

        show cecilia idle at right
        cecilia """
        Yes.
        
        When will I see you again?

        Properly, this time?
        """
        hide cecilia

        show pc idle at right
        pc "I honestly don't know."
        hide pc

        jump blood_selling_3

    label blood_selling_3:
        
        stop music_nostalgia fadeout 1.0

        show janos idle at right
        janos "Was your relationship with Cecilia purely about business?"
        hide janos

        menu:
            "Was your relationship with Cecilia purely about business?"

            "No":
                show pc idle at right
                pc """
                She liked me very much, no question about it.

                But can you blame her?

                In all honesty though, and what should I be in front of my sheriiff if not completely honest,

                There is a kind of sentiment, that only the living, can inspire in us.

                That lived in me - Ironic as that may sound.
                """
                hide pc

            "Yes":

                show pc idle at right
                pc """
                She liked me very much, no question about it.

                But can you blame her?

                One look at me and you can fall in love.

                I am sure you feel the same way.

                But honestly, for me, it has always been about the blood.
                """
                hide pc
                
        show janos idle at right
        janos "I believe I have some understanding for that."
        hide janos

        show pc idle at right
        pc "Sure, you look like that kind of guy."
        hide pc

        show janos idle at right
        janos """
        ...
        
        Additionally, may one ask, did you meet anyone besides her at the hospital?
        """
        hide janos

        menu:
            "Tell the truth":
                show pc idle at right
                pc "I also saw Emilio for a brief moment. He looked lost deep in thoughts, so I decided not to bother him."
                hide pc

                $ story_mention_emilio = True

            "Tell a lie {image=dice}":
                $ roll_janos = Roll(janos_sheet.INTELLIGENCE + janos_sheet.MANIPULATION, janos_sheet.hunger, difficulty=0)
                $ roll_janos.roll()
                $ roll_pc = Roll(pc_sheet.WITS + pc_sheet.PERSUASION, pc_sheet.hunger, difficulty=roll_janos.margin_of_success)
                $ roll_pc.roll()

                if roll_pc.is_success:
                    $ story_mention_emilio = False
                    centered "The words come very easily and smoothly for you."

                    show pc idle at right
                    pc "Anyone? Try everyone! It is a hospital for God's sake, full of people. If you really tried hard, you could even find the pope there."
                    hide pc

                    centered """Rage. It never fails.
                    
                    You lean back with the pleasurable smile of achievement.

                    You're happy you could keep Emilio out of this.
                    """ 

                else:
                    centered """It is begining to be difficult to keep track of what's what and all the lies.
                    
                    You find yourself confused.
                    """

                    show pc idle at right
                    pc "I meet a few people."
                    hide pc

                    show janos idle at right
                    janos "Who, precisely?"
                    hide janos

                    centered """
                    You try to hide the only important name in a never ending stream of lies
                    
                    but he cathes is.
                    """

                    show janos idle at right
                    janos "Emilio."
                    hide janos

                    $ story_mention_emilio = True

                    centered "No use to hide it anymore."

                    show pc idle at right
                    pc "Yes."
                    hide pc

        show janos idle at right
        janos "Noted."
        hide janos
                
    stop music fadeout 1.0
    hide screen dynamic_stats
    scene black
    with fade
    return