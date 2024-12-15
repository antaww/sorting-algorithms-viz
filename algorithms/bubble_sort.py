"""
Bubble Sort
----------
Principle:
1. Traverse the array from left to right
2. Compare each pair of adjacent elements
3. Swap them if they are in the wrong order
4. Repeat until no swaps are needed

Advantages:
- Simple to understand and implement
- Stable (preserves order of equal elements)
- Little extra memory required

Complexity:
- Average: O(n²)
- Worst case: O(n²)
- Best case: O(n) (already sorted array)
"""

import pygame
from constants import *

class BubbleSort:
    def __init__(self, array, colors, visualizer, sound_manager):
        self.array = array
        self.colors = colors
        self.visualizer = visualizer
        self.sound_manager = sound_manager
        self.comparisons = 0
        self.swaps = 0
        self.sort_interrupt = False

    def sort(self):
        n = len(self.array)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.sort_interrupt:
                    return

                self.comparisons += 1
                self.colors[j] = RED
                self.colors[j + 1] = RED
                self.sound_manager.compare_sound.play()
                self.visualizer.draw_array(self.array, self.colors, WIDTH // len(self.array))
                pygame.time.wait(1)

                if self.array[j] > self.array[j + 1]:
                    self.swaps += 1
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    self.sound_manager.swap_sound.play()
                    self.colors[j] = GREEN
                    self.colors[j + 1] = GREEN
                    self.visualizer.draw_array(self.array, self.colors, WIDTH // len(self.array))
                    pygame.time.wait(1)

                self.colors[j] = WHITE
                self.colors[j + 1] = WHITE

            # Mark the last element as sorted
            self.colors[n - i - 1] = GREEN 