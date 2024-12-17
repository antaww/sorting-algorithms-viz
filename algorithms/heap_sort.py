"""
Heap Sort
---------
Principle:
1. Build a max heap (heapify)
2. Swap root with last element
3. Reduce heap size and reorganize
4. Repeat until heap is empty

Advantages:
- In-place sorting (no extra memory)
- Efficient on average
- Predictable (always O(n log n))

Complexity:
- Average: O(n log n)
- Worst case: O(n log n)
- Best case: O(n log n)
"""

import pygame
from constants import *
from .base_sort import BaseSort

class HeapSort(BaseSort):
    def __init__(self, array, colors, visualizer, sound_manager):
        super().__init__(array, colors, visualizer, sound_manager)
        self.sort_interrupt = False

    def sort(self):
        n = len(self.array)
        
        # Build heap
        for i in range(n // 2 - 1, -1, -1):
            if self.sort_interrupt:
                return
            self._heapify(n, i)

        # Extract elements one by one
        for i in range(n - 1, 0, -1):
            if self.sort_interrupt:
                return
            self.swaps += 1
            self.array[i], self.array[0] = self.array[0], self.array[i]
            self.sound_manager.play_swap_sound(i, n)
            self.colors[i] = GREEN
            self.colors[0] = RED
            self.update_display()
            pygame.time.wait(SORTING_DELAY)
            self.colors[0] = WHITE
            self._heapify(i, 0)

    def _heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n:
            self.comparisons += 1
            self.colors[left] = RED
            self.colors[largest] = BLUE
            self.sound_manager.play_comparison_sound(left, n)
            self.update_display()
            pygame.time.wait(SORTING_DELAY)

            if self.array[left] > self.array[largest]:
                largest = left
            self.colors[left] = WHITE
            self.colors[largest] = BLUE

        if right < n:
            self.comparisons += 1
            self.colors[right] = RED
            self.colors[largest] = BLUE
            self.sound_manager.play_comparison_sound(right, n)
            self.update_display()
            pygame.time.wait(SORTING_DELAY)

            if self.array[right] > self.array[largest]:
                largest = right
            self.colors[right] = WHITE
            self.colors[largest] = BLUE

        if largest != i:
            self.swaps += 1
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.sound_manager.play_swap_sound(i, n)
            self.colors[i] = GREEN
            self.colors[largest] = RED
            self.update_display()
            pygame.time.wait(SORTING_DELAY)
            self._heapify(n, largest) 