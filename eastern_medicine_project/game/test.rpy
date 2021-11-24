label test:
    # Game over
    # hover_color = u'#264e60'
    
    scene background_video_black_wheel_empty
    with Dissolve(3.0)

    $ pc_sheet = Almos()
    $ janos_sheet = Janos()

    call show_dynamic_stats

    centered "Test scene to test testable stuff. Hi!"

    play sound smoke_bomb
    
    centered "Tested something."

    centered "Tested another something."

        
    init python:
        renpy.music.register_channel("music_nostalgia", "music", True)

    play music background_music_hospital volume 0.5 loop
    centered "Tested something."
    play music_nostalgia nostalgia volume 0.2 loop
    centered "Tested something."
    stop music_nostalgia fadeout 1.0

    centered "This is still a test environment. Hihi"
    # pc "I'm Almos."

    # janos "And the molecules of your bodym only boudn together by the Dark Fathers curse perpetuated through the ages begin to give."
    # "a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a"

    # # Contest roll
    # $ roll_janos = Roll(janos_sheet.INTELLIGENCE + janos_sheet.MANIPULATION, janos_sheet.hunger, difficulty=0)
    # $ roll_janos.roll()
    # $ roll_pc = Roll(pc_sheet.WITS + pc_sheet.PERSUASION, pc_sheet.hunger, difficulty=roll_janos.margin_of_success)
    # $ roll_pc.roll()
    
    return