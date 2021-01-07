#!/usr/bin/env python3

# Created by: Roman Cernetchi
# Created on: January 2021
# This program calculates the volume of a cylinder

import math


def calculate_volume(radius, height):
    # calculates the volume of a cylinder

    volume = math.pi*radius**2 * height
    float_volume = "{:.2f}".format(volume)

    return float_volume


def main():
    # input the radius and height
    while True:
        try:
            radius_from_user = int(input("Enter the radius of the cylinder"
                                         "(cm): "))
            height_from_user = int(input("Enter the height of the cylinder"
                                         "(cm): "))
            print("")

            # calls function
            float_volume = calculate_volume(radius_from_user,
                                            height_from_user)

            if radius_from_user <= 0 or height_from_user <= 0:
                print("Invalid input")
            else:
                # output
                print("The perimeter is: {0} cm²".format(float_volume))
                break

        except ValueError:
            print("This was not a number")


if __name__ == "__main__":
    main()
