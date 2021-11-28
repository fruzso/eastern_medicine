label victory:
    # Game over - Victory
    # Only accessible at the end

    scene black 
    with fade

    centered "You have escaped."

    play music background_music_victory volume 1.0 loop

    scene background_video_rakpart
    with Dissolve(3.0)

    show pc idle at center

    if story_janos_condemns:
        centered "Janos tought you were guilty."
    else:
        centered "Janos thought you were innocent."
    
    centered "But it doesn't matter now."

    if story_pc_guilty:
        centered "Even tough you were guilty. You made it out."
        centered "After all, it's about the survival of the fittest, and that you are"
        centered "Your pride is hard-earned."
        centered "It's time to vanish into the night sky of Budapest."
        centered "Or maybe somewhere else..."
    else:
        centered "You were innocent and you made it out."
        centered "Just as it should be."
        centered "Who says there is no justice among the kindred."
        centered "Precisely, justice is the privilage of the kindred."
        centered "You wonder though, who the guilty party was..."

    hide pc

    jump the_end

label willpower_defeat:
    # Game over
    scene black
    with fade

    show pc idle at center
    centered """You fall to the ground. 

    Anyone around might think it is a sign of weekness,

    but inside, you know, that it is the strength of the beast that makes your undying heart beat.

    Yet, you cannot control it anymore.

    Knowing that there is no comming back from here you give all control over to it,

    having finally lost your will to hold it at bay."""
    hide pc
    with Dissolve(3.0)

    jump the_end

label health_defeat:
    # Game over
    hide screen dynamic_stats
    scene black
    with fade

    show pc idle at center
    centered """This was the last blow.

    Yes, at times, when well fed you can stitch back together wounded and demorphed flesh.

    Not anymore.
    
    Not that it matters, when your molecules are disintegrating with the first gust of wind."""
    hide pc
    with Dissolve(3.0)

    jump the_end

label hunger_defeat:
    # Game over
    scene black
    with fade

    show pc idle at center
    centered """There is a noise rattling inside your skull,

    nothing can silence it, nevermore,

    nothign can hold it back, nevermore.

    The smell of blood fills your nostrils.

    The beast takes over you.
    
    There're flashes of rampaging around.
    
    You have lost yourself."""
    hide pc
    with Dissolve(3.0)

    jump the_end

label violent_defeat:
    # Game over

    scene background_video_black_wheel_empty
    with Dissolve(1.0)

    show janos idle at center
    centered """You have made a fatal mistake. 

    Not sure where, though.

    Maybe it was something you said. Maybe something you didn't.

    But is does not matter anymore.
    
    Janos grabs you swiftly, with motions too quick even for your eyes to follow.

    Consequently, the molecules of your body only bound together by the Dark Father's curse,
    
    perpetuated through the ages begin to give."""
    hide janos
    with Dissolve(3.0)
    
    # This ends the game.
    jump the_end