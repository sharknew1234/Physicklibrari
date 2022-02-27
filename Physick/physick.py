class physick:
    def phys(x, y, z):
        d = x - y
        s = d / z
        print(s)

    x = float(input('Enter a larger dimension:'))
    y = float(input('Smaller Larger Dimension:'))
    z = float(input('Enter the division value:'))

    phys(x, y, z)