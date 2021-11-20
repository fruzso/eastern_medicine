label lost_willpower:
    # Game over
    scene black
    with fade

    pause(1.0)

    "You lost all your willpower"

    return

label defeat_mid_interogation:
    # Game over

    scene background_video_black_wheel_empty
    with Dissolve(3.0)

    centered "Janos grabs you swiftly"
    "His motions are too quick even for your eye to follow"
    "And the molecules of your bodym only boudn together by the Dark Fathers curse perpetuated through the ages begin to give."
    
    # This ends the game.
    return