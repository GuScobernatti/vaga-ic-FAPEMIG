import pandas as pd
import matplotlib.pyplot as plt

# Caminho do arquivo
file_path = "10 - M1IOCA1.csv"  # ajuste se necessário

# O arquivo possui 2 linhas iniciais de metadados
df = pd.read_csv(file_path, skiprows=2, header=None)

# Coluna 0 = tempo
# Coluna 1 = corrente
tempo = pd.to_numeric(df[0], errors="coerce")
corrente = pd.to_numeric(df[1], errors="coerce")

# Remover possíveis valores inválidos
mask = tempo.notna() & corrente.notna()
tempo = tempo[mask]
corrente = corrente[mask]

# Plot
plt.figure()
plt.plot(tempo, corrente)
plt.xlabel("Tempo (s)")
plt.ylabel("Corrente (A)")
plt.title("Corrente vs Tempo")
plt.grid(True)
plt.show()
