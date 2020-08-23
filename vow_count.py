def vow_c(slog):
    vow = 0
    for symb in slog:
        if symb.isalpha():
            if symb.lower() in 'уеыаоэяи': #если есть согласная
                vow += 1
    return (vow)
    