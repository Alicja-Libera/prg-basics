class TaxiRide:
    def __init__(self, rate_per_km,):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km
    
    def print_receipt(self) :
        print(f'The distance is: {self.distance}')
        print(f'The rate is: {self.rate_per_km}')
        print(f'The total price is: {self.fare}')
    


def main():
    taxi1= TaxiRide(rate_per_km=4) 
    taxi2= TaxiRide(rate_per_km=5)

    taxi1.calculate_fare(100)
    taxi2.calculate_fare(200)

    print('The receipt from Taxi 1 is :')
    taxi1.print_receipt()
    print('The receipt from Taxi 2 is :')
    taxi2.print_receipt()

if __name__ == "__main__":
    main()

