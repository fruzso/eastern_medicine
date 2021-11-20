label  rakpart:
    # Start scenne
    # Janos enters and ponders the crimes of the PC

    scene black
    with fade

    centered "August 22, 2021 Budapest, Hungary."

    play music background_music_rakpart volume 0.5 loop

    centered "Time: GTM+1 23:00"

    centered "Location: Somewhere near the seats of power that the Tzimische have cultivated for so long."

    scene background_video_rakpart
    with Dissolve(3.0)

    pause(2.0)

    show janos idle at left
    
    # Create Janos' character sheet
    $ janos_sheet = Janos()

    janos """
    What an ungodly hour to work for the living, and most certainly for the everlasting.
    
    or for the undying, or whatever you will call us.

    Magistrates in the dark.

    Fiends of the night.

    Leeches.

    Illuminati - that's a good one.

    Nevertheless, not the worst places to suffer through a laborius night.

    Eventually dawn comes anyway.

    Of course, there is a bit more danger to it, if it's accompanied by a handfull of initiated agents, 
    
    armed to the teeth - even if it's not the sharpest nature can provide - with wooden bullets and similarly lethal whatnots.

    Naturally someone must have invited them.
    """

    #TODO:AUDIO queue footstep sound here
    "/Footsteps approach in the mist, thumping the ground with a growing determination of volume./"

    pause(2.0)

    janos """
    Can it be our gracious party host?

    or

    just another kindred, whose ignorance puts them to the screws.

    Wouldn't be the first of its kind.

    Certainly not the last.
    """

    scene black
    with fade
    return
