label character_selection:
    # Rakpart darkness
    # PLOTPOINTS: Character selction and customization

    # TODO: add footstep sound

    $ renpy.pause(2.0)

    scene background_video_black_wheel_filled
    with Dissolve(3.0)

    $ renpy.pause(3.0)

    menu choose_character:
        "Choose your character"
        "Almos":
<<<<<<< HEAD
            $ pc_sheet = Almos()
            "My name is [pc_sheet.NAME], I am a [pc_sheet.CLAN]. [pc_sheet.QUOTE]"
        "Cayanne":
            $ pc_sheet = Cayenne()
            "My name is [pc_sheet.NAME], I am a [pc_sheet.CLAN]. [pc_sheet.QUOTE]"
    return
=======
            "Almos"
            # pc is already defined in script.rpy by default as almos
            show pc idle #TODO: This pc character switch (together with line 26) needs to be fixed.
            python:
                import game_functions # Note: Tried and unfortunately it seems, that before callling a function the game_functions.py has to be balled in the same "python: " unit every time
                game_functions.create_character("Almos") #Note: the functions console.log is visible in the game engine, click at the bottom to console
        
        "Cayanne":
            "Cayanne"
            define pc = Character("Cayanne")
            show pc idle
            python:
                import game_functions
                game_functions.create_character("Cayanne")

    return
>>>>>>> FIX-0001 Brought back all the dialog and wrote some more.
