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
    janos """
    Me'thought the question was fairly obvious.

    Considering all the facts. I should have risen self evidently,

    for the trained eye of the observer.
    """
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
                    show pc at right
                    pc "No fucking idea, asshole!"
                    hide pc

                    $ janos_strikes += 1

                    show janos idle at right
                    janos "That is strike number [janos_strikes]."
                    hide janos

                "Stay cordial":
                    show pc at right
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

            $ janos_strikes += 1

            show janos idle at right
            janos "That is strike number [janos_strikes]."
            hide janos

        "They must have followed me":
            show pc idle at right
            pc "I am no trained observered, but since I hadn't told them they must have followed me.
            
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
                    pc "It must have been Elemér."
                    hide pc

                    show janos idle at right
                    janos "Hmm... Elemér, interesting accusation. I shall look into that later."
                    hide janos

                    cnetered "Did he buy it?"

        show janos idle at right
        janos """
        While it is tempting to think that It was your own ignorance and carelessness that put you in harms way,

        unfortunately, - or fortunately, I cannot quite tell at this point -

        my sources reveal otherwise.
        """
        hide janos

        show pc idle at right
        pc "Insults aside, you have hooked. What do your sources reveal?"
        hide pc

        show janos idle at right
        janos "The second inquisition has started to introduce radioactive isotopes to marked poritons of blood,
        
        distributed accross town at medical facilities of suspected activities.
        
        Ultimate with the quite decernable goal of locating the motions and geolcoations of said isotopes.
        """
        hide janos

        show pc idle at right
        pc "Shiiiit."
        hide pc

        show janos idle at right
        janos """
        The elloquence of your generation amases me.
        
        But essentially, yes. They are back on.

        So it happens that somebody has been aiding their distribution endevour.
        """
        hide janos

        if story_selling_blood:
            centered "The recognition comes somewhat slowly."

            centered "You lied to Janos that you have been selling blood to the kindred community from the hospital."

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
        janos "I any case. Where did you go once yoru haven has been breached?"
        hide janos

        show pc idle at right
        pc "I needed help"
        hide pc    

    hide screen dynamic_stats
    scene black
    with fade
    return