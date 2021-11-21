# Dynamic stat variables
define widget_text_y_offset = 45
define widget_text_x_offset = 150
define widget_text_height = 14
define widget_counter_x_offset = 100

screen dynamic_stats(character_name, character_clan, health_value, hunger_value, willpower_value):
    # Paintbrush background
    add "gui/dynamic_stats/meter_widget_[character_name].png" pos (0, 0) 
    add "gui/dynamic_stats/clan_symbol_[character_clan].png" pos (75, 40) xysize (100, 100)

    text "WILLPOWER" size widget_text_height xpos widget_text_x_offset ypos widget_text_y_offset + widget_text_height
    text "HEALTH" size widget_text_height xpos widget_text_x_offset ypos widget_text_y_offset + (widget_text_height * 2)
    text "HUNGER" size widget_text_height xpos widget_text_x_offset ypos widget_text_y_offset + (widget_text_height * 3)

    text "[willpower_value]" size widget_text_height xpos widget_text_x_offset + widget_counter_x_offset ypos widget_text_y_offset + widget_text_height
    text "[health_value]" size widget_text_height xpos widget_text_x_offset + widget_counter_x_offset ypos widget_text_y_offset + (widget_text_height * 2)
    text "[hunger_value]" size widget_text_height xpos widget_text_x_offset + widget_counter_x_offset ypos widget_text_y_offset + (widget_text_height * 3)

label show_dynamic_stats:
    show screen dynamic_stats(character_name=pc_sheet.NAME, character_clan=pc_sheet.CLAN, health_value=pc_sheet.health, hunger_value=pc_sheet.hunger, willpower_value=pc_sheet.willpower)
    return

label change_dynamic_stats:
    hide screen dynamic_stats
    with dissolve(0.5)

    #TODO:AUDIO stat change sounds

    call show_dynamic_stats
    with dissolve(0.5)

    return