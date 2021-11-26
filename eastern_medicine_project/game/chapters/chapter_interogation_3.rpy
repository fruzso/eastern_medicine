label interogation_3:
    # The main scene of the game, where the player returns many times
    # PLOTPOINTS: puttign together the pieces from teh puzzle

    scene black 
    with fade 
    
    play music background_music_interrogation volume 0.5 loop

    scene background_video_interogation
    with Dissolve(3.0)

    call show_dynamic_stats

    show janos idle at right
    janos "Did you wonder?"
    hide janos

    show pc idle at right
    pc "What?"
    hide pc

    show janos idle at right
    janos """Me'thought the question was fairly obvious.

    Considering all the facts. It should have risen self evidently,

    for the trained eye of the observer."""
    hide janos

    show pc idle at right
    pc "Let's jsut pretend that I don't have the 'trained eye of the observer'."
    hide pc

    show janos idle at right
    janos "Gladly."
    hide janos

    show pc idle at right
    pc "..."
    hide pc

    show janos idle at right
    janos "How did the agents of the second inquisition learn of your haven's location?"
    hide janos

    menu how_did_they_find_the_pc:
        "How did they find you?"

        "I have no idea":
            show pc idle at right
            pc """
            We might not be best friends, but I don't wanna fuck with you,
            
            so I'm gonna level with you:
            """
            hide pc

            menu:
                "Choose your tone"
                "Insult him":
                    show pc idle at right
                    pc "No fucking idea, asshole!"
                    hide pc
                    
                    call increase_janos_strikes
                    show janos idle at right
                    janos "That is strike number [janos_strikes]."
                    hide janos

                "Stay cordial":
                    show pc idle at right
                    pc "Sincerelly, I don't know."
                    hide pc
                
        "That is your job to figure out":
            show pc idle at right
            pc """
            That's asking me to do your job for you.

            Figure it out.

            How the fuck should I know?
            """
            hide pc

            call increase_janos_strikes
            show janos idle at right
            janos "That is strike number [janos_strikes]."
            hide janos

        "They must have followed me":
            show pc idle at right
            pc """I am no trained observer, but since I hadn't told them they must have followed me.
            
            Or, and this is the truly terrifying possiblity, someone lead them there.
            
            It had to have been someone who knew, where my haven was.
            """
            
            centered "For example and official like Janos."

            centered "Shit."

            centered "I cannot say that."

            menu trouble:
                "What next?"
                "Stop talking":
                    centered "You stop talking."
                "Cast the shadow of doubt on someone else":
                    pc "It must have been Elemér." #TODO: STORY Zsarol with cecilia
                    hide pc

                    show janos idle at right
                    janos "Hmm... Elemér, interesting accusation. I shall look into that later."
                    hide janos

                    centered "Did he buy it?"

    show janos idle at right
    janos """
    While it is tempting to think that It was your own ignorance and carelessness that put you in harms way,

    unfortunately, - or fortunately, I cannot quite tell at this point -

    my sources reveal otherwise.
    """
    hide janos

    show pc idle at right
    pc "Insults aside, you have me hooked. What do your sources reveal?"
    hide pc

    show janos idle at right
    janos """
    The second inquisition has started to introduce radioactive isotopes to marked poritons of blood,
    
    distributed accross town at medical facilities of suspected activities.
    
    Ultimately, with the quite decernable goal of locating the motions and geolcoations of said isotopes

    and if it wasn't obvious those dear kindred who have consumed said isotopes."""
    hide janos

    show pc idle at right
    pc "Shiiiit."
    hide pc

    show janos idle at right
    janos """
    The elloquence of your generation amases me.
    
    But essentially, yes. They are back on.

    So it happens that somebody has been aiding their distribution endevour."""
    hide janos


    if story_pc_guilty:
        centered """He knows quite a lot.

        Let's see:

        He knows I am selling the blood,

        he knows I have a human connection to the hospital.

        This ain't gonna be pretty.
        """

    else:
        centered """The recognition comes somewhat slowly.

        Shit.

        You just told him a few minutes ago that you're selling blood to the kindred community from a hospital.

        This does not look good.

        By the way is that shit really tainted?
        """

    show janos idle at right
    janos """
    The crime itself is punishible beyond a shadow of a doubt.
    
    The only factor to assertain is

    whether it was commited inadvertantly or out of malice,

    you see.
    """
    hide janos

    show pc idle at right
    pc "I am not sure."
    hide pc

    show janos idle at right
    janos "I any case. Where did you go once your haven has been breached?"
    hide janos

    show pc idle at right
    pc """It was still pretty early.

    And daytime.

    First I navigated my building, hiding in corridors and stairstops, carefully avoiding the light."""

    $ pc_sheet.lose_health(1)
    call change_dynamic_stats("worse")

    pc """
    As much as I could.
    
    There have been a few accidents.
    
    Neither has it been easy to stay - should I say alive? awake?
    """

    $ pc_sheet.lose_willpower(1)
    call change_dynamic_stats("worse")

    pc """
    I made my way into garage of teh building, and hid under a Volkswagen.
    """
    hide pc    

    show janos idle at right
    janos "Must have been quite a journey. Where did you go next?"
    hide janos

    hide screen dynamic_stats
    scene black
    with fade
    return