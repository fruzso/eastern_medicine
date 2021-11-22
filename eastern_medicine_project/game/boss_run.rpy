label run:
    centered """
        It's decided, you have to flee for your life.
        There will be no time to appeal to the prince.
        It is now or never.
        """

        menu where_to_run:
            "Choose a direciton!"
            "Vanish into thin air (OBFUSCATE)" if pc_sheet.OBFUSCATE >= 4:
                centered "Thank the Dark Father, you have to power to vanish from the eye."
                
                # Rousecheck
                if not pc_sheet.rouse_check():
                    call change_dynamic_stats("worse")                   

                $ roll_janos = Roll(janos_sheet.WITS + janos_sheet.AWARENESS, janos_sheet.hunger, difficulty=0)
                $ roll_janos.roll()
                $ roll_pc = Roll(pc_sheet.WITS + pc_sheet.OBFUSCATE, pc_sheet.hunger, difficulty=roll_janos.margin_of_success)
                $ roll_pc.roll()

                if roll_pc.is_success:
                    centered "You vanish in front of Janos' eyes."

                    if janos_sheet.AUSPEX > 1:
                        $ roll_janos = Roll(janos_sheet.WITS + janos_sheet.AUSPEX, janos_sheet.hunger, difficulty=0)
                        $ roll_janos.roll()
                        $ roll_pc = Roll(pc_sheet.WITS + pc_sheet.OBFUSCATE, pc_sheet.hunger, difficulty=roll_janos.margin_of_success)
                        $ roll_pc.roll()

                        centered "You sense that is looking for you with dark power of sight"

                        if roll_pc.is_success:
                            centered "But it is to no point. He cannot find you."
                            call victory
                        else:
                            centered "Shit. He's got you"
                            call fight_2                              

                    else:
                        call victory

                else:
                    centered "You begin to fade in front of Janos' eyes, but the nosferatu cannot be fouled."
                    call defeat_violent


            "I've got speed (CELERITY)" if pc_sheet.CELERITY > 0:
                centered "PLACEHOLDER" # TODO:WRITE

            "The door might be too obvious, but that's the surprise":
                centered "PLACEHOLDER" # TODO:WRITE

            "The window will do just fine":
                centered "PLACEHOLDER" # TODO:WRITE
