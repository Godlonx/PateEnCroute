
def f_test(mob):
    mobs = {1:[1, 2], 2:[1, 3], 3:[5, 8]}
    while True:
        x = int(input("Wave"))
        if x == 0:
            return "fin"

        nb_gold = 50
        for i in range(x):
            nb_mob = 11+i
            pv_mob = mobs[mob][0]+(i//4)
            for i in range(nb_mob+1):
                nb_gold += mobs[mob][1]
            print(nb_mob, pv_mob, nb_gold)