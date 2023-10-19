import calculator

if __name__ == '__main__':
    calc = calculator.Calculator()
    calc.add_car(
        calculator.Car("Fiat 124 Spider", price=29000, fuel_economy=9, service_cost=500, insurance_cost=1000),
    )
    calc.add_car(
        calculator.Car("Mazda MX-5", 30000, 8, 500, 1000),
    )
    calc.add_car(
        calculator.ElectricCar("Fiat 500e", 50000, 500, 100),
    )
    calc.print_cars()
