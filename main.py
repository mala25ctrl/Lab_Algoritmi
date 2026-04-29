import timeit
from typing import cast
import numpy as np
from plots import generate_all_plots
from trees.avl_tree import AVLTree
from trees.binary_search_tree import BinarySearchTree
from trees.red_black_tree import RedBlackTree


def generate_random(n: int) -> list[int]:
    """
    Genera una lista di n numeri interi casuali.
    Args:
        n: il numero di interi da generare
    Returns:
        una lista di n numeri interi casuali
    """
    np.random.seed(n) #stesso seed per avere sempre gli stessi numeri per ogni n
    numbers = np.random.randint(0, n * 10, size=n)
    return cast(np.ndarray, numbers).tolist()


def generate_sorted(n: int) -> list[int]:
    """
    Genera una lista di n interi consecutivi in ordine crescente (da 0 a n-1).
    Args:
        n: numero di chiavi da generare
    Returns: lista di n interi in ordine crescente
    """
    return list(range(n))


def generate_almost_sorted(n: int) -> list[int]:
    """
    Genera una lista di n chiavi quasi ordinate effettuando circa il 5% di scambi casuali.
    Args:
        n: numero di chiavi da generare
    Returns:
        lista di n interi quasi ordinati
    """
    np.random.seed(n) #stesso seed per avere sempre gli stessi numeri per ogni n
    keys = list(range(n))
    num_swap = max(1, n // 20)  # Scambia almeno 1 coppia o il 5% delle coppie
    for _ in range(num_swap):
        i, j = np.random.randint(0, n, 2)
        keys[i], keys[j] = keys[j], keys[i]  # Scambia le chiavi
    return keys


def measure_insert(TreeClass, keys: list[int], number: int = 50) -> float:
    """
    Misura il tempo medio necessario per inserire una lista di chiavi in un albero.

    Esegue l'inserimento completo delle chiavi in un nuovo albero per un certo
    numero di ripetizioni (default 50) e calcola il tempo medio dividendo il
    tempo totale restituito da timeit per il numero di esecuzioni
    Args:
        TreeClass: la classe dell'albero in cui inserire le chiavi
        keys: la lista di chiavi da inserire
        number: numero di ripetizioni per ottenere una media più stabile
    Returns:
        tempo medio (in secondi) per inserire tutte le chiavi
    """

    def insert_all():
        tree = TreeClass()
        for key in keys:
            tree.insert(key)

    # Misura il tempo medio degli inserimenti nell'albero in oggetto
    return timeit.timeit(insert_all, number=number) / number


def measure_search(tree, keys: list[int], number: int = 50) -> float:
    """
    Misura il tempo medio necessario per cercare una chiave in un albero.

    Esegue la ricerca di tutte le chiavi per un certo numero di ripetizioni e
    restituisce il tempo medio per singola chiave cercata.
    Args:
        tree: l'albero in cui cercare le chiavi
        keys: la lista di chiavi da cercare
        number: numero di ripetizioni
    Returns:
        tempo medio (in secondi) per cercare una singola chiave nell'albero
    """
    def search_all():
        for key in keys:
            tree.search(key)

    return timeit.timeit(search_all, number=number) / number / len(keys)


def run_experiments(sizes: list[int]) -> dict:
    """
    Esegue gli esperimenti di inserimento, ricerca e altezza per tre alberi
    (BST, AVL e Red-Black Tree) su diversi scenari di input.

    Args:
        sizes: lista di dimensioni n da testare
        
    Returns: 
        dizionario contenente, per ogni scenario e per ogni albero:
        - tempi medi di inserimento
        - tempi medi di ricerca
        - altezze finali dell'albero
    """
    generators = {
        "random": generate_random,
        "sorted": generate_sorted,
        "almost_sorted": generate_almost_sorted
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

    # Eseguiamo gli esperimenti per ogni scenario, dimensione e albero
    for scenario, generator in generators.items():
        print(f"Scenario: {scenario}")

        # Cicliamo sulle dimensioni da testare
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
    sizes = [1, 10, 50, 100, 200, 300, 400, 500, 750, 1000]
    results = run_experiments(sizes)
    generate_all_plots(results)
