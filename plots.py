import os
import matplotlib.pyplot as plt

SIZES = [1, 10, 50, 100, 200, 300, 400, 500, 750, 1000]
SCENARIOS = ["random", "sorted", "almost_sorted"]
TREES = ["BST", "AVL", "RBT"]
COLORS = {"BST": "blue", "AVL": "green", "RBT": "red"}
SCENARIO_LABELS = {
    "random": "Casuale",
    "sorted": "Ordinato",
    "almost_sorted": "Quasi ordinato"
}
OUTPUT_DIR = "output"


def setup_output_dir() -> None:
    """
    Crea la cartella di output se non esiste
    """
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)


def plot_metric(results: dict, metric: str, title: str, ylabel: str, filename: str) -> None:
    """
    Genera e salva un grafico per una specifica metrica al variare di n,
    per ogni scenario di input e struttura dati.

    Args:
        results: dizionario con i risultati degli esperimenti.
        metric: chiave della metrica da visualizzare
            ("heights", "insert_times" oppure "search_times").
        title: titolo del grafico.
        ylabel: etichetta dell'asse y.
        filename: nome del file di output.
    """
    fig, axes = plt.subplots(1, len(SCENARIOS), figsize=(5 * len(SCENARIOS), 5))
    fig.suptitle(title)

    if len(SCENARIOS) == 1:
        axes = [axes]

    for ax, scenario in zip(axes, SCENARIOS):
        for tree_name in TREES:
            values = results[scenario][tree_name][metric]
            ax.plot(
                SIZES,
                values,
                label=tree_name,
                color=COLORS[tree_name],
                marker="o"
            )

        ax.set_title(f"Input: {SCENARIO_LABELS[scenario]}")
        ax.set_xlabel("n")
        ax.set_ylabel(ylabel)
        ax.legend()
        ax.grid(True)

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig(os.path.join(OUTPUT_DIR, filename), dpi=300)
    plt.close()


def plot_heights(results: dict) -> None:
    """
    Genera il grafico dell'altezza al variare di n per ogni scenario
    Args:
        results: dizionario con i risultati degli esperimenti
    """
    plot_metric(
        results,
        metric="heights",
        title="Altezza dell'albero al variare di n",
        ylabel="Altezza",
        filename="heights.png"
    )


def plot_insert_times(results: dict) -> None:
    """
    Genera e salva un grafico del tempo di inserimento al variare di n
    per diversi scenari di input.
    Args:
        results: dizionario con i risultati degli esperimenti
    """
    plot_metric(
        results,
        metric="insert_times",
        title="Tempo di inserimento al variare di n",
        ylabel="Tempo (s)",
        filename="insert_times.png"
    )


def plot_search_times(results: dict) -> None:
    """
    Genera e salva un grafico del tempo di ricerca al variare di n
    per diversi scenari di input.
    Args:
        results: dizionario con i risultati degli esperimenti
    """
    plot_metric(
        results,
        metric="search_times",
        title="Tempo di ricerca al variare di n",
        ylabel="Tempo medio per chiave (s)",
        filename="search_times.png"
    )


def plot_table(results: dict, metric: str, title: str, filename: str, fmt: str = "{:.4f}") -> None:
    """
    Genera una tabella con i risultati di una metrica per ogni scenario e struttura
    Args:
        results: dizionario con i risultati degli esperimenti
        metric: chiave della metrica da visualizzare (insert_times, search_times, heights)
        title: titolo della tabella
        filename: nome del file di output
        fmt: formato dei valori numerici
    """
    headers = ["n"] + [f"{SCENARIO_LABELS[s]}\n{t}" for s in SCENARIOS for t in TREES]
    rows = []
    for i, n in enumerate(SIZES):
        row = [str(n)]
        for scenario in SCENARIOS:
            for tree_name in TREES:
                val = results[scenario][tree_name][metric][i]
                row.append(fmt.format(val))
        rows.append(row)

    fig, ax = plt.subplots(figsize=(14, 4))
    ax.axis("off")
    table = ax.table(cellText=rows, colLabels=headers, loc="center", cellLoc="center")
    table.auto_set_column_width(col=list(range(len(headers))))
    table.scale(1, 1.8)

    for cell in table._cells:
        if cell[0] == 0:  # Intestazione
            table[cell].set_facecolor("#c1d6ff")
            table[cell].set_text_props(weight="bold")
        elif cell[0] % 2 == 0:  # Righe pari
            table[cell].set_facecolor("#deebff")

    ax.set_title(title, fontsize=13, fontweight="bold", pad=10)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, filename), dpi=200, bbox_inches="tight")
    plt.close()


def plot_tables(results: dict) -> None:
    """
    Genera e salva le tabelle per le principali metriche:
    tempi di inserimento, tempi di ricerca e altezza degli alberi.

    Args:
        results: dizionario con i risultati degli esperimenti.
    """
    plot_table(results, "insert_times", "Tempi di inserimento (s)", "tabella_inserimento.png")
    plot_table(results, "search_times", "Tempi di ricerca per chiave (s)", "tabella_ricerca.png", fmt="{:.2e}")
    plot_table(results, "heights", "Altezza dell'albero", "tabella_altezza.png", fmt="{:.0f}")


def generate_all_plots(results: dict) -> None:
    """
        Genera e salva tutti i grafici e le tabelle a partire dai risultati
        degli esperimenti.

        Esegue:
            - creazione della directory di output
            - grafici: altezza, tempi di inserimento e ricerca
            - tabelle: inserimento, ricerca e altezza

        Args:
            results: dizionario con i risultati degli esperimenti.
        """
    setup_output_dir()
    plot_heights(results)
    plot_insert_times(results)
    plot_search_times(results)
    plot_tables(results)
    print(f"Grafici e tabelle salvati in '{OUTPUT_DIR}/'")
