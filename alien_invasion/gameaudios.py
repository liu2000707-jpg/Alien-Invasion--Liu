import pygame

class GameAudios:
    def __init__(self):
        self.bgm = {
            "battle":"sounds/Meditating Beat.mp3",
            "boss":"sounds/Epic Boss Battle.mp3"
            }

    def play_bgm(self, style, loop=-1, volume=0.5):
        pygame.mixer.music.load(self.bgm[style])
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(loop)

    def stop_bgm(self):
        pygame.mixer.music.stop()
        
