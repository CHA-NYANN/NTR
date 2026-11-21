# Environmental sounds share the effects slider. The crowd, rail and
# foreground cues can play at the same time as the score.
init python:
    renpy.music.register_channel("story_crowd", mixer="sfx", loop=True, tight=True)
    renpy.music.register_channel("story_rail", mixer="sfx", loop=True, tight=True)
    renpy.music.register_channel("story_train", mixer="sfx", loop=False)
