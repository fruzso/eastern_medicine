label interogation_3:
    # The main scene of the game, where the player returns many times
    # PLOTPOINTS: puttign together the pieces from teh puzzle

    scene black 
    with fade 
    
    play music background_music_interrogation volume 0.5 loop

    scene background_video_interogation
    with Dissolve(3.0)

    call show_dynamic_stats

    pause(1.0)

    hide screen dynamic_stats
    scene black
    with fade
    return