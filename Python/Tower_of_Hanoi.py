def towerOfHanoi(numrings, from_pole, to_pole, aux_pole):
    if numrings == 1:
        print('Move ring 1 from', from_pole, 'pole to', to_pole, 'pole')
        return
    towerOfHanoi(numrings - 1, from_pole, aux_pole, to_pole)
    print('Move ring', numrings, 'from', from_pole, 'pole to', to_pole, 'pole')
    towerOfHanoi(numrings - 1, aux_pole, to_pole, from_pole)


numrings = 2
towerOfHanoi(numrings, 'Left', 'Right', 'Middle')
