screen dynamic_stats(character_name, character_clan, health_value, hunger_value, willpower_value):
    
    # Paintbrush background
    add "gui/dynamic_stats/meter_widget_[character_name].png" pos (0, 0) xysize (410, 195)

    # Show stats button bg
    add "gui/dynamic_stats/stat_button_bg.png" pos (30, 123) xysize (150, 70) # For show stats texctbutton
    add "gui/dynamic_stats/stat_button_bg.png" pos (170, 123) xysize (150, 70) # For heal texctbutton

    # Clan symbol
    add "gui/dynamic_stats/clan_symbol_[character_clan].png" pos (60, 40) xysize (100, 100)

    # Meters
    hbox xpos 175 ypos 40 spacing 10:
        vbox:
            text "WILLPOWER" size 15
            text "HEALTH" size 15
            text "HUNGER" size 15

        vbox: 
            text "[willpower_value]" size 15 bold True
            text "[health_value]" size 15 bold True
            text "[hunger_value]" size 15 bold True

    frame xpos 80 ypos 140:
        background None
        hbox:
            textbutton "HEAL":
                action Call("heal")
                text_size 15
                text_color "#FFFFFF"
                text_hover_color "#264e60"
            textbutton "STATS":
                action Show("character_stats", sheet=pc_sheet, choosable=False)
                text_size 15
                text_color "#FFFFFF"
                text_hover_color "#264e60"


label heal:
    # Increase health at the cost of doing a rouse check
    # if pc_sheet.health < pc_sheet.MAX_HEALTH:
    $ pc_sheet.heal(1)
    call change_dynamic_stats("better")

    # if not pc_sheet.rouse_check():
    #     action Call(change_dynamic_stats, direction="worse")
    return 
    
    
label show_dynamic_stats:
    show screen dynamic_stats(character_name=pc_sheet.NAME, character_clan=pc_sheet.CLAN, health_value=pc_sheet.health, hunger_value=pc_sheet.hunger, willpower_value=pc_sheet.willpower)
    return

label change_dynamic_stats(direction):
    hide screen dynamic_stats
    with Dissolve(0.5)

    if direction == "worse":
        play sound widget_lose_stat
    elif direction == "better":
        play sound widget_gain_stat
    
    if pc_sheet.willpower <= 0:
        call willpower_defeat
    elif pc_sheet.health <= 0:
        call health_defeat
    elif pc_sheet.hunger >= 5:
        call hunger_defeat
    else:
        call show_dynamic_stats
        with Dissolve(0.5)

        return