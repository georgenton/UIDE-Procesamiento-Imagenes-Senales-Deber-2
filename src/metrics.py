import numpy as np

def snr_db(clean: np.ndarray, test: np.ndarray) -> float:
    clean = clean.astype(np.float64)
    test = test.astype(np.float64)
    err = test - clean
    p_signal = np.mean(clean**2) + 1e-12
    p_noise = np.mean(err**2) + 1e-12
    return 10.0 * np.log10(p_signal / p_noise)

def band_energy_ratio_db(x: np.ndarray, fs: int, band: tuple[float, float]) -> float:
    x = x.astype(np.float64)
    N = len(x)
    X = np.fft.rfft(x)
    freqs = np.fft.rfftfreq(N, 1/fs)

    low, high = band
    in_band = (freqs >= low) & (freqs <= high)
    out_band = ~in_band

    e_in = np.sum(np.abs(X[in_band])**2) + 1e-12
    e_out = np.sum(np.abs(X[out_band])**2) + 1e-12
    return 10.0 * np.log10(e_in / e_out)
