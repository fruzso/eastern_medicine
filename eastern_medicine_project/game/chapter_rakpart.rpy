label  rakpart:
    # Start scenne
    # Janos enters and ponders the crimes of the PC

    play music background_music_rakpart volume 0.5 loop

    pause(2.0)

    scene background_video_rakpart
    with Dissolve(3.0)

    pause(2.0)

    show janos idle at left
    with Dissolve(2.0)

    # These display lines of dialogue.

    janos """
    What an ungodly hour to work. Not for the living, and certainly not for the everlasting.
    
    Nor for the undying, whatever you will call us.

    Magistrates in the dark.

    Fiends of the night.

    Leeches.

    Illuminati - that's a good one.

    Nevertheless, not the worst places to suffer through a laborius night.

    Eventually dawn comes anyway.

    Of course, there is a bit more danger to it, if it's accompanied by a handfull of initiated agents, 
    
    armed to the teeth - even if it's nnot sharpest nature can give - with wooden bullets and similarly lethal gadets.

    Naturally someone must have invited them.
    """

    #TODO:AUDIO queue footstep sound here
    "/Footsteps approach in the mist, thumping the ground with a growing determination of volume./"

    pause(2.0)

    janos """
    Can it be the gracious party host?

    or

    just another kindred, whose ignore puts them to the screws.

    Wouldn't be the first.

    And certainly not the last of its kind.
    """

    scene black
    with fade

    return
