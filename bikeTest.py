import unittest
from datetime import datetime, timedelta
from main import Rental, Customer


class BikeRentalTest(unittest.TestCase):
    def test_Bike_Rental_diplays_correct_stock(self):
        shop1 = Rental()
        shop2 = Rental(10)
        self.assertEqual(shop1.displaystock(), 0)
        self.assertEqual(shop2.displaystock(), 10)

    def test_rentBikeOnHourlyBasis_for_negative_number_of_bikes(self):
        shop = Rental(10)
        self.assertEqual(shop.rent_bike_on_hourly_basis(-1), None)

    def test_rentBikeOnHourlyBasis_for_zero_number_of_bikes(self):
        shop = Rental(10)
        self.assertEqual(shop.rent_bike_on_hourly_basis(0), None)

    def test_rentBikeOnHourlyBasis_for_valid_positive_number_of_bikes(self):
        shop = Rental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.rent_bike_on_hourly_basis(2).hour, hour)

    def test_rentBikeOnHourlyBasis_for_invalid_positive_number_of_bikes(self):
        shop = Rental(10)
        self.assertEqual(shop.rent_bike_on_hourly_basis(11), None)

    def test_rentBikeOnDailyBasis_for_negative_number_of_bikes(self):
        shop = Rental(10)
        self.assertEqual(shop.rent_bike_on_hourly_basis(-1), None)

    def test_rentBikeOnDailyBasis_for_zero_number_of_bikes(self):
        shop = Rental(10)
        self.assertEqual(shop.rent_bike_on_hourly_basis(0), None)

    def test_rentBikeOnDailyBasis_for_valid_positive_number_of_bikes(self):
        shop = Rental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.rent_bike_on_hourly_basis(2).hour, hour)

    def test_rentBikeOnDailyBasis_for_invalid_positive_number_of_bikes(self):
        shop = Rental(10)
        self.assertEqual(shop.rent_bike_on_hourly_basis(11), None)

    def test_rentBikeOnWeeklyBasis_for_negative_number_of_bikes(self):
        shop = Rental(10)
        self.assertEqual(shop.rent_bike_on_hourly_basis(-1), None)

    def test_rentBikeOnWeeklyBasis_for_zero_number_of_bikes(self):
        shop = Rental(10)
        self.assertEqual(shop.rent_bike_on_hourly_basis(0), None)

    def test_rentBikeOnWeeklyBasis_for_valid_positive_number_of_bikes(self):
        shop = Rental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.rent_bike_on_hourly_basis(2).hour, hour)

    def test_rentBikeOnWeeklyBasis_for_invalid_positive_number_of_bikes(self):
        shop = Rental(10)
        self.assertEqual(shop.rent_bike_on_hourly_basis(11), None)

    def test_returnBike_for_invalid_rentalTime(self):
        # create a shop and a customer
        shop = Rental(10)
        customer = Customer()
        # let the customer not rent a bike a try to return one.
        request = customer.returnBike()
        self.assertIsNone(shop.return_bike(request))
        # manually check return function with error values
        self.assertIsNone(shop.return_bike((0, 0, 0)))

    def test_returnBike_for_invalid_rentalBasis(self):
        # create a shop and a customer
        shop = Rental(10)
        customer = Customer()

        # create valid rentalTime and bikes
        customer.rentalTime = datetime.now()
        customer.bikes = 3
        # create invalid rentalbasis
        customer.rentalBasis = 7
        request = customer.returnBike()
        self.assertEqual(shop.return_bike(request), 0)

    def test_returnBike_for_invalid_numOfBikes(self):
        # create a shop and a customer
        shop = Rental(10)
        customer = Customer()

        # create valid rentalTime and rentalBasis
        customer.rentalTime = datetime.now()
        customer.rentalBasis = 1
        # create invalid bikes
        customer.bikes = 0
        request = customer.returnBike()
        self.assertIsNone(shop.return_bike(request))

    def test_returnBike_for_valid_credentials(self):
        # create a shop and a various customers
        shop = Rental(50)
        customer1 = Customer()
        customer2 = Customer()
        customer3 = Customer()
        customer4 = Customer()
        customer5 = Customer()
        customer6 = Customer()

        # create valid rentalBasis for each customer
        customer1.rentalBasis = 1  # hourly
        customer2.rentalBasis = 1  # hourly
        customer3.rentalBasis = 2  # daily
        customer4.rentalBasis = 2  # daily
        customer5.rentalBasis = 3  # weekly
        customer6.rentalBasis = 3  # weekly
        # create valid bikes for each customer
        customer1.bikes = 1
        customer2.bikes = 5  # eligible for family discount 30%
        customer3.bikes = 2
        customer4.bikes = 8
        customer5.bikes = 15
        customer6.bikes = 30
        # create past valid rental times for each customer

        customer1.rentalTime = datetime.now() + timedelta(hours=-4)
        customer2.rentalTime = datetime.now() + timedelta(hours=-23)
        customer3.rentalTime = datetime.now() + timedelta(days=-4)
        customer4.rentalTime = datetime.now() + timedelta(days=-13)
        customer5.rentalTime = datetime.now() + timedelta(weeks=-6)
        customer6.rentalTime = datetime.now() + timedelta(weeks=-12)
        # make all customers return their bikes
        request1 = customer1.returnBike()
        request2 = customer2.returnBike()
        request3 = customer3.returnBike()
        request4 = customer4.returnBike()
        request5 = customer5.returnBike()
        request6 = customer6.returnBike()
        # check if all of them get correct bill
        self.assertEqual(shop.return_bike(request1), 20)
        self.assertEqual(shop.return_bike(request2), 402.5)
        self.assertEqual(shop.return_bike(request3), 160)
        self.assertEqual(shop.return_bike(request4), 2080)
        self.assertEqual(shop.return_bike(request5), 5400)
        self.assertEqual(shop.return_bike(request6), 21600)


class CustomerTest(unittest.TestCase):

    def test_return_Bike_with_valid_input(self):
        # create a customer
        customer = Customer()

        # create valid rentalTime, rentalBasis, bikes
        now = datetime.now()
        customer.rentalTime = now
        customer.rentalBasis = 1
        customer.bikes = 4
        self.assertEqual(customer.returnBike(), (now, 1, 4))

    def test_return_Bike_with_invalid_input(self):
        # create a customer
        customer = Customer()

        # create valid rentalBasis and bikes

        customer.rentalBasis = 1
        customer.bikes = 0
        # create invalid rentalTime
        customer.rentalTime = 0
        self.assertEqual(customer.returnBike(), (0, 0, 0))


if __name__ == '__main__':
    unittest.main()