"""
Shell Sort
----------
Principle:
1. Start with a large gap and reduce it gradually
2. Compare elements that are 'gap' positions apart
3. Perform insertion sort on these sub-arrays
4. Reduce gap and repeat until gap = 1

Advantages:
- More efficient than Bubble Sort and Insertion Sort
- In-place algorithm (no extra memory needed)
- Adaptive (performs better on partially sorted arrays)

Complexity:
- Average: O(n log n) to O(n^(3/2)) depending on gap sequence
- Worst case: O(n^2)
- Best case: O(n log n)
"""

import pygame
from constants import *
from .base_sort import BaseSort

class ShellSort(BaseSort):
    def __init__(self, array, colors, visualizer, sound_manager):
        super().__init__(array, colors, visualizer, sound_manager)
        self.sort_interrupt = False

    def sort(self):
        n = len(self.array)
        gap = n // 2  # Start with n/2 gap

        while gap > 0 and not self.sort_interrupt:
            for i in range(gap, n):
                if self.sort_interrupt:
                    return

                temp = self.array[i]
                j = i

                # Compare elements that are 'gap' positions apart
                while j >= gap and not self.sort_interrupt:
                    self.comparisons += 1
                    self.colors[j] = RED
                    self.colors[j - gap] = BLUE
                    self.sound_manager.play_comparison_sound(j, n)
                    self.update_display()
                    pygame.time.wait(SORTING_DELAY)

                    if self.array[j - gap] > temp:
                        self.swaps += 1
                        self.array[j] = self.array[j - gap]
                        self.sound_manager.play_swap_sound(j, n)
                        self.colors[j] = GREEN
                        self.update_display()
                        pygame.time.wait(SORTING_DELAY)
                        j -= gap
                    else:
                        break

                    self.colors[j] = WHITE
                    if j + gap < n:
                        self.colors[j + gap] = WHITE

                self.array[j] = temp
                self.colors[j] = WHITE
                if i < n:
                    self.colors[i] = WHITE

            gap //= 2  # Reduce gap by half 