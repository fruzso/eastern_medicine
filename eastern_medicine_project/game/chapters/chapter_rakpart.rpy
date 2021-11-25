label rakpart:
    # Janos enters and ponders the crimes of the PC

    scene background_video_rakpart
    with Dissolve(1.0)

    show janos idle at right

    janos """
    What an ungodly hour to work for the living, and most certainly for the everlasting.
    
    or for the undying, or whatever you will call us.

    Magistrates in the dark.

    Fiends of the night.

    Leeches.

    Illuminati - that's a good one.

    Nevertheless, not the worst places to suffer through a laborius night.

    Eventually dawn comes anyway.

    Naturally, there is a bit more danger to it, if it's accompanied by a handfull of initiated agents, 
    
    armed to the teeth - even if it's not the sharpest nature can provide - with wooden bullets and similarly lethal whatnots.

    Someone must have invited them.
    """
    hide janos

    play sound rakpart_footsteps fadein 1.0 volume 1.0 # TODO : thi sshould be much louder
    centered """
    Footsteps approach in the mist, 
    thumping the ground with a growing determination of volume.
    """
    show janos idle at right
    janos """
    Can it be our gracious party host?

    or

    just another kindred, whose ignorance puts them to the screws.

    Wouldn't be the first of its kind.

    Certainly not the last.
    """
    stop sound fadeout 1.0
    hide janos
    scene black
    with fade
    return
