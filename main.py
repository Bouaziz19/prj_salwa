import d_input as inp


class Tache:
    def __init__(self, pt):
        self.pt = pt

    def demanderpt(self):
        self.pt = input("entrer pt: ")
        print("tache a pt=" + str(self.pt))


class Cromosome:
    def __init__(self, n_tch):
        et = []
        for ind_tache in range(n_tch):
            pt = inp.list_pt[ind_tache]
            tache = Tache(pt)
            et.append(tache)
        self.lstch = et


def test():
    tache1 = Tache(10)
    print(tache1.pt)
    # tache1.demanderpt()
    s0 = Cromosome(inp.n_tch)
    print(s0.lstch)
    for tch in s0.lstch:
        print(tch.pt)


test()
