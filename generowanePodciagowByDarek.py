subsequences = []
def wygeneruj_wszystkie_podciagi(ciag, podciag):
    if ciag:
        wygeneruj_wszystkie_podciagi(ciag[1:], podciag.copy())
        wygeneruj_wszystkie_podciagi(ciag[1:], [*podciag, ciag[0]])
    else:
        subsequences.append(podciag)


input_data = [1, 2, 3, 4]
wygeneruj_wszystkie_podciagi(input_data, [])
print(sorted(subsequences))
