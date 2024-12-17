import pygame
import numpy as np

class SoundManager:
    def __init__(self):
        pygame.mixer.init(44100, -16, 2, 512)
        self.compare_sound = self._create_sound(800, 50)  # Son aigu court pour les comparaisons
        self.swap_sound = self._create_sound(400, 100)    # Son plus grave pour les échanges
        self.complete_sound = self._create_sound(600, 500) # Son de succès pour la fin
        self.sweep_sound = self._create_sound(1200, 20)   # Son aigu très court pour le balayage final
        
        # Ajuster les volumes
        self.compare_sound.set_volume(0.01)
        self.swap_sound.set_volume(0.02)
        self.complete_sound.set_volume(0.01)
        self.sweep_sound.set_volume(0.005)  # Volume plus faible pour ne pas être trop agressif

    def _create_sound(self, frequency, duration=50):
        sample_rate = 44100
        t = np.linspace(0, duration / 1000, int(sample_rate * duration / 1000), endpoint=False)
        sound_array = np.sin(2 * np.pi * frequency * t)
        sound_array = np.int16(sound_array * 32767)
        stereo_array = np.column_stack((sound_array, sound_array))
        return pygame.sndarray.make_sound(stereo_array) 