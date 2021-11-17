label character_selection:
    # Rakpart darkness
    # PLOTPOINTS: Character selction and customization

    scene background_video_black_wheel_filled
    with Dissolve(3.0)

    menu choose_character:
        "Choose your character"
        "Almos":
            "Almos"
            python:
                import game_functions # Note: Tried and unfortunately it seems, that before callling a function the game_functions.py has to be balled in the same "python: " unit every time
                game_functions.create_character("Almos") #Note: the functions console.log is visible in the game engine, click at the bottom to console
        
        "Cayanne":
            "Cayanne"
            python:
                import game_functions
                game_functions.create_character("Cayanne")

    return