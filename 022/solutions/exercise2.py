cars = [
  {
    "Dimensions": {
      "Height": 140,
      "Length": 143,
      "Width": 202
    },
    "Engine Information": {
      "Driveline": "All-wheel drive",
      "Engine Type": "Audi 3.2L 6 cylinder 250hp 236ft-lbs",
      "Hybrid": True,
      "Number of Forward Gears": 6,
      "Transmission": "6 Speed Automatic Select Shift",
      "Engine Statistics": {
        "Horsepower": 250,
        "Torque": 236
      }
    },
    "Fuel Information": {
      "City mpg": 18,
      "Fuel Type": "Gasoline",
      "Highway mpg": 25
    },
    "Identification": {
      "Classification": "Automatic transmission",
      "ID": "2009 Audi A3 3.2",
      "Make": "Audi",
      "Model Year": "2009 Audi A3",
      "Year": 2009
    }
  },
  {
    "Dimensions": {
      "Height": 140,
      "Length": 143,
      "Width": 202
    },
    "Engine Information": {
      "Driveline": "All-wheel drive",
      "Engine Type": "Audi 3.2L 6 cylinder 250hp 236ft-lbs",
      "Hybrid": True,
      "Number of Forward Gears": 6,
      "Transmission": "6 Speed Automatic Select Shift",
      "Engine Statistics": {
        "Horsepower": 250,
        "Torque": 236
      }
    },
    "Fuel Information": {
      "City mpg": 23,
      "Fuel Type": "Gasoline",
      "Highway mpg": 25
    },
    "Identification": {
      "Classification": "Automatic transmission",
      "ID": "2009 Mercedes A3 3.2",
      "Make": "Audi",
      "Model Year": "2009 Audi A3",
      "Year": 2009
    }
  },
]


def get_car_by_name(name):
    result = []

    for car in cars:
        if car["Identification"]["ID"].find(name) > -1:
            result.append(car)

    return result
