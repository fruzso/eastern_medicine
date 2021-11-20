label test:
    # Game over

    scene background_video_black_wheel_empty
    with Dissolve(3.0)

    $ pc_sheet = Almos()
    $ janos_sheet = Janos()

    centered "Janos grabs you swiftly"
    "His motions are too quick even for your eye to follow"
    "And the molecules of your bodym only boudn together by the Dark Fathers curse perpetuated through the ages begin to give."

    # Contest roll
    $ roll_janos = Roll(janos_sheet.INTELLIGENCE + janos_sheet.MANIPULATION, janos_sheet.hunger, difficulty=0)
    $ roll_janos.roll()
    $ roll_pc = Roll(pc_sheet.WITS + pc_sheet.PERSUASION, pc_sheet.hunger, difficulty=roll_janos.margin_of_success)
    $ roll_pc.roll()
    
    return