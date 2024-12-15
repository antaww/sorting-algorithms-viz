from constants import WIDTH
import pygame

class BaseSort:
    def __init__(self, array, colors, visualizer, sound_manager):
        self.array = array
        self.colors = colors
        self.visualizer = visualizer
        self.sound_manager = sound_manager
        self.comparisons = 0
        self.swaps = 0
        self.start_time = None
        self.end_time = None
        
    def get_stats(self):
        return {
            'algorithm': self.__class__.__name__,
            'size': len(self.array),
            'comparisons': self.comparisons,
            'swaps': self.swaps,
            'start_time': self.start_time,
            'end_time': self.end_time
        }

    def update_display(self):
        self.visualizer.draw_array(
            self.array, 
            self.colors, 
            WIDTH // len(self.array),
            self.get_stats()
        )
        pygame.display.flip() 