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

class HeapSort:
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
            self.sound_manager.swap_sound.play()
            self.colors[i] = GREEN
            self.colors[0] = RED
            self.visualizer.draw_array(self.array, self.colors, WIDTH // len(self.array))
            pygame.time.wait(1)
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
            self.sound_manager.compare_sound.play()
            self.visualizer.draw_array(self.array, self.colors, WIDTH // len(self.array))
            pygame.time.wait(1)

            if self.array[left] > self.array[largest]:
                largest = left
            self.colors[left] = WHITE
            self.colors[largest] = BLUE

        if right < n:
            self.comparisons += 1
            self.colors[right] = RED
            self.colors[largest] = BLUE
            self.sound_manager.compare_sound.play()
            self.visualizer.draw_array(self.array, self.colors, WIDTH // len(self.array))
            pygame.time.wait(1)

            if self.array[right] > self.array[largest]:
                largest = right
            self.colors[right] = WHITE
            self.colors[largest] = BLUE

        if largest != i:
            self.swaps += 1
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.sound_manager.swap_sound.play()
            self.colors[i] = GREEN
            self.colors[largest] = RED
            self.visualizer.draw_array(self.array, self.colors, WIDTH // len(self.array))
            pygame.time.wait(1)
            self.colors[largest] = WHITE
            self._heapify(n, largest) 