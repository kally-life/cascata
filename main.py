# Game Title                : schiva la cascata
# Date                      : 08-10-2020
# Requirements              : Python 3.4.x , Requests module (python -m pip install requests)
# Code found on             : https://github.com/kally-life/schiva_la_cascata
# Author                    : Kally-life  Italian Pentester
# Tested on                 : Windows 10 / Ubuntu 14.04
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import sys
import pygame
from player import HumanPlayer
from screen import Screen
from game import Game

def play_game(screen, player, game):
	game_over = False
	while not game_over:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT and player.x > 0:
					player.x -= player.size
				elif event.key == pygame.K_RIGHT and player.x < (screen.width - player.size):
					player.x += player.size

		game.drop_enemies(screen.width)
		game.update_enemy_positions(screen.height)
		game.set_level()

		screen.update_screen(game.enemy_list, player, game.score)

		if game.collision_check(player):
			game_over = True
			break

if __name__ == "__main__":
	pygame.init()

	screen = Screen()
	player = HumanPlayer(screen.width/2, screen.height-100)
	game = Game()

	play_game(screen, player, game)