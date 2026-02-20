import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

from features_processment import (
    feature1,
    feature2,
    feature3,
    feature4,
    feature5,
    feature6,
    rolling_mean,
)

# Caminho do arquivo
data_folder = "../dados"
csv_files = glob.glob(os.path.join(data_folder, "*.csv"))

if not csv_files:
    print("Nenhum arquivo CSV encontrado na pasta.")

data = []

for csv_file in csv_files:

    try:
        df = pd.read_csv(csv_file, skiprows=2, header=None)

        # Coluna 0 = tempo
        # Coluna 1 = corrente
        tempo = pd.to_numeric(df[0], errors="coerce")
        corrente = pd.to_numeric(df[1], errors="coerce")

        # Remover possíveis valores inválidos
        mask = tempo.notna() & corrente.notna()
        tempo = tempo[mask]
        corrente = corrente[mask]

        rolling_mean_corrente = rolling_mean(corrente, tempo)
        findIndex_f1, f1_time, corrente_f1 = feature1(
            rolling_mean_corrente, tempo, corrente
        )
        findIndex_f6, f6_time, corrente_f6 = feature6(
            rolling_mean_corrente, tempo, corrente
        )
        findIndex_f2, f2_time, corrente_f2 = feature2(
            rolling_mean_corrente, tempo, corrente, findIndex_f1, findIndex_f6
        )
        findIndex_f4, f4_time, corrente_f4 = feature4(
            rolling_mean_corrente, tempo, corrente
        )
        f3_time, corrente_f3 = feature3(
            rolling_mean_corrente, tempo, corrente, findIndex_f2, findIndex_f4
        )
        f5_time, corrente_f5 = feature5(
            rolling_mean_corrente, tempo, corrente, findIndex_f4, findIndex_f6
        )

        data.append(
            {
                "Arquivo": os.path.basename(csv_file),
                "F1_Tempo": f1_time,
                "F1_Corrente": corrente_f1,
                "F2_Tempo": f2_time,
                "F2_Corrente": corrente_f2,
                "F3_Tempo": f3_time,
                "F3_Corrente": corrente_f3,
                "F4_Tempo": f4_time,
                "F4_Corrente": corrente_f4,
                "F5_Tempo": f5_time,
                "F5_Corrente": corrente_f5,
                "F6_Tempo": f6_time,
                "F6_Corrente": corrente_f6,
            }
        )

        # Plot
        plt.figure()
        plt.plot(tempo, corrente)

        plt.plot(
            f1_time, corrente_f1, marker="o", markersize=8, color="blue", label="F1"
        )
        if f2_time is not None:
            plt.plot(
                f2_time,
                corrente_f2,
                marker="o",
                markersize=8,
                color="green",
                label="F2",
            )
        if f3_time is not None:
            plt.plot(
                f3_time, corrente_f3, marker="o", markersize=8, color="cyan", label="F3"
            )
        plt.plot(
            f4_time,
            corrente_f4,
            marker="o",
            markersize=8,
            color="orange",
            label="F4",
        )
        plt.plot(
            f5_time, corrente_f5, marker="o", markersize=8, color="brown", label="F5"
        )
        plt.plot(
            f6_time, corrente_f6, marker="o", markersize=8, color="red", label="F6"
        )

        plt.xlabel("Tempo (s)")
        plt.ylabel("Corrente (A)")
        plt.title("Corrente vs Tempo")
        plt.grid(True)
        plt.legend()

        # plt.show()
        plt.savefig(
            os.path.join(
                "..",
                "graficos",
                "sinais_individuais",
                os.path.basename(csv_file).replace(".csv", ".png"),
            ),
            dpi=300,
            bbox_inches="tight",
        )
        plt.close()

    except Exception as err:
        print(f"Erro ao processar o arquivo {csv_file}: {err}")


df_results = pd.DataFrame(data)

features = ["F1", "F2", "F3", "F4", "F5", "F6"]
data_with_mean_and_std = []

for feature in features:
    # feature_time_col = f"{feature}_Tempo"
    feature_corrente_col = f"{feature}_Corrente"

    # mean_time = df_results[feature_time_col].mean()
    # std_time = df_results[feature_time_col].std()

    mean_corrente = df_results[feature_corrente_col].mean()
    std_corrente = df_results[feature_corrente_col].std()

    data_with_mean_and_std.append(
        {
            "Feature": feature,
            "Mean_Corrente": round(mean_corrente, 2),
            "Std_Corrente": round(std_corrente, 2),
        }
    )

df_results_with_mean_and_std = pd.DataFrame(data_with_mean_and_std)
df_results_with_mean_and_std.to_csv(
    "./resultado.csv", index=False, sep=";", decimal=","
)
print(df_results_with_mean_and_std)

plt.figure(figsize=(10, 6))
for feature in features:
    feature_time_col = f"{feature}_Tempo"
    feature_corrente_col = f"{feature}_Corrente"

    plt.scatter(
        df_results[feature_time_col],
        df_results[feature_corrente_col],
        label=feature,
        s=100,
        alpha=0.7,
    )

plt.xlabel("Tempo (s)")
plt.ylabel("Corrente (A)")
plt.title("Gráfico de Dispersão Geral - Todos os Sinais")
plt.grid(True)
plt.legend()

plt.savefig("../graficos/dispersao/dispersao.png", dpi=300, bbox_inches="tight")
plt.close()
