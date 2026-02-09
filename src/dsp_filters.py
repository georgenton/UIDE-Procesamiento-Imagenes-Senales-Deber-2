import numpy as np
from scipy.signal import butter, cheby1, ellip, firwin, filtfilt, lfilter

def normalize_audio(x: np.ndarray) -> np.ndarray:
    x = x.astype(np.float32)
    peak = np.max(np.abs(x)) + 1e-12
    return x / peak

def design_iir_bandpass(fs: int, low: float, high: float, kind: str, order: int = 4,
                        rp: float = 1.0, rs: float = 40.0):
    nyq = 0.5 * fs
    wn = [low / nyq, high / nyq]

    if kind == "butter":
        b, a = butter(order, wn, btype="band")
    elif kind == "cheby1":
        b, a = cheby1(order, rp, wn, btype="band")
    elif kind == "ellip":
        b, a = ellip(order, rp, rs, wn, btype="band")
    else:
        raise ValueError("kind debe ser: butter | cheby1 | ellip")
    return b, a

def design_iir_highpass(fs: int, fc: float, kind: str = "butter", order: int = 4,
                        rp: float = 1.0, rs: float = 40.0):
    nyq = 0.5 * fs
    wn = fc / nyq

    if kind == "butter":
        b, a = butter(order, wn, btype="high")
    elif kind == "cheby1":
        b, a = cheby1(order, rp, wn, btype="high")
    elif kind == "ellip":
        b, a = ellip(order, rp, rs, wn, btype="high")
    else:
        raise ValueError("kind debe ser: butter | cheby1 | ellip")
    return b, a

def apply_iir(x: np.ndarray, b, a, zero_phase: bool = True) -> np.ndarray:
    if zero_phase:
        return filtfilt(b, a, x)
    return lfilter(b, a, x)

def design_fir_bandpass(fs: int, low: float, high: float, ntaps: int = 401, window="hamming"):
    nyq = 0.5 * fs
    taps = firwin(ntaps, [low/nyq, high/nyq], pass_zero=False, window=window)
    return taps

def apply_fir(x: np.ndarray, taps) -> np.ndarray:
    return lfilter(taps, 1.0, x)
