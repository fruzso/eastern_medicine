label hospital:
    # A memmory of the Hospital
    # PLOTPOINTS: We learn about the stolen blood and the PC's relation to Cecila

    scene backgorund_video_hospital
    with Dissolve(2.0)

    "/The memory of St. Margit's hospital comes back, maybe even more clearly than you would like/"

    with Pause(1.0)

    jump show_dynamic_stats

    show pc idle at right
    pc "The hospital was particulary quiet that evening."
    hide pc

    show janos idle at left
    janos "Were you a frequent visitor?"

    "/He fiddles around his notes./"

    "/Naturally, he does not share his discoveries with you./"
    hide janos

    show pc idle at right
    pc "It seems that you already have the answer somewhere there, written down."
    hide pc

    show janos idle at left
    janos "I often find that the subject's verbal account illuminates the salient points of the affair in comparision to which textual evidence quite simply pales."
    hide janos

    show pc idle at right
    pc "illuminates the salient points..."
    
    "/Janos' imapatient voice interupts you./"
    hide pc

    show janos idle at left
    janos """
    Yes. It illuminates.
    
    So, illuminate

    please.

    With what frequency did you visit the hospital?
    """
    hide janos

    menu hospital_visits:
        "Choose your answer"
        "Tell the truth":
            show pc idle at right
            pc "At least once a week"
            hide pc

            show janos idle at left
            janos """
            That is quite frequent.

            Quite frequent, indeed, for someone who has no need of medical attention.

            Unless you carry the weakest of remnants of the dark father's blood in you,"""

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

            show janos idle at left
            janos "Who?"
            hide janos

        "Tell a lie":
            $ roll_janos = Roll(janos_sheet.INTELLIGENCE + janos_sheet.MANIPULATION, janos_sheet.hunger, difficulty=0)
            $ roll_janos.roll()
            $ roll_pc = Roll(pc_sheet.WITS + pc_sheet.PERSUASION, pc_sheet.hunger, difficulty=roll_janos.margin_of_success)
            $ roll_pc.roll()

            if roll_pc.margin_of_success > 0:
                $ story_selling_blood = True

                "/You lay back confidently, knowing that the secret to every good lie is in the details./"

                show pc idle at right
                if pc_sheet.CLAN == "Malkavian":
                    pc """
                    Sometimes it was spontanoues, sometimes not,

                    you know, I am here and I am there,

                    sometimes I am everywhere.
                    """
                    hide pc

                    show janos idle at left
                    janos "May I ask, the [pc_sheet.ASSUMED_GENDER] to leave poetics in the hands of the experts and communicate only the facts."
                    hide janos

                    show pc idle at right
                    pc """
                    The blood is profitable, and deep,
                    
                    Sweet dreams don't come to us cheap.
                    """

                else:
                    pc """
                    You caught me.

                    I have a little something going on, on the side.

                    There are certain kindred who are willing to pay top-money for the right vitae.
                    """
                hide pc

                show janos idle at left
                janos """
                And the hospital is where you got your wares.

                So, may I assume from the frequency of your visits, that business was going splendidly?
                """
                hide janos

                show pc idle at right
                pc "You, very well may."
                hide pc

                show janos idle at left
                janos "You must have had a contact on the inside."
                hide janos

                show pc idle at right
                pc "Yes."
                hide pc

                show janos idle at left
                janos "Who?"
                hide Janos

            else:
                "/You try to act confidently, but you it's hard to lie to your own sheriff./"
                show pc idle at right
                pc """
                I wouldn't say I visited the hospital often.

                I would go there a bit more than the others.
                """

                "/You feel that the right words escape you./"

                "/Why does he let this drag on./"

                "/Maybe he is buying it./"

                pc "You know there is a certain beuty to a place like that."

                "/Shit. Beuty to a Hungarian hospital?/"
                hide pc

                show janos idle at left
                janos "Yes, I see."
                hide janos

                show pc idle at right
                "/Did he really buy that?!/"

                "/I must press on/"
                pc "I know it is not for everybody's taste, but you need somethign to keep you going through the years"
                hide pc

                show janos idle at left
                janos """[pc_sheet.AGE] of them, to be exact.

                So in [pc_sheet.AGE] years you have found that it is the ethemeral beauty of underfunded hospitals that, how did you put it 'keeps you going'
                """
                hide janos

                show pc idle at right
                pc "Kinda."
                hide pc

                show janos idle at left
                janos "I think it disrespectful, when someone lies to my face."
                hide janos

                "/Burn. You lose 1 point of willpower./"
                $ pc_sheet.lose_willpower(1)
                call change_dynamic_stats
                if pc_sheet.WILLPOWER = 0:
                    call lost_willpower

                show janos idle at left
                janos """
                So much effort without success.

                I wonder why.

                Maybe you were visiting someone on a regular basis.

                But who?
                """
                hide janos

    show pc idle at right
    pc "It was Cecilia."
    hide pc

    hide screen dynamic_stats
    scene black
    with fade
    return