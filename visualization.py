import pygame
import math
from constants import *
import time

# Ajouter ces constantes si elles n'existent pas déjà
GLASS_WHITE = (255, 255, 255, 30)
GLASS_DARK = (20, 20, 40, 150)

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
        # Fond dégradé
        gradient = pygame.Surface((WIDTH, HEIGHT))
        for y in range(HEIGHT):
            color = (
                int(20 + (y / HEIGHT) * 20),  # R
                int(10 + (y / HEIGHT) * 15),  # G
                int(40 + (y / HEIGHT) * 30)   # B
            )
            pygame.draw.line(gradient, color, (0, y), (WIDTH, y))
        self.screen.blit(gradient, (0, 0))
        
        # Effet de particules en arrière-plan (points qui bougent lentement)
        current_time = pygame.time.get_ticks()
        for i in range(50):  # 50 particules
            x = (WIDTH // 2 + (i * 173 + current_time // 50) % WIDTH) % WIDTH
            y = (HEIGHT // 2 + (i * 121 + current_time // 30) % HEIGHT) % HEIGHT
            pygame.draw.circle(self.screen, (100, 100, 150, 50), (x, y), 2)
        
        # Ajuster la taille de la police pour une meilleure lisibilité
        self.font_title = pygame.font.SysFont('Arial', 48)  # Plus grand pour le titre
        self.font_option = pygame.font.SysFont('Arial', 32)  # Plus grand pour les options
        self.font_instruction = pygame.font.SysFont('Arial', 24)  # Taille ajustée pour les instructions
        
        # Titre et sous-titre avec meilleur espacement
        title_text = "Sorting Algorithms"
        subtitle_text = "Visualization"
        
        # Panneau de verre pour le titre plus haut
        title_panel = pygame.Surface((600, 120), pygame.SRCALPHA)
        title_panel.fill((255, 255, 255, 25))
        pygame.draw.rect(title_panel, (255, 255, 255, 30), title_panel.get_rect(), border_radius=20)
        self.screen.blit(title_panel, (WIDTH // 2 - 300, 30))
        
        # Ajuster la position du titre et sous-titre
        title_surface = self.font_title.render(title_text, True, WHITE)
        subtitle_surface = self.font_title.render(subtitle_text, True, (200, 200, 255))
        self.screen.blit(title_surface, (WIDTH // 2 - title_surface.get_width() // 2, 45))
        self.screen.blit(subtitle_surface, (WIDTH // 2 - subtitle_surface.get_width() // 2, 95))
        
        # Options avec effet glassmorphism et meilleur espacement
        algorithms = [
            ("Quicksort", RED, "O(n log n)", "Fast & widely used", "1"),
            ("Merge Sort", GREEN, "O(n log n)", "Stable & reliable", "2"),
            ("Shell Sort", BLUE, "O(n log n)", "Adaptive & efficient", "3"),
            ("Heapsort", YELLOW, "O(n log n)", "Memory efficient", "4"),
            ("Insertion Sort", (200, 200, 200), "O(n²)", "Great for small data", "5")
        ]
        
        # Panneau principal des algorithmes ajusté - réduire la hauteur
        algo_panel = pygame.Surface((900, 350), pygame.SRCALPHA)  # Hauteur réduite
        algo_panel.fill((255, 255, 255, 15))
        pygame.draw.rect(algo_panel, (255, 255, 255, 30), algo_panel.get_rect(), border_radius=20)
        self.screen.blit(algo_panel, (WIDTH // 2 - 450, HEIGHT // 2 - 130))
        
        # Réduire l'espacement vertical entre les algorithmes
        for i, (name, color, complexity, description, key) in enumerate(algorithms):
            algo_rect = pygame.Rect(
                WIDTH // 2 - 400,
                HEIGHT // 2 - 110 + i * 60,  # Espacement réduit de 65 à 60
                800,
                50  # Hauteur réduite de 55 à 50
            )
            
            # Effet de survol avec plus de contraste
            mouse_pos = pygame.mouse.get_pos()
            if algo_rect.collidepoint(mouse_pos):
                pygame.draw.rect(self.screen, (255, 255, 255, 60), algo_rect, border_radius=10)
            else:
                # Fond plus sombre pour un meilleur contraste
                pygame.draw.rect(self.screen, (30, 30, 40, 25), algo_rect, border_radius=10)
            
            # Bordure plus visible
            pygame.draw.rect(self.screen, color, algo_rect, 2, border_radius=10)
            
            # Numéro de raccourci avec fond sombre pour plus de lisibilité
            key_bg = pygame.Rect(algo_rect.x + 10, algo_rect.y + 12, 35, 30)
            pygame.draw.rect(self.screen, (20, 20, 30), key_bg, border_radius=5)
            key_surface = self.font_instruction.render(f"[{key}]", True, color)
            self.screen.blit(key_surface, (algo_rect.x + 15, algo_rect.y + 15))
            
            # Nom de l'algorithme plus visible avec un léger effet d'ombre
            name_shadow = self.font_option.render(name, True, (20, 20, 30))
            self.screen.blit(name_shadow, (algo_rect.x + 61, algo_rect.y + 13))
            name_surface = self.font_option.render(name, True, color)
            self.screen.blit(name_surface, (algo_rect.x + 60, algo_rect.y + 12))
            
            # Description et complexité avec meilleur contraste
            desc_surface = self.font_instruction.render(f"{description} | {complexity}", True, (220, 220, 220))
            self.screen.blit(desc_surface, (algo_rect.x + 300, algo_rect.y + 18))
        
        # Panneau inférieur pour les contrôles déplacé plus bas
        control_panel = pygame.Surface((900, 130), pygame.SRCALPHA)
        control_panel.fill((255, 255, 255, 15))
        pygame.draw.rect(control_panel, (255, 255, 255, 30), control_panel.get_rect(), border_radius=20)
        self.screen.blit(control_panel, (WIDTH // 2 - 450, HEIGHT - 140))
        
        # Instructions avec icônes réorganisées sur deux colonnes
        instructions = [
            ("⌨️ Number keys", "Select algorithm"),
            ("🖱️ Click or TAB", "Edit array size"),
            ("⚡ SPACE", "Start sorting"),
            ("⬅️ ESC", "Return to menu")
        ]
        
        # Ajuster le positionnement des instructions (déplacées à gauche)
        for i, (icon, text) in enumerate(instructions):
            instruction = f"{icon} {text}"
            surface = self.font_instruction.render(instruction, True, (220, 220, 220))
            x_pos = WIDTH // 2 - 420 + (i % 2) * 380  # Déplacé plus à gauche
            y_pos = HEIGHT - 120 + (i // 2) * 35
            self.screen.blit(surface, (x_pos, y_pos))
        
        # Zone de saisie déplacée plus à droite et avec meilleure visibilité
        size_label = self.font_instruction.render("Array Size:", True, (220, 220, 220))
        input_box_x = WIDTH // 2 + 250  # Déplacé plus à droite
        input_box_y = HEIGHT - 120
        input_box_rect.x = input_box_x
        input_box_rect.y = input_box_y
        
        # Fond sombre pour la zone de saisie
        input_bg = pygame.Rect(input_box_rect.x - 120, input_box_rect.y - 5, 250, 45)
        pygame.draw.rect(self.screen, (30, 30, 40), input_bg, border_radius=10)
        
        # Label de la zone de saisie
        self.screen.blit(size_label, (input_box_rect.x - 110, input_box_rect.y + 8))
        
        # Boîte de saisie avec fond plus visible
        pygame.draw.rect(self.screen, (50, 50, 60), input_box_rect, border_radius=10)  # Fond plus visible
        pygame.draw.rect(self.screen, input_box_color, input_box_rect, 2, border_radius=10)
        
        # Texte de saisie avec limitation et meilleure visibilité
        if input_text:
            # Limiter le texte pour qu'il ne dépasse pas la boîte
            font_input = pygame.font.SysFont('Arial', 28)  # Police légèrement plus petite
            input_surface = font_input.render(input_text, True, (220, 220, 220))  # Texte plus visible
            
            # Vérifier si le texte dépasse la boîte
            if input_surface.get_width() > input_box_rect.width - 20:
                # Tronquer le texte si nécessaire
                while input_surface.get_width() > input_box_rect.width - 20:
                    input_text = input_text[:-1]
                    input_surface = font_input.render(input_text, True, (220, 220, 220))
            
            # Centrer le texte verticalement
            text_y = input_box_rect.y + (input_box_rect.height - input_surface.get_height()) // 2
            self.screen.blit(input_surface, (input_box_rect.x + 10, text_y))
        
        pygame.display.flip() 