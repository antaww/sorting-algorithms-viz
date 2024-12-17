"""
Insertion Sort
-------------
Principle:
1. Start from the second element
2. Compare with previous elements
3. Insert at the correct position
4. Repeat for all elements

Advantages:
- Simple implementation
- Efficient for small data sets
- Adaptive (efficient for data that is already substantially sorted)
- Stable (maintains relative order of equal elements)

Complexity:
- Average: O(n²)
- Worst case: O(n²)
- Best case: O(n) (already sorted)
"""

import pygame
from constants import *
from .base_sort import BaseSort

class InsertionSort(BaseSort):
    def __init__(self, array, colors, visualizer, sound_manager):
        super().__init__(array, colors, visualizer, sound_manager)
        self.sort_interrupt = False

    def sort(self):
        n = len(self.array)
        for i in range(1, n):
            if self.sort_interrupt:
                return
                
            key = self.array[i]
            j = i - 1
            self.colors[i] = BLUE  # Élément en cours d'insertion
            
            while j >= 0 and not self.sort_interrupt:
                self.comparisons += 1
                self.colors[j] = RED
                self.sound_manager.play_comparison_sound(j, n)
                self.update_display()
                pygame.time.wait(SORTING_DELAY)
                
                if self.array[j] > key:
                    self.swaps += 1
                    self.array[j + 1] = self.array[j]
                    self.sound_manager.play_swap_sound(j, n)
                    self.colors[j] = GREEN
                    self.update_display()
                    pygame.time.wait(SORTING_DELAY)
                    j -= 1
                else:
                    break
                    
                self.colors[j + 1] = WHITE
            
            self.array[j + 1] = key
            self.colors[i] = WHITE
            self.update_display()