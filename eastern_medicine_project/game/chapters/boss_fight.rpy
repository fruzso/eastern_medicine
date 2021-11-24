label fight_pc_start:  
    #play music background_music_run_and_fight volume 0.5 loop
    $ renpy.music.play(audio.background_music_run_and_fight, relative_volume=0.5, loop=True, if_changed=True)

    menu first_attack:
        "He might not think I have the audacity to strike an annointed sheriff."
        "Strike him {image=dice}":
            call strike_janos_1
            call pc_hits_1

        "Confuse his mind {image=dice}" if pc_sheet.DOMINATE >= 2 and pc_sheet.OBFUSCATE >= 2:
            call dementation # Or call Victory
            call pc_hits_1

    call janos_hits_1

label pc_hits_1:
    centered "You try to get a jump on him."

    # Roll fight
    $ roll_janos = Roll(janos_sheet.DEXTERITY + janos_sheet.BRAWL, janos_sheet.hunger, difficulty=0)
    $ roll_janos.roll()
    $ roll_pc = Roll(pc_sheet.DEXTERITY + pc_sheet.BRAWL, pc_sheet.hunger, difficulty=roll_janos.margin_of_success)
    $ roll_pc.roll()

    if roll_pc.is_success:
        centered """Your muscles cleverly obey your command as courses through your nervous system,
        
        manifests in powerful blow
        
        and connects with Janos' already disfigured face."""

        $ janos_sheet.lose_health(roll_pc.margin_of_success)
        call check_janos_alive

    else:
        show pc idle at right
        pc "Shit!"
        hide pc

        centered "He evades your attack, looking fierce and out for blood."  
    return
    
label dementation:
    # Rousecheck
    if not pc_sheet.rouse_check():
        call change_dynamic_stats("worse")

    # Roll Dementation
    $ roll_janos = Roll(janos_sheet.INTELLIGENCE + janos_sheet.COMPOSURE, janos_sheet.hunger, difficulty=0)
    $ roll_janos.roll()
    $ roll_pc = Roll(pc_sheet.MANIPULATION + pc_sheet.DOMINATE, pc_sheet.hunger, difficulty=roll_janos.margin_of_success)
    $ roll_pc.roll()

    if roll_pc.is_success:
        show pc idle at right
        pc """
        Quite a sheriff you are. Ventured as far as the basement of the most famous building in the city.

        You didn't know what you will find.

        I guess you already presented to the prince that you know ALL about what happend.

        And now, having listened to my account, you haven't got the foggiest. 
        """
        hide pc

        centered "You see rage building up in the nosferatu."

        centered "You are hitting the right spots, just need to apply a bit mor epressure."

        show pc idle at right
        pc """
        Trapped in a time you don't really understand. With a language most jsut despise.

        Serving as the tzimische's lapdog. And nothing more.
        """
        hide pc

        show janos idle at right
        janos "Stop. You have no idea what you are talking about."
        hide janos

        centered "You know this is just a feeble attempt to shield his mind."

        show pc idle at right
        pc "You know how to stop this."
        hide pc

        centered "You get up and walk out of the door, leaving a petrified Janos behind."

        call victory

    else:
        show pc idle at right
        pc "Quite a sheriff you are. Ventured as far as the..."
        hide pc

        centered "He cuts you off mid-sentence."

        show janos idle at right
        janos "I am not gonna stand here and listen to your demented mind."
        hide janos

        return

label janos_hits_1:
    #play music background_music_run_and_fight volume 0.5 loop
    $ renpy.music.play(audio.background_music_run_and_fight, relative_volume=0.5, loop=True, if_changed=True)
    centered "You try to escape his grasp. {image=dice}"

    $ roll_janos = Roll(janos_sheet.DEXTERITY + janos_sheet.BRAWL, janos_sheet.hunger, difficulty=0)
    $ roll_janos.roll()
    $ roll_pc = Roll(pc_sheet.DEXTERITY + pc_sheet.BRAWL, pc_sheet.hunger, difficulty=roll_janos.margin_of_success)
    $ roll_pc.roll()

    if roll_pc.is_success:
        centered "Your muscles cleverly obey your commands and you escape his grasp."

    else:
        show pc idle at right
        pc "Shit!"
        hide pc

        centered "His grasp hold firm."  

    "PLACEHOLDER" # TODO: STROY
    return
    
       