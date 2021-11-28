# The Main script of the game goes in this file.
# Sajti and Stangli love each other (and their typos) very much :).

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define janos = Character("Janos")
define cecilia = Character("Cecilia")
define agent = Character("Agent")
# PC is defined in chapter_character_selction.rpy

# Audio
define audio.background_music_rakpart = "music/background_music_rakpart.mp3"
define audio.background_music_interrogation = "music/background_music_interrogation.mp3"
define audio.background_music_hospital = "music/background_music_hospital.mp3"
define audio.background_music_carpark = "music/background_music_carpark.mp3"
define audio.background_music_haven = "music/background_music_haven.mp3"
define audio.background_music_run_and_bossfight = "music/background_run_and_bossfight.mp3"
define audio.background_music_victory = "music/background_music_victory.mp3"
define audio.nostalgia = "music/nostalgia.mp3"

define audio.background_noise_hospital = "music/background_hospital_noises.mp3"
define audio.background_noise_carpark = "music/background_carpark_noises.mp3"

define audio.beast_roar = "sounds/beast_roar.mp3"
define audio.death_scream_1 = "sounds/death_scream_1.mp3"
define audio.death_scream_2 = "sounds/death_scream_2.mp3"
define audio.death_scream_3 = "sounds/death_scream_3.mp3"
define audio.fireworks = "sounds/fireworks.mp3"
define audio.flashbang_high = "sounds/flashbang_high.mp3"
define audio.flashbang_low = "sounds/flashbang_low.mp3"
define audio.gunfight = "sounds/gunfight.mp3"
define audio.interrogation_footsteps_and_door = "sounds/interrogation_footsteps_and_door.mp3"
define audio.knife_slash = "sounds/knife_slash.mp3"
define audio.machine_gun_single = "sounds/machine_gun_single.mp3"
define audio.machine_gun_longer = "sounds/machine_gun_longer.mp3"
define audio.outside_alarm = "sounds/outside_alarm.mp3"
define audio.rakpart_footsteps = "sounds/rakpart_footsteps.mp3"
define audio.smash_and_grunt = "sounds/smash_and_grunt.mp3"
define audio.smoke_bomb = "sounds/smoke_bomb.mp3"
define audio.wall_breaking = "sounds/wall_breaking.mp3"
define audio.widget_gain_stat = "sounds/widget_gain_stat.mp3"
define audio.widget_lose_stat = "sounds/widget_lose_stat.mp3"
define audio.pulse = "sounds/pulse.mp3"
define audio.hiss = "sounds/hiss.mp3"
define audio.heal = "sounds/heal.mp3"
define audio.memory = "sounds/memory.mp3"

# dialogue settings
define gui.dialogue_xpos = 250
define gui.dialogue_ypos = 125

# namebox settings
define gui.name_xalign = 0.5
define gui.name_yalign = 0.5
define gui.name_xpos = 250
define gui.name_ypos = 10
define gui.namebox_width = 300
define gui.namebox_height = 125

image background_video_rakpart = Movie(play = "video/movie_rakpart.webm", mask = None)
image background_video_interogation = Movie(play = "video/movie_interogation.webm", mask = None)
image background_video_black_wheel_filled = Movie(play = "video/movie_character_selection_filled.webm")
image background_video_black_wheel_empty = Movie(play = "video/moive_character_seelction_empty.webm", mask = None)
image backgorund_video_hospital = Movie(play = "video/movie_hospital.webm", mask = None)
image background_video_carpark = Movie(play = "video/movie_carpark.webm", mask = None)
image background_video_haven = Movie(play = "video/movie_haven.webm", mask = None)
image background_ekg = Movie(play = "video/movie_ekg_title.webm", loop = False)
image white = "#ffff"

# Props
transform dice_transform:
    zoom 0.065
image dice = At("images/d10.png", dice_transform)

# The game starts here.
label start:
    # This is the selection of the entire game, where every scene connects and is callled
    
    call variables # Non-story label

    # call test

    call intro

    call rakpart

    call character_selection

    call interogation_1

    call hospital

    call interogation_2

    call haven

    call interogation_3

    call carpark

    call interogation_4
    
 
        
label variables:
    # Only programatic content, nothing to show
    # Game mechanics:

    # Janos
    $ janos_strikes = 0
    $ janos_strikes_limit = 3
    $ janos_sheet = Janos()
    $ janos_suspicion_meter = 0
    $ janos_guilt_critera = 3

    # Story events:
    # False by default and only switched if chosen
    $ story_mention_emilio = False # To be able to act upon when Emilio comes up for the first time
    $ story_seated = False # Whether the pc sat down to the chair
    $ story_pc_guilty = False # Weather you think you are guilty
    $ story_janos_condemns = True # Weather Janos thinks you are guilty
    $ story_violent_arrival = False # Did the si agenets wake up the pc
    $ story_si_vision = False # pc vision of the si agents
    $ story_weapon = "Nothing"
    $ story_remaining_si = 4 # Second Inquisition agent in the Haven scene

    return

