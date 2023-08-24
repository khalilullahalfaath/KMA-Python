def trimr(x):
    global Ra, Rb, Nvar

    for ii in range(Nvar):
        x[x[:, ii] < Rb[ii], ii] = Rb[ii]
        x[x[:, ii] > Ra[ii], ii] = Ra[ii]
    return x