import pygame
import random
import time
from constants import *
from sound_manager import SoundManager
from visualization import Visualizer
from algorithms import QuickSort, MergeSort, ShellSort, HeapSort, InsertionSort, CombSort

def generate_array(size):
    arr = list(range(1, size + 1))
    random.shuffle(arr)
    return [int((value / size) * (HEIGHT - 150)) for value in arr]

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sorting Algorithms Visualization")
    clock = pygame.time.Clock()
    
    sound_manager = SoundManager()
    visualizer = Visualizer(screen)
    
    array_size = DEFAULT_ARRAY_SIZE
    array = generate_array(array_size)
    colors = [WHITE] * array_size
    
    input_active = False
    input_text = str(array_size)
    input_box = pygame.Rect(WIDTH // 2 + 250, HEIGHT - 120, 100, 35)
    
    # Variables pour les statistiques
    selected_algorithm = None
    start_time = None
    end_time = None
    current_sorter = None
    sort_started = False
    
    algorithms = {
        pygame.K_1: (QuickSort, "Quicksort"),
        pygame.K_2: (MergeSort, "Merge Sort"),
        pygame.K_3: (ShellSort, "Shell Sort"),
        pygame.K_4: (HeapSort, "Heapsort"),
        pygame.K_5: (InsertionSort, "Insertion Sort"),
        pygame.K_6: (CombSort, "Comb Sort")
    }
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN and selected_algorithm is None:
                input_active = input_box.collidepoint(event.pos)
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and selected_algorithm is not None:
                    selected_algorithm = None
                    start_time = None
                    end_time = None
                    current_sorter = None
                    sort_started = False
                    array = generate_array(array_size)
                    colors = [WHITE] * array_size
                elif selected_algorithm is None:
                    if input_active:
                        if event.key == pygame.K_RETURN:
                            try:
                                new_size = min(int(input_text), 2000)
                                if 10 <= new_size <= 2000:
                                    array_size = new_size
                                    array = generate_array(array_size)
                                    colors = [WHITE] * array_size
                                input_text = str(array_size)
                            except ValueError:
                                input_text = str(array_size)
                            input_active = False
                        elif event.key == pygame.K_BACKSPACE:
                            input_text = input_text[:-1]
                        elif event.unicode.isdigit() and len(input_text) < 4:
                            input_text = input_text + event.unicode
                    elif event.key == pygame.K_TAB:
                        input_active = True
                    elif event.key in algorithms:
                        AlgorithmClass, name = algorithms[event.key]
                        selected_algorithm = name
                        array_copy = array.copy()
                        colors_copy = colors.copy()
                        current_sorter = AlgorithmClass(array_copy, colors_copy, visualizer, sound_manager)
                elif event.key == pygame.K_SPACE and not sort_started:
                    sort_started = True
                    start_time = time.time()
                    current_sorter.start_time = start_time
                    if selected_algorithm == "Quicksort":
                        current_sorter.sort(0, len(array) - 1)
                    elif selected_algorithm == "Merge Sort":
                        current_sorter.sort(0, len(array))
                    else:
                        current_sorter.sort()
                    current_sorter.final_sweep()
                    end_time = time.time()
                    current_sorter.end_time = end_time
                    sound_manager.complete_sound.play()
        
        screen.fill(BLACK)
        if selected_algorithm is None:
            input_box_color = INPUT_BOX_COLOR_ACTIVE if input_active else INPUT_BOX_COLOR_INACTIVE
            visualizer.draw_menu(input_box, input_box_color, input_text)
        else:
            stats = {
                'algorithm': selected_algorithm,
                'size': array_size,
                'comparisons': current_sorter.comparisons if current_sorter else 0,
                'swaps': current_sorter.swaps if current_sorter else 0,
                'start_time': start_time if sort_started else None,
                'end_time': end_time
            }
            visualizer.draw_array(
                current_sorter.array if current_sorter else array,
                current_sorter.colors if current_sorter else colors,
                WIDTH // array_size,
                stats
            )
            
        clock.tick(FPS)
        pygame.display.flip()
        
    pygame.quit()

if __name__ == "__main__":
    main() 