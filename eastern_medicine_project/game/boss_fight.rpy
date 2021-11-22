label fight_pc_start:
    "PLACEHOLDER" # TODO: STROY
    call fight

label fight_janos_start:
    centered "You try to escape his grasp."

    $ roll_janos = Roll(janos_sheet.DEXTERITY + janos_sheet.BRAWL, janos_sheet.hunger, difficulty=0)
    $ roll_janos.roll()
    $ roll_pc = Roll(pc_sheet.DEXTERITY + pc_sheet.BRAWL, pc_sheet.hunger, difficulty=roll_janos.margin_of_success)
    $ roll_pc.roll()

    if roll_pc.is_success:
        show pc idle at right
        pc "Hah!"
        hide pc

        centered "Your muscles cleverly obey your commands and you escape his grasp."

    else:
        show pc idle at right
        pc "Shit!"
        hide pc

        centered "His grasp hold firm."  

    "PLACEHOLDER" # TODO: STROY
    call final_fight

label final_fight:
    "PLACEHOLDER" # TODO: STROY

       