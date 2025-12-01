import pandas as pd
import numpy as np
import yfinance as yf
import ta
import matplotlib.pyplot as plt

# Descargar datos históricos del oro
data = yf.download('GC=F', start='2020-01-01', end='2023-01-01')

# Calcular ADX
data['ADX'] = ta.trend.adx(data['High'], data['Low'], data['Close'], window=14)

# Calcular el indicador WaveTrend de Lazy Bear
n1 = 10
n2 = 21
data['hlc3'] = (data['High'] + data['Low'] + data['Close']) / 3
data['esa'] = ta.trend.ema_indicator(data['hlc3'], window=n1)
data['d'] = ta.trend.ema_indicator(abs(data['hlc3'] - data['esa']), window=n1)
data['ci'] = (data['hlc3'] - data['esa']) / (0.015 * data['d'])
data['tci'] = ta.trend.ema_indicator(data['ci'], window=n2)
data['wt1'] = data['tci']
data['wt2'] = data['wt1'].rolling(window=4).mean()

# Definir niveles de sobrecompra y sobreventa
overbought_level = 60
oversold_level = -60

# Generar señales basadas en alta volatilidad y sobrecompra/sobreventa
data['Signal'] = np.where(
    (data['ADX'] > 25) & (data['wt1'] < oversold_level), 'Compra',
    np.where(
        (data['ADX'] > 25) & (data['wt1'] > overbought_level), 'Venta',
        'Neutral'
    )
)

# Visualizar señales en el gráfico
plt.figure(figsize=(14, 7))
plt.plot(data.index, data['Close'], label='Precio de Cierre')
plt.scatter(data.index[data['Signal'] == 'Compra'], data['Close'][data['Signal'] == 'Compra'], label='Compra', marker='^', color='g')
plt.scatter(data.index[data['Signal'] == 'Venta'], data['Close'][data['Signal'] == 'Venta'], label='Venta', marker='v', color='r')
plt.legend()
plt.show()

# Mostrar las últimas 30 señales encontradas
print(data[['Close', 'ADX', 'wt1', 'Signal']].tail(30))
