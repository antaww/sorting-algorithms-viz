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
    def _partition(self, low, high):
        pivot = self.array[high]
        self.colors[high] = BLUE
        i = low - 1
        
        for j in range(low, high):
            self.comparisons += 1
            self.colors[j] = RED
            self.sound_manager.compare_sound.play()
            self.update_display()
            pygame.time.wait(1)
            
            if self.array[j] < pivot:
                i += 1
                self.swaps += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
                self.sound_manager.swap_sound.play()
                self.colors[i] = GREEN
                self.colors[j] = WHITE
                self.update_display()
                pygame.time.wait(1)
            else:
                self.colors[j] = WHITE
                
        self.swaps += 1
        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
        self.sound_manager.swap_sound.play()
        self.colors[i + 1] = GREEN
        self.colors[high] = WHITE
        self.update_display()
        pygame.time.wait(1)
        
        return i + 1 

    def sort(self, low, high):
        if low < high:
            pivot_index = self._partition(low, high)
            self.sort(low, pivot_index - 1)
            self.sort(pivot_index + 1, high)