import sys

import pygame
from pygame.locals import *
from Data.GameData import GameData
from Data.EventData import EventData


class Game:
    def __init__(self):
        self.is_game_running = True
        pygame.init()

        GameData.fps_clock = pygame.time.Clock()
        GameData.surface = pygame.display.set_mode((GameData.WINDOW_WIDTH, GameData.WINDOW_HEIGHT))

        pygame.display.set_caption(GameData.NAME)

    def init(self):
        pass

    def event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.exit()
            elif event.type == KEYDOWN:
                if event.key == K_w:
                    EventData.is_key_w_down = True
                if event.key == K_s:
                    EventData.is_key_s_down = True
                if event.key == K_a:
                    EventData.is_key_a_down = True
                if event.key == K_d:
                    EventData.is_key_d_down = True

            elif event.type == KEYUP:
                if event.key == K_w:
                    EventData.is_key_w_down = False
                if event.key == K_s:
                    EventData.is_key_s_down = False
                if event.key == K_a:
                    EventData.is_key_a_down = False
                if event.key == K_d:
                    EventData.is_key_d_down = False

            EventData.is_mouse_move = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == BUTTON_LEFT:
                    EventData.is_left_mouse_down = True
                if event.button == BUTTON_RIGHT:
                    EventData.is_right_mouse_down = True
                if event.button == BUTTON_MIDDLE:
                    EventData.is_middle_mouse_down = True
            if event.type == MOUSEBUTTONUP:
                if event.button == BUTTON_LEFT:
                    EventData.is_left_mouse_down = False
                if event.button == BUTTON_RIGHT:
                    EventData.is_right_mouse_down = False
                if event.button == BUTTON_MIDDLE:
                    EventData.is_middle_mouse_down = False
            if event.type == MOUSEMOTION:
                EventData.is_mouse_move = True
                EventData.mouse_x, EventData.mouse_y = event.pos

    def update(self):
        pass

    def draw(self):
        pass

    def loop(self):
        while self.is_game_running:
            GameData.surface.fill((0, 0, 0))
            self.event()
            self.draw()
            self.update()

            pygame.display.update()
            GameData.fps_clock.tick(GameData.FPS)

    def exit(self):
        pygame.quit()
        sys.exit()
