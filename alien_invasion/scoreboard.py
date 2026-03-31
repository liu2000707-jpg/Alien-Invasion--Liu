import pygame.font
class Scoreboard():
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = self.screen.dimension.get_rect()
        self.stats = stats

        #显示的文本样式
        self.text_color = (30,30,30)
        self.font = pygame.font.Font(None,  48)
        self.prep_high_score()
        self.prep_score()  # 初始得分图像

    def prep_high_score(self):
        high_score_str = "H: " + str(self.stats.high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.screen.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.right - 20
        self.high_score_rect.top = 20

    def prep_score(self):
        score_str = str(self.stats.scores)
        self.score_image = self.font.render(score_str, True, self.text_color, self.screen.bg_color)

            #锚定位置
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = self.high_score_rect.bottom + 10

    def show_score(self):
        self.screen.dimension.blit(self.high_score_image, self.high_score_rect)
        self.screen.dimension.blit(self.score_image, self.score_rect)

