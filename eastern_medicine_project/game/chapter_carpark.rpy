label carpark:
    # A memory of the Carpark
    # PLOTPOINTS: the mentors letter

    scene background_video_carpark
    with Dissolve(3.0)

    call show_dynamic_stats

    pause(1.0)

    hide screen dynamic_stats
    scene black
    with fade
    return