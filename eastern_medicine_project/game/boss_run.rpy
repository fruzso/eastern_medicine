label run:
    play music background_music_run_and_fight volume 0.5 loop
    
    centered """
    It's decided, you have to flee for your life.
    There will be no time to appeal to the prince.
    It is now or never.
    """

    menu where_to_run:
        "Choose a direction!"

        "The door might be too obvious, but that's the surprise":
            centered "You get up and try to make your way to the door."
            centered "Buy Janos grabs you quickly."
            call fight_janos_start

        "The window will do just fine":
            centered "You get up and try to make your way to the window."
            centered "Buy Janos grabs you quickly."
            call fight_janos_start

        # Discipline choices
        "Vanish into thin air {image=dice}" if pc_sheet.OBFUSCATE >= 4:
            centered "Thank the Dark Father, you have the power to vanish."
            
            # Rousecheck
            if not pc_sheet.rouse_check():
                call change_dynamic_stats("worse")                   

            # Roll Vanish
            $ roll_janos = Roll(janos_sheet.WITS + janos_sheet.AWARENESS, janos_sheet.hunger, difficulty=0)
            $ roll_janos.roll()
            $ roll_pc = Roll(pc_sheet.WITS + pc_sheet.OBFUSCATE, pc_sheet.hunger, difficulty=roll_janos.margin_of_success)
            $ roll_pc.roll()

            if not roll_pc.is_success:
                centered "You begin to fade in front of Janos' eyes, but the nosferatu cannot be fooled."
                call fight_janos_start
    
            else:
                centered "You vanish before Janos' eyes."

                if janos_sheet.AUSPEX < 1:
                    call victory
                    centered "You escape through the door."                          

                else:
                    # Roll Sense of the unseen
                    $ roll_janos = Roll(janos_sheet.WITS + janos_sheet.AUSPEX, janos_sheet.hunger, difficulty=0)
                    $ roll_janos.roll()
                    $ roll_pc = Roll(pc_sheet.WITS + pc_sheet.OBFUSCATE, pc_sheet.hunger, difficulty=roll_janos.margin_of_success)
                    $ roll_pc.roll()

                    centered "You sense that he is looking for you with the dark powers of sight."

                    if roll_pc.is_success:
                        centered "But it is to no point. He cannot find you."
                        centered "You escape through the door."
                        call victory
                    else:
                        centered "Shit. He's got you"
                        call fight_janos_start

        "I've got speed (CELERITY)" if pc_sheet.CELERITY >= 3:
            centered "It does not really matter which way you go, the question is can you get there quickly enough."
            centered "You decide for the door."

            # Rousecheck
            if not pc_sheet.rouse_check():
                call change_dynamic_stats("worse")   

            # Roll Blink contest (potentially both are celerity users)
            $ roll_janos = Roll(janos_sheet.DEXTERITY + pc_sheet.CELERITY + janos_sheet.ATHLETICS, janos_sheet.hunger, difficulty=0)
            $ roll_janos.roll()
            $ roll_pc = Roll(pc_sheet.DEXTERITY + pc_sheet.CELERITY + pc_sheet.ATHLETICS, pc_sheet.hunger, difficulty=roll_janos.margin_of_success)
            $ roll_pc.roll()

            if not roll_pc.is_success:
                centered "You thought yourself to be quick as the wind."
                centered "But Janos was quicker."

                call fight_janos_start
            else:
                centered "You thought yourself qucik and damn, right you were."
                centered """
                Within the blink of an eye, you place your hand on the door handle
                press it down. Fresh air. Just what the doctor ordered.
                """
                centered "Politics you can't run out, but apperently Janos you could."

                call victory
