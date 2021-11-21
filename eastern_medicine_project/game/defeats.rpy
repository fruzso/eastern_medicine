label willpower_defeat:
    # Game over
    scene black
    with fade

    pause(1.0)

    centered "You lost all your willpower"

    return

label health_defeat:
    # Game over
    scene black
    with fade

    pause(1.0)

    centered "You lost all your health"

    return

label hunger_defeat:
    # Game over
    scene black
    with fade

    pause(1.0)

    centered "The beast takes over you."

    centered "There flashes of rampaging around in the room."

    centered "And Janos' word cathes the artificial light."

    return

label defeat_violent:
    # Game over

    scene background_video_black_wheel_empty
    with Dissolve(3.0)

    centered "Janos grabs you swiftly"
    centered "His motions are too quick even for your eye to follow"
    centered "And the molecules of your bodym only boudn together by the Dark Fathers curse perpetuated through the ages begin to give."
    
    # This ends the game.
    return