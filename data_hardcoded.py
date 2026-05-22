def get_problem_data():
    """
    Zwraca dane problemu optymalizacji patroli.

    Returns:
        tuple: (num_settlements, num_patrols, populations, adjacency_list)
    """
    num_settlements = 24
    num_patrols = 15

    # Populacje osiedli
    populations = {
        1: 25,
        2: 18,
        3: 32,
        4: 20,
        5: 35,
        6: 45,
        7: 25,
        8: 50,
        9: 34,
        10: 15,
        11: 12,
        12: 29,
        13: 24,
        14: 11,
        15: 10,
        16: 8,
        17: 9,
        18: 12,
        19: 19,
        20: 7,
        21: 10,
        22: 5,
        23: 8,
        24: 7
    }

    # Graf sąsiedztwa - lista sąsiadów dla każdego osiedla
    adjacency_list = {
        1: [2, 3, 6, 7],
        2: [1, 3, 4, 5, 6, 21],
        3: [1, 2, 8, 9, 15, 21],
        4: [2, 5, 10, 12, 21, 22],
        5: [2, 4, 6, 10, 19],
        6: [1, 2, 5, 7, 13, 19, 20],
        7: [1, 6, 9, 13, 14],
        8: [3, 9, 11, 15, 16],
        9: [3, 7, 8, 11, 14],
        10: [4, 5, 12, 17, 18, 19],
        11: [8, 9, 14, 16, 24],
        12: [4, 10, 17, 22, 23],
        13: [6, 7, 20, 14],
        14: [7, 9, 11, 13, 24],
        15: [3, 8, 16, 21],
        16: [8, 11, 15],
        17: [10, 12, 18, 23],
        18: [10, 17, 19],
        19: [5, 6, 10, 18, 20],
        20: [6, 13, 19],
        21: [2, 3, 4, 15, 22],
        22: [4, 12, 21, 23],
        23: [12, 17, 22],
        24: [11, 14]
    }

    return num_settlements, num_patrols, populations, adjacency_list


if __name__ == '__main__':
    # Test danych
    num_settlements, num_patrols, populations, adjacency_list = get_problem_data()

    print(f"Liczba osiedli: {num_settlements}")
    print(f"Liczba patroli: {num_patrols}")
    print(f"\nPrzykładowe populacje:")
    for i in range(1, 6):
        print(f"  Osiedle {i}: {populations[i]} mieszkańców")
    print(f"\nPrzykładowe sąsiedztwa:")
    for i in range(1, 6):
        print(f"  Osiedle {i} sąsiaduje z: {adjacency_list[i]}")
