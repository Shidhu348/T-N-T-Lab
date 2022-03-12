from math import pi


def vol(radius):
    return 4 / 3 * pi * pow(radius, 3)


if __name__ == '__main__':
    rad = int(input("Enter the radius : "))
    print(f"\nVolume of the sphere with radius {rad} is {str(round(vol(rad), 2))}")
