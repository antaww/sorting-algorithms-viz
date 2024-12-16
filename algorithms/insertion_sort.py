"""
Insertion Sort
-------------
Principle:
1. Start from the second element
2. Compare with previous elements
3. Insert the element at the right position
4. Repeat for all elements

Advantages:
- Simple implementation
- Efficient for small data sets
- Adaptive (efficient for data sets that are already substantially sorted)
- Stable sort
- In-place algorithm

Complexity:
- Average: O(n²)
- Worst case: O(n²)
- Best case: O(n) (already sorted array)
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
            self.colors[i] = BLUE  # Current element being inserted
            
            while j >= 0 and not self.sort_interrupt:
                self.comparisons += 1
                self.colors[j] = RED  # Element being compared
                self.sound_manager.compare_sound.play()
                self.update_display()
                pygame.time.wait(1)
                
                if self.array[j] > key:
                    self.swaps += 1
                    self.array[j + 1] = self.array[j]
                    self.colors[j] = GREEN
                    self.sound_manager.swap_sound.play()
                    self.update_display()
                    pygame.time.wait(1)
                    self.colors[j] = WHITE
                    j -= 1
                else:
                    self.colors[j] = WHITE
                    break
                    
            self.array[j + 1] = key
            self.colors[i] = WHITE 