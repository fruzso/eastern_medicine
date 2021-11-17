label character_selection:
    # Rakpart darkness
    # PLOTPOINTS: Character selction and customization

    scene background_video_black_wheel_filled
    with Dissolve(3.0)

    menu choose_character:
        "Choose your character"
        "Almos":
            $ pc_sheet = Almos()
            "My name is [pc_sheet.NAME], I am a [pc_sheet.CLAN]. [pc_sheet.QUOTE]"
        "Cayanne":
            $ pc_sheet = Cayenne()
            "My name is [pc_sheet.NAME], I am a [pc_sheet.CLAN]. [pc_sheet.QUOTE]"
    return