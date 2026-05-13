def bubble_sort(liste):

    for i in range(len(liste)):

        for j in range(len(liste) - 1 - i):

            if liste[j] > liste[j + 1]:

                liste[j], liste[j + 1] = liste[j + 1], liste[j]

    return liste


if __name__ == "__main__":
    a = [8, 5, 2, 7]
    print(bubble_sort(a))