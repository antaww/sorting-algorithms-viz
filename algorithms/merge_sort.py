"""
Merge Sort
----------
Principle:
1. Divide the array into two equal halves
2. Recursively sort each half
3. Merge the two sorted halves

Advantages:
- Stable (preserves order of equal elements)
- Efficient on large lists
- Predictable (always O(n log n))

Complexity:
- Average: O(n log n)
- Worst case: O(n log n)
- Best case: O(n log n)
"""

import pygame
from constants import *

class MergeSort:
    def __init__(self, array, colors, visualizer, sound_manager):
        self.array = array
        self.colors = colors
        self.visualizer = visualizer
        self.sound_manager = sound_manager
        self.comparisons = 0
        self.swaps = 0
        self.sort_interrupt = False

    def sort(self, start, end):
        if end - start > 1 and not self.sort_interrupt:
            mid = (start + end) // 2
            self.sort(start, mid)
            self.sort(mid, end)
            self._merge(start, mid, end)

    def _merge(self, start, mid, end):
        left = self.array[start:mid]
        right = self.array[mid:end]
        i = j = 0
        k = start

        while i < len(left) and j < len(right) and not self.sort_interrupt:
            self.comparisons += 1
            self.colors[k] = RED
            self.colors[start + i] = YELLOW
            self.colors[mid + j] = YELLOW
            self.sound_manager.compare_sound.play()
            self.visualizer.draw_array(self.array, self.colors, WIDTH // len(self.array))
            pygame.time.wait(1)

            if left[i] < right[j]:
                self.array[k] = left[i]
                i += 1
            else:
                self.array[k] = right[j]
                j += 1

            self.swaps += 1
            self.colors[k] = GREEN
            self.visualizer.draw_array(self.array, self.colors, WIDTH // len(self.array))
            pygame.time.wait(1)
            self.colors[k] = WHITE
            k += 1

        # Copier les éléments restants
        while i < len(left) and not self.sort_interrupt:
            self.array[k] = left[i]
            self.swaps += 1
            self.colors[k] = GREEN
            self.sound_manager.compare_sound.play()
            self.visualizer.draw_array(self.array, self.colors, WIDTH // len(self.array))
            pygame.time.wait(1)
            self.colors[k] = WHITE
            i += 1
            k += 1

        while j < len(right) and not self.sort_interrupt:
            self.array[k] = right[j]
            self.swaps += 1
            self.colors[k] = GREEN
            self.sound_manager.compare_sound.play()
            self.visualizer.draw_array(self.array, self.colors, WIDTH // len(self.array))
            pygame.time.wait(1)
            self.colors[k] = WHITE
            j += 1
            k += 1 