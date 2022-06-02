#!/usr/bin/env python
from bike_taxi import BikeTaxi


def main():
    # Driving with a motorized bike taxi
    biketaxi1 = BikeTaxi(True)
    biketaxi1.drive(15)
    biketaxi1.enter_passengers(2)
    biketaxi1.drive(300)
    biketaxi1.enter_passengers(1)
    biketaxi1.drive(3)
    biketaxi1.repair()
    biketaxi1.enter_passengers(3)
    biketaxi1.exit_passengers(2)
    biketaxi1.drive(250)
    biketaxi1.enter_passengers(2)
    biketaxi1.drive(25)
    biketaxi1.repair()
    biketaxi1.drive(150)
    print("=====")

    # Driving with a manual bike taxi
    biketaxi2 = BikeTaxi(False)
    biketaxi2.drive(25)
    biketaxi2.enter_passengers(1)
    biketaxi2.drive(200)
    biketaxi2.enter_passengers(1)
    biketaxi2.repair()
    biketaxi2.drive(3)
    biketaxi2.enter_passengers(1)
    biketaxi2.exit_passengers(2)
    biketaxi2.drive(100)
    biketaxi2.enter_passengers(2)
    biketaxi2.drive(25)
    biketaxi2.repair()
    biketaxi2.drive(250)


if __name__ == "__main__":
    main()
