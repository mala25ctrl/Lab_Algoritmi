import os
import matplotlib.pyplot as plt

SIZES = [100, 500]
SCENARIOS = ["random", "sorted", "almost_sorted"]
SCENARIO_LABELS = {
    "random": "Casuale",
    "sorted": "Ordinato",
    "almost_sorted": "Quasi ordinato",
}
TREES = ["BST", "AVL", "RBT"]
COLORS = {"BST": "blue", "AVL": "green", "RBT": "red"}
OUTPUT_DIR = "output"

def set_output_dir() -> None:
    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

def plots_heights(results: dict) -> None:
    """Genera i grafici dell'altezza al variare di n per ogni scenario"""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle("Altezza dell'albero al variare di n")

    for ax, scenario in zip(axes, SCENARIOS):
        for tree_name in TREES:
            heights = results[scenario][tree_name]["heights"]
            ax.plot(SIZES, heights, color=COLORS[tree_name], label=tree_name, marker="o")

        ax.set_title(f"Input: {SCENARIO_LABELS[scenario]}")
        ax.set_xlabel("n")
        ax.set_ylabel("Altezza")
        ax.legend()
        ax.grid(True)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "heights.png"))
    plt.close()

def plot_insert_times(results: dict) -> None:
    """Genera i grafici del tempo di inserimento al variare di n per ogni scenario"""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle("Tempo di inserimento al variare di n")

    for ax, scenario in zip(axes, SCENARIOS):
        for tree_name in TREES:
            times = results[scenario][tree_name]["insert_times"]
            ax.plot(SIZES, times, color=COLORS[tree_name], label=tree_name, marker="o")

        ax.set_title(f"Input: {SCENARIO_LABELS[scenario]}")
        ax.set_xlabel("n")
        ax.set_ylabel("Tempo (s)")
        ax.legend()
        ax.grid(True)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "insert_times.png"))
    plt.close()

def plot_search_times(results: dict) -> None:
    """Genera i grafici del tempo di ricerca al variare di n per ogni scenario"""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle("Tempo di ricerca al variare di n")

    for ax, scenario in zip(axes, SCENARIOS):
        for tree_name in TREES:
            times = results[scenario][tree_name]["search_times"]
            ax.plot(SIZES, times, color=COLORS[tree_name], label=tree_name, marker="o")

        ax.set_title(f"Input: {SCENARIO_LABELS[scenario]}")
        ax.set_xlabel("n")
        ax.set_ylabel("Tempo medio per chiave (s)")
        ax.legend()
        ax.grid(True)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "search_times.png"))
    plt.close()


def generate_all_plots(results: dict) -> None:
    set_output_dir()
    plots_heights(results)
    plot_insert_times(results)
    plot_search_times(results)
    print(f"Grafici salvati in {OUTPUT_DIR}/")