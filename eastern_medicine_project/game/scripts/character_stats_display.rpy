screen character_stats(sheet):
    add "images/[sheet.NAME] idle.png" pos (0,0)

    vbox spacing 40 xalign 0.5 yalign 0.5:
        hbox spacing 80:
            # General
            vbox:
                text "Name: [sheet.NAME]"
                text "Age: [sheet.AGE]"

            vbox:
                text "Clan: [sheet.CLAN]"
                text "Generation: [sheet.GENERATION]"
            
            vbox:    
                text "Sex: [sheet.SEX]"
                text "Blood potency: [sheet.BLOOD_POTENCY]"

        hbox spacing 80:
            # Attributes
            vbox:
                text "Strength: [sheet.STRENGTH]"
                text "Dexterity: [sheet.DEXTERITY]"
                text "Stamina: [sheet.STAMINA]"

            vbox:
                text "Charisma: [sheet.CHARISMA]"
                text "Manipulation: [sheet.MANIPULATION]"
                text "Composure: [sheet.COMPOSURE]"

            vbox:
                text "Intelligence: [sheet.INTELLIGENCE]"
                text "Wits: [sheet.WITS]"
                text "Resolve: [sheet.RESOLVE]"
        
        hbox spacing 80:
            # Skills
            vbox:
                text "Athletics: [sheet.ATHLETICS]"
                text "Brawl: [sheet.BRAWL]"
                text "Craft: [sheet.CRAFT]"
                text "Drive: [sheet.DRIVE]"
                text "Firearms: [sheet.FIREARMS]"
                text "Melee: [sheet.MELEE]"
                text "Larceny: [sheet.LARCENY]"
                text "Stealth: [sheet.STEALTH]"
                text "Survival: [sheet.SURVIVAL]"

            vbox:
                text "Animal ken: [sheet.ANIMAL_KEN]"
                text "Etiquette: [sheet.ETIQUETTE]"
                text "Insight: [sheet.INSIGHT]"
                text "Intimidation: [sheet.INTIMIDATION]"
                text "Leadership: [sheet.LEADERSHIP]"
                text "Performance: [sheet.PERFORMANCE]"
                text "Persuasion: [sheet.PERSUASION]" 
                text "Streetwise: [sheet.STREETWISE]"
                text "Subterfuge: [sheet.SUBTERFUGE]"

            vbox:
                text "Academics: [sheet.ACADEMICS]"
                text "Awareness: [sheet.AWARENESS]"
                text "Finance: [sheet.FINANCE]"
                text "Investigation: [sheet.INVESTIGATION]"
                text "Medicine: [sheet.MEDICINE]"
                text "Occult: [sheet.OCCULT]"
                text "Politics: [sheet.POLITICS]"
                text "Science: [sheet.SCIENCE]"
                text "Technology: [sheet.TECHNOLOGY]"
        
        hbox spacing 80:
            # Disciplines
            if sheet.ANIMALISM > 0: 
                text "Animalism: [sheet.ANIMALISM]"
            if sheet.AUSPEX > 0:
                text "Auspex: [sheet.AUSPEX]"
            if sheet.CELERITY > 0:
                text "Celerity: [sheet.CELERITY]"
            if sheet.DOMINATE > 0:
                text "Dominate: [sheet.DOMINATE]"
            if sheet.FORTITUDE > 0:
                text "Fortitude: [sheet.FORTITUDE]"
            if sheet.OBFUSCATE > 0:
                text "Obfuscate: [sheet.OBFUSCATE]"
            if sheet.PRESENCE > 0:
                text "Presence: [sheet.PRESENCE]"
            if sheet.POTENCE > 0:
                text "Potence: [sheet.POTENCE]"

        hbox spacing 80:
            # Dynamic
            text "Starter health: [sheet.health]"
            text "Starter willpower: [sheet.willpower]"
            text "Starter hunger: [sheet.hunger]"

    vbox:
        textbutton "Choose" action Jump("chosen")
        textbutton "Back" action Jump("choose_character")


