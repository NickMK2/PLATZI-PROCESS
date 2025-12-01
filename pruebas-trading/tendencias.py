import numpy as np
import pandas as pd

# =========================================================
# 1. SIMULAR VELAS PARA PROBAR LA TENDENCIA
# =========================================================
def simulate_candles(n=500, seed=42):
    np.random.seed(seed)
    prices = np.cumsum(np.random.normal(0, 1, n)) + 100  # camino aleatorio

    df = pd.DataFrame({
        "open": prices,
        "high": prices + np.random.uniform(0.1, 1.0, n),
        "low": prices - np.random.uniform(0.1, 1.0, n),
        "close": prices + np.random.uniform(-0.5, 0.5, n)
    })

    return df


# =========================================================
# 2. DETECTAR TENDENCIA USANDO PIVOTES ADAPTATIVOS
# =========================================================
def detect_trend(df, lookback=20, tolerance=0.003):
    """
    lookback = cuántas velas hacia atrás analizamos
    tolerance = qué tan “distintos” deben ser máximos/mínimos para no considerarse rango
    """

    df = df.copy()
    df["pivot_high"] = df["high"].rolling(lookback).max()
    df["pivot_low"] = df["low"].rolling(lookback).min()

    trend = []
    for i in range(len(df)):
        if i < lookback:
            trend.append("NEUTRAL")
            continue

        ph_now = df["pivot_high"].iloc[i]
        ph_prev = df["pivot_high"].iloc[i - lookback]

        pl_now = df["pivot_low"].iloc[i]
        pl_prev = df["pivot_low"].iloc[i - lookback]

        # Variaciones relativas
        high_change = (ph_now - ph_prev) / ph_prev if ph_prev != 0 else 0
        low_change = (pl_now - pl_prev) / pl_prev if pl_prev != 0 else 0

        # Reglas
        if high_change > tolerance and low_change > tolerance:
            trend.append("UPTREND")
        elif high_change < -tolerance and low_change < -tolerance:
            trend.append("DOWNTREND")
        else:
            trend.append("RANGE")

    df["trend"] = trend
    return df


# =========================================================
# 3. EJECUCIÓN DE LA SIMULACIÓN
# =========================================================
if __name__ == "__main__":
    df = simulate_candles(400)

    result = detect_trend(
        df,
        lookback=20,       # puedes cambiarlo
        tolerance=0.002    # sensibilidad
    )

    print(result[["close", "pivot_high", "pivot_low", "trend"]].tail(40))
