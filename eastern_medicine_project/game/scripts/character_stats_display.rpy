screen character_stats(sheet):
    add "images/[sheet.NAME] idle.png" pos (0,0)
    vbox xpos 500:
        # General
        text "Name: [sheet.NAME]"
        text "Age: [sheet.AGE]"
        text "Clan: [sheet.CLAN]"
        text "Generation: [sheet.GENERATION]"

    vbox xpos 700:
        # Attributes
        text "Strength: [sheet.STRENGTH]"
        text "Dexterity: [sheet.DEXTERITY]"
        text "Stamina: [sheet.STAMINA]"

        text "Charisma: [sheet.CHARISMA]"
        text "Manipulation: [sheet.MANIPULATION]"
        text "Composure: [sheet.COMPOSURE]"
            
        text "Intelligence: [sheet.INTELLIGENCE]"
        text "Wits: [sheet.WITS]"
        text "Resolve: [sheet.RESOLVE]"
    
    vbox xpos 900:
        # Skills
        text "Athletics: [sheet.ATHLETICS]"
        text "Brawl: [sheet.BRAWL]"
        text "Craft: [sheet.CRAFT]"
        text "Drive: [sheet.DRIVE]"
        text "Firearms: [sheet.FIREARMS]"
        text "Melee: [sheet.MELEE]"
        text "Larceny: [sheet.LARCENY]"
        text "Stealth: [sheet.STEALTH]"
        text "Survival: [sheet.SURVIVAL]"

        text "Animal ken: [sheet.ANIMAL_KEN]"
        text "Etiquette: [sheet.ETIQUETTE]"
        text "Insight: [sheet.INSIGHT]"
        text "Intimidation: [sheet.INTIMIDATION]"
        text "Leadership: [sheet.LEADERSHIP]"
        text "Performance: [sheet.PERFORMANCE]"
        text "Persuasion: [sheet.PERSUASION]" 
        text "Streetwise: [sheet.STREETWISE]"
        text "Subterfuge: [sheet.SUBTERFUGE]"

        text "Academics: [sheet.ACADEMICS]"
        text "Awareness: [sheet.AWARENESS]"
        text "Finance: [sheet.FINANCE]"
        text "Investigation: [sheet.INVESTIGATION]"
        text "Medicine: [sheet.MEDICINE]"
        text "Occult: [sheet.OCCULT]"
        text "Politics: [sheet.POLITICS]"
        text "Science: [sheet.SCIENCE]"
        text "Technology: [sheet.TECHNOLOGY]"

        # Disciplines
        text "Animalism: [sheet.ANIMALISM]"
        text "Auspex: [sheet.AUSPEX]"
        text "Celerity: [sheet.CELERITY]"
        text "Dominate: [sheet.DOMINATE]"
        text "Fortitude: [sheet.FORTITUDE]"
        text "Obfuscate: [sheet.OBFUSCATE]"
        text "Presence: [sheet.PRESENCE]"
        text "Potence: [sheet.POTENCE]"

        # Dynamic
        text "Starter health: [sheet.health]"
        text "Starter willpower: [sheet.willpower]"
        text "Starter hunger: [sheet.hunger]"

        # Other
        text "[sheet.BLOOD_POTENCY]"

    vbox:
        textbutton "Choose" action Jump("chosen")
        textbutton "Back" action Jump("choose_character")


