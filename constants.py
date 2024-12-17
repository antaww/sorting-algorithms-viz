import pygame

# Dimensions de l'écran
WIDTH = 1200
HEIGHT = 600
DEFAULT_ARRAY_SIZE = 300
FPS = 120

# Couleurs
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Couleurs de la boîte de saisie
INPUT_BOX_COLOR_INACTIVE = pygame.Color('lightskyblue3')
INPUT_BOX_COLOR_ACTIVE = pygame.Color('dodgerblue2') 

# Délais (en millisecondes)
SWEEP_DELAY = 5      # Délai pour l'effet de balayage final
SORTING_DELAY = 1    # Délai pendant le tri