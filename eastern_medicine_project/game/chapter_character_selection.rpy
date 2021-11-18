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
            $ pc_sheet = Almos()
            "My name is [pc_sheet.NAME], I am a [pc_sheet.CLAN]. [pc_sheet.QUOTE]"
        "Cayanne":
            $ pc_sheet = Cayenne()
            "My name is [pc_sheet.NAME], I am a [pc_sheet.CLAN]. [pc_sheet.QUOTE]"
    
    define pc = Character("[pc_sheet.NAME]")
    show pc idle at right
    return
