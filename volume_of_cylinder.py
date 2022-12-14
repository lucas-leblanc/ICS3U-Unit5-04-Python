#!/usr/bin/env python3

# Created by: Lucas LeBlanc
# Created on: Nov 2022
# This program finds the volume of a cylinder

import math


def cylinder_volume_calculation(radius, height):
    # This function calculates the volume of the cylinder

    volume = math.pi * radius**2 * height

    return volume


def main():
    # This function gets the radius and height from the user

    radius_from_user = input("Enter the radius of the cylinder (cm): ")
    height_from_user = input("Enter the height of the cylinder (cm): ")

    try:
        radius_from_user = int(radius_from_user)
        height_from_user = int(height_from_user)
        # Call function
        final_volume = cylinder_volume_calculation(radius_from_user, height_from_user)
        print(
            "\nThe volume of a cylinder with the radius of {0} cm and the height of {1} cm is {2} cm³.".format(
                radius_from_user, height_from_user, final_volume
            )
        )
    except Exception:
        print("\nInvalid Input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
