import pygame
from constants import *
import time

class Visualizer:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Arial', 20)
        self.font_title = pygame.font.SysFont('Arial', 40)
        self.font_option = pygame.font.SysFont('Arial', 30)
        self.font_instruction = pygame.font.SysFont('Arial', 25)
        
    def draw_array(self, array, colors, bar_width, stats):
        self.screen.fill(BLACK)
        
        # Display statistics
        font = pygame.font.SysFont('Arial', 20)
        if stats['start_time'] is None:
            stats_text = "Press SPACE to start sorting"
        else:
            elapsed_time = (stats['end_time'] or time.time()) - stats['start_time']
            stats_text = f"Algorithm: {stats['algorithm']} | Size: {stats['size']} | "
            stats_text += f"Comparisons: {stats['comparisons']} | Swaps: {stats['swaps']} | "
            stats_text += f"Time: {elapsed_time:.2f}s"
            if stats['end_time']:
                stats_text += " | Completed!"
        
        text_surface = font.render(stats_text, True, WHITE)
        self.screen.blit(text_surface, (10, 10))
        
        # Calculate bar width to occupy full width
        bar_width = WIDTH / len(array)  # Use float division
        
        # Display bars
        for i in range(len(array)):
            x = int(i * bar_width)  # Convert to integer for drawing
            width = int(bar_width)  # Ensure last bar fills the space properly
            if i == len(array) - 1:  # Adjust last bar to avoid gaps
                width = WIDTH - x
            
            pygame.draw.rect(
                self.screen,
                colors[i],
                (x, HEIGHT - array[i] - 50, width, array[i])
            )
        
        pygame.display.flip()
        
    def draw_menu(self, input_box_rect, input_box_color, input_text):
        self.screen.fill(BLACK)
        
        title_text = "Sorting Algorithms Visualization"
        options = [
            ("1. Quicksort", RED),
            ("2. Merge Sort", GREEN),
            ("3. Bubble Sort", BLUE),
            ("4. Heapsort", YELLOW),
            ("5. Insertion Sort", WHITE)  # Ajout du nouvel algorithme
        ]
        
        # Display title
        title_surface = self.font_title.render(title_text, True, WHITE)
        self.screen.blit(title_surface, (WIDTH // 2 - title_surface.get_width() // 2, HEIGHT // 4))
        
        # Display options
        for i, (text, color) in enumerate(options):
            surface = self.font_option.render(text, True, color)
            self.screen.blit(surface, (WIDTH // 2 - surface.get_width() // 2, HEIGHT // 2 - 80 + i * 50))
            
        # Display instructions
        instructions = [
            "Press the corresponding number to choose an algorithm",
            "Press 'TAB' or click the box to enter the size"
        ]
        
        for i, text in enumerate(instructions):
            surface = self.font_instruction.render(text, True, WHITE)
            self.screen.blit(surface, (WIDTH // 2 - surface.get_width() // 2, HEIGHT // 2 + 150 + i * 30))
            
        # Display input area
        pygame.draw.rect(self.screen, input_box_color, input_box_rect, 2)
        input_surface = self.font_option.render(input_text, True, WHITE)
        self.screen.blit(input_surface, (input_box_rect.x + 5, input_box_rect.y + 5))
        
        pygame.display.flip() 