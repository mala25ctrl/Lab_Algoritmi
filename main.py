import timeit
from typing import cast
import numpy as np

from plots import generate_all_plots
from trees.avl_tree import AVLTree
from trees.binary_search_tree import BinarySearchTree
from trees.red_black_tree import RedBlackTree


def generate_random(n: int) -> list[int]:
    """
    Genera una lista di n numeri interi casuali univoci
    Args:
        n: il numero di interi da generare
    Returns: una lista di n numeri interi casuali univoci
    """
    np.random.seed(n)
    numbers = np.random.randint(0, n * 10, size=n)
    return cast(np.ndarray, numbers).tolist()


def generate_sorted(n: int) -> list[int]:
    """
    Genera una lista di n chiavi in ordine crescente
    Args:
        n: numero di chiavi da generare
    Returns: lista di n interi in ordine crescente
    """
    return list(range(n))


def generated_almost_sorted(n: int) -> list[int]:
    """
    Genera una lista di n chiavi quasi ordinate (scambia il 5% delle coppie)
    Args:
        n: numero di chiavi da generare
    Returns: lista di n interi quasi ordinati
    """
    np.random.seed(n)
    keys = list(range(n))
    num_swap = max(1, n // 20)  # Scambia almeno 1 coppia o il 5% delle coppie
    for _ in range(num_swap):
        i, j = np.random.randint(0, n, 2)
        keys[i], keys[j] = keys[j], keys[i]  # Scambia le chiavi
    return keys


def measure_insert(TreeClass, keys: list[int], number: int = 5) -> float:
    """
    Misura il tempo di inserimento di una lista di chiavi nell'albero
    Args:
        TreeClass: l'albero di chiavi da inserire
        number: numero di ripetizioni per ottenere una media più stabile
        keys: la lista di chiavi da inserire
    Returns: tempo totale di inserimento in secondi
    """

    def insert_all():
        tree = TreeClass()
        for key in keys:
            tree.insert(key)

    return timeit.timeit(insert_all, number=number) / number


def measure_search(tree, keys: list[int], number: int = 5) -> float:
    """
    Misura il tempo medio di ricerca di una lista di chiavi nell'albero
    Args:
        number: numero di ripetizioni
        tree: l'albero in cui cercare le chiavi
        keys: la lista di chiavi da cercare
    Returns: tempo medio di ricerca per chiave in secondi
    """

    def search_all():
        for key in keys:
            tree.search(key)

    total_time = timeit.timeit(search_all, number=number) / number
    return total_time / len(keys)


def run_experiments(sizes: list[int]) -> dict:
    """
    Esegue gli esperimenti di inserimento e ricerca per i tre alberi
    Args:
        sizes: lista di dimensioni n da testare
    Returns: dizionario con i risultati degli esperimenti
    """
    generators = {
        "random": generate_random,
        "sorted": generate_sorted,
        "almost_sorted": generated_almost_sorted
    }

    trees = {
        "BST": BinarySearchTree,
        "AVL": AVLTree,
        "RBT": RedBlackTree
    }

    results = {
        scenario: {
            tree_name: {
                "insert_times": [],
                "search_times": [],
                "heights": []
            }
            for tree_name in trees
        }
        for scenario in generators
    }

    for scenario, generator in generators.items():
        print(f"Scenario: {scenario}")
        for n in sizes:
            print(f"n: {n}")
            keys = generator(n)
            for tree_name, TreeClass in trees.items():
                # Inserimento
                insert_time = measure_insert(TreeClass, keys)
                results[scenario][tree_name]["insert_times"].append(insert_time)

                # Costruiamo l'albero per altezza e ricerca
                tree = TreeClass()
                for key in keys:
                    tree.insert(key)

                # Altezza dopo inserimento
                results[scenario][tree_name]["heights"].append(tree.get_height())

                # Ricerca
                search_time = measure_search(tree, keys)
                results[scenario][tree_name]["search_times"].append(search_time)
    return results


if __name__ == '__main__':
    sizes = [100, 500, 1000, 2000, 5000, 10000]
    results = run_experiments(sizes)
    generate_all_plots(results)
