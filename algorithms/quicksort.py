"""
Quicksort
---------
Principle:
1. Choose a pivot (here the last element)
2. Partition the array around the pivot:
   - Smaller elements to the left
   - Larger elements to the right
3. Recursively sort the left and right subarrays

Complexity:
- Average: O(n log n)
- Worst case: O(n²)
- Best case: O(n log n)
"""

import pygame
from .base_sort import BaseSort
from constants import *

class QuickSort(BaseSort):
    def __init__(self, array, colors, visualizer, sound_manager):
        super().__init__(array, colors, visualizer, sound_manager)
        self.sort_interrupt = False

    def _partition(self, low, high):
        pivot = self.array[high]
        self.colors[high] = BLUE
        i = low - 1
        
        for j in range(low, high):
            if self.sort_interrupt:
                return i + 1
                
            self.comparisons += 1
            self.colors[j] = RED
            self.sound_manager.play_comparison_sound(j, len(self.array))
            self.update_display()
            pygame.time.wait(SORTING_DELAY)
            
            if self.array[j] < pivot:
                i += 1
                self.swaps += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
                self.sound_manager.play_swap_sound(i, len(self.array))
                self.colors[i] = GREEN
                self.colors[j] = WHITE
                self.update_display()
                pygame.time.wait(SORTING_DELAY)
            else:
                self.colors[j] = WHITE
                
        self.swaps += 1
        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
        self.sound_manager.play_swap_sound(i + 1, len(self.array))
        self.colors[i + 1] = GREEN
        self.colors[high] = WHITE
        self.update_display()
        pygame.time.wait(SORTING_DELAY)
        
        return i + 1 

    def sort(self, low, high):
        if low < high and not self.sort_interrupt:
            pivot_index = self._partition(low, high)
            self.sort(low, pivot_index - 1)
            self.sort(pivot_index + 1, high)