import numpy as np
import scipy.io.wavfile as wav


def moving_average(_sample: np.array, _window: int) -> np.array:
    for n in np.arange(len(_sample[:, 0])):
        _sample[int(n), :] = np.mean(_sample[n : (n + _window), :], axis=0)
    return _sample


def exponential_smoother(_sample: np.array, _alpha: float) -> np.array:
    for n in np.arange(1, len(_sample[:, 0])):
        _sample[int(n), :] = (1 - _alpha) * _sample[int(n - 1), :] + _alpha * _sample[
            int(n), :
        ]

    return _sample


fs, audio = wav.read("inception_sound_track.wav")

up_sampled = np.zeros((3 * audio.shape[0], 2))
up_sampled[::3, :] = audio

# apply smoothing
smoothed = moving_average(up_sampled, 50)
#smoothed = exponential_smoother(up_sampled, 1)
wav.write("smoothed_file_1_exp.wav", fs, smoothed.astype("int16"))
