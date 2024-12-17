"""
Comb Sort
---------
Principle:
1. Uses a gap larger than 1 (initially n/1.3)
2. Compare elements with gap distance
3. Reduce gap by factor 1.3 in each iteration
4. When gap = 1, it becomes bubble sort
5. The gap sequence helps eliminate small values at end (turtle values)

Advantages:
- Much better than Bubble Sort
- Simple implementation
- Handles "turtle" values efficiently
- Visually interesting with varying gaps

Complexity:
- Average: O(n²/2^p) where p is number of increments
- Worst case: O(n²)
- Best case: O(n log n)
"""

import pygame
from constants import *
from .base_sort import BaseSort

class CombSort(BaseSort):
    def __init__(self, array, colors, visualizer, sound_manager):
        super().__init__(array, colors, visualizer, sound_manager)
        self.sort_interrupt = False

    def get_next_gap(self, gap):
        # Shrink gap by factor of 1.3
        gap = int(gap / 1.3)
        return max(1, gap)

    def sort(self):
        n = len(self.array)
        gap = n
        swapped = True

        while gap != 1 or swapped:
            if self.sort_interrupt:
                return

            gap = self.get_next_gap(gap)
            swapped = False

            for i in range(0, n - gap):
                if self.sort_interrupt:
                    return

                self.comparisons += 1
                self.colors[i] = RED
                self.colors[i + gap] = BLUE
                self.sound_manager.play_comparison_sound(i, n)
                self.update_display()
                pygame.time.wait(SORTING_DELAY)

                if self.array[i] > self.array[i + gap]:
                    self.swaps += 1
                    self.array[i], self.array[i + gap] = self.array[i + gap], self.array[i]
                    self.sound_manager.play_swap_sound(i, n)
                    swapped = True
                    self.colors[i] = YELLOW
                    self.colors[i + gap] = GREEN
                    self.update_display()
                    pygame.time.wait(SORTING_DELAY)

                self.colors[i] = WHITE
                self.colors[i + gap] = WHITE

                # Visualiser le gap actuel
                if i + gap * 2 < n:
                    self.colors[i + gap * 2] = (100, 100, 255, 128)  # Bleu clair pour montrer le motif du gap
                    self.update_display() 