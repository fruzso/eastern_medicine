label interogation_3:
    # The main scene of the game, where the player returns many times
    # PLOTPOINTS: puttign together the pieces from teh puzzle

    scene background_video_interogation
    with Dissolve(3.0)

    call screen show_dynamic_stats

    pause(1.0)

    hide screen dynamic_stats
    scene black
    with fade
    return