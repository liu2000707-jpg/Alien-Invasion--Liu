import pygame

class GameAudios:
    def __init__(self):
        pygame.mixer.init()
        self.bgm = {
            "battle":"sounds/Meditating Beat.mp3",
            "boss":"sounds/Epic Boss Battle.mp3",
            }
        self.sounds = {
            "laser": pygame.mixer.Sound("sounds/Laser Shoot.mp3"),
            "destroy": pygame.mixer.Sound("sounds/Collision Destroy.mp3"),
            }

    def play_bgm(self, style, loop=-1, volume=0.5):
        pygame.mixer.music.load(self.bgm[style])
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(loop)

    def play_sounds(self, name, loop=1, volume=0.5):
        sound = self.sounds[name]
        sound.set_volume(volume)
        sound.play(loop)

    def stop_bgm(self):
        pygame.mixer.stop()

    def stop_sounds(self):
        pygame.mixer.music.stop()
