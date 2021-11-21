screen dynamic_stats(character_name, character_clan, health_value, hunger_value, willpower_value):
    # Paintbrush background
    add "gui/dynamic_stats/meter_widget_[character_name].png" pos (0, 0) 
    add "gui/dynamic_stats/clan_symbol_[character_clan].png" pos (75, 40) xysize (100, 100)

    hbox xpos 150 ypos 45:
        vbox:
            text "WILLPOWER" size 14
            text "HEALTH" size 14
            text "HUNGER" size 14
            textbutton "Character sheet" action Show("character_stats", sheet=pc_sheet, choosable=False)
            
        vbox: 
            text "[willpower_value]" size 14
            text "[health_value]" size 14
            text "[hunger_value]" size 14

        
    
label show_dynamic_stats:
    show screen dynamic_stats(character_name=pc_sheet.NAME, character_clan=pc_sheet.CLAN, health_value=pc_sheet.health, hunger_value=pc_sheet.hunger, willpower_value=pc_sheet.willpower)
    return

label change_dynamic_stats(direction):
    hide screen dynamic_stats
    with Dissolve(0.5)

    if direction == "lose":
        play sound "sounds/widget_lose_stat.mp3"
    elif direction == "gain":
        play sound "sounds/widget_gain_stat.mp3"
    

    if pc_sheet.willpower == 0:
        jump willpower_defeat
    if pc_sheet.health == 0:
        jump health_defeat
    if pc_sheet.hunger == 5:
        jump hunger_defeat

    call show_dynamic_stats
    with Dissolve(0.5)

    return