import pandas as pd
import yfinance as yf
from datetime import datetime

# Busca o histórico do dólar
ticker = "BRL=X"

df = yf.download(
    tickers=ticker,
    start='2017-01-01',
    end=datetime.today().strftime('%Y-%m-%d')
)

# 1. Remove o segundo nível do cabeçalho (o "BRL=X")
df.columns = df.columns.droplevel(1)
df.columns.name = None

# === A MÁGICA PARA FICAR NA MESMA LINHA ===
# Transforma o índice 'Date' em uma coluna normal
df_alinhado = df.reset_index()
# ==========================================

print(df_alinhado.head())

# Salva o arquivo CSV perfeitamente alinhado na primeira linha
df_alinhado.to_csv('dolar.csv', index=False) # index=False evita criar uma coluna extra sem nome