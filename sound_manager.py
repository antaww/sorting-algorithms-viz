from pygame import mixer
import numpy as np

class SoundManager:
    def __init__(self):
        mixer.init()
        
        # Créer un tableau de sons avec des fréquences différentes
        self.comparison_sounds = self._generate_comparison_sounds(88)  # 88 comme un piano
        self.swap_sounds = self._generate_swap_sounds(88)
        
        # Générer les sons spéciaux
        self.complete_sound = self._generate_success_sound()
        self.sweep_sound = self._generate_sweep_sound()
        
    def _generate_tone(self, frequency, duration=0.1, volume=0.3):
        sample_rate = 44100
        t = np.linspace(0, duration, int(sample_rate * duration))
        # Générer une onde sinusoïdale
        tone = np.sin(2 * np.pi * frequency * t)
        # Appliquer une enveloppe pour éviter les clics
        envelope = np.exp(-3 * t)
        tone = tone * envelope
        # Normaliser et ajuster le volume
        tone = np.int16(tone * volume * 32767)
        return mixer.Sound(tone.tobytes())
    
    def _generate_success_sound(self):
        # Créer un son de succès avec un arpège montant
        duration = 0.5
        sample_rate = 44100
        t = np.linspace(0, duration, int(sample_rate * duration))
        
        # Créer un arpège avec plusieurs fréquences
        frequencies = [440, 554.37, 659.25, 880]  # La4, Do#5, Mi5, La5
        tone = np.zeros_like(t)
        
        for i, freq in enumerate(frequencies):
            # Décaler chaque note dans le temps
            start = int(i * sample_rate * duration / 5)
            end = int(sample_rate * duration)
            t_note = t[start:end]
            envelope = np.exp(-5 * np.linspace(0, 1, len(t_note)))
            tone[start:end] += np.sin(2 * np.pi * freq * t_note) * envelope
            
        tone = np.int16(tone * 0.2 * 32767)
        return mixer.Sound(tone.tobytes())
    
    def _generate_sweep_sound(self):
        # Créer un son de balayage court avec une fréquence montante
        duration = 0.02
        sample_rate = 44100
        t = np.linspace(0, duration, int(sample_rate * duration))
        
        # Réduire les fréquences du balayage
        freq_start = 600  # Au lieu de 800
        freq_end = 900    # Au lieu de 1200
        frequency = np.linspace(freq_start, freq_end, len(t))
        
        # Générer le son
        tone = np.sin(2 * np.pi * frequency * t)
        envelope = np.exp(-3 * t)
        tone = tone * envelope
        
        tone = np.int16(tone * 0.15 * 32767)
        return mixer.Sound(tone.tobytes())
        
    def _generate_comparison_sounds(self, count):
        # On baisse la fréquence de base et on réduit la plage de fréquences
        base_freq = 165  # Mi3 (E3) au lieu de 220 (A3)
        sounds = []
        for i in range(count):
            # Réduire la progression des fréquences en divisant par 16 au lieu de 12
            frequency = base_freq * (2 ** (i / 16))
            sounds.append(self._generate_tone(frequency, duration=0.1, volume=0.2))
        return sounds
        
    def _generate_swap_sounds(self, count):
        # Même chose pour les sons d'échange
        base_freq = 165
        sounds = []
        for i in range(count):
            frequency = base_freq * (2 ** (i / 16))
            sounds.append(self._generate_tone(frequency, duration=0.05, volume=0.15))
        return sounds
        
    def play_comparison_sound(self, index, array_length):
        relative_pos = index / array_length
        sound_index = int(relative_pos * (len(self.comparison_sounds) - 1))
        self.comparison_sounds[sound_index].play()
        
    def play_swap_sound(self, index, array_length):
        relative_pos = index / array_length
        sound_index = int(relative_pos * (len(self.swap_sounds) - 1))
        self.swap_sounds[sound_index].play() 