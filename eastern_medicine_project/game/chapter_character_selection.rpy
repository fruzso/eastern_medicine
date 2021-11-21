label character_selection:
    # Rakpart darkness
    # PLOTPOINTS: Character selction and customization

    # TODO:AUDIO add footstep sound

    scene background_video_black_wheel_filled
    with Dissolve(3.0)

    pause(3.0)

    menu choose_character:
        "Choose your character"
        "Almos":
            $ pc_sheet = Almos()
        "Cayanne":
            $ pc_sheet = Cayenne()
          
    define pc = Character("[pc_sheet.NAME]") # The player character is defined, and can be reffered to as pc from hereon
    image pc idle = "[pc_sheet.NAME] idle.png"

    show pc idle at center

    call show_dynamic_stats

    "[pc_sheet.NAME], of clan [pc_sheet.CLAN]. [pc_sheet.QUOTE]"



    pause(3.0)

    hide screen dynamic_stats
    scene black
    with fade
    return