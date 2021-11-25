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
        centered "Who says there is no justice amond the kindred."
        centered "Pricely, justice is the privilage of the kindred."
        centered "You wonder tough, who the guilty party was..."

    hide pc

    jump the_end

label willpower_defeat:
    # Game over
    scene black
    with fade

    centered "You lost all your willpower."

    jump the_end

label health_defeat:
    # Game over
    scene black
    with fade

    centered "You lost all your health."

    jump the_end

label hunger_defeat:
    # Game over
    scene black
    with fade

    centered "The beast takes over you."

    centered "There flashes of rampaging around in the room."

    centered "And Janos' word cathes the artificial light."

    jump the_end

label vioient_defeat:
    # Game over

    scene background_video_black_wheel_empty
    with Dissolve(3.0)

    centered "Janos grabs you swiftly"
    centered "His motions are too quick even for your eyes to follow"
    centered "And the molecules of your body only bound together by the Dark Fathers curse perpetuated through the ages begin to give."
    
    # This ends the game.
    jump the_end