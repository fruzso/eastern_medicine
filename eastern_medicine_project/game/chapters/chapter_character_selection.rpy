label character_selection:
    # Rakpart darkness
    # PLOTPOINTS: Character selction and customization

    scene background_video_black_wheel_filled
    with Dissolve(3.0)

    pause(3.0)

    menu choose_character:
        # TODO Names ypos 
        # TODO Hover color
        "Choose your character"
        "Almos":
            $ pc_sheet = Almos()
            call screen character_stats(pc_sheet, choosable=True)
        "Cayenne":
            $ pc_sheet = Cayenne()
            call screen character_stats(pc_sheet, choosable=True)
        
    label chosen:
        scene background_video_black_wheel_empty
        hide screen character_stats
              
        define pc = Character("[pc_sheet.NAME]") # The player character is defined, and can be reffered to as pc from hereon
        image pc idle = "[pc_sheet.NAME] idle.png"

        show pc idle at center

        call show_dynamic_stats

        centered "[pc_sheet.NAME], of clan [pc_sheet.CLAN]." 
        pc "[pc_sheet.QUOTE]"
        hide pc

    stop music fadeout 1.0
    hide screen dynamic_stats
    return