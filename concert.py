class Ticket:
    def __init__(self, concert):
        self.concert = concert

    def get_total_price(self):
        return self.concert.base_price

    def __str__(self):
        return f"General ticket for {self.concert.artist} - {self.get_total_price()} €"

class StandsTicket(Ticket):
    def __init__(self, concert, seat):
        super().__init__(concert)
        self.seat = seat

    def get_total_price(self):
        return self.concert.base_price

    def __str__(self):
        return f"Stands ticket for {self.concert.artist} - {self.get_total_price()} €"

class FloorTicket(Ticket):
    def __init__(self, concert, standing):
        super().__init__(concert)
        self.standing = standing

    def get_total_price(self):
        return self.concert.base_price * 1.10

    def __str__(self):
        return f"Floor ticket for {self.concert.artist} - {self.get_total_price()} €"

class VIPTicket(Ticket):
    def __init__(self, concert, includes_drink):
        super().__init__(concert)
        self.includes_drink = includes_drink

    def get_total_price(self):
        if self.includes_drink:
            return self.concert.base_price * 1.20
        return self.concert.base_price * 1.15

    def __str__(self):
        return f"VIP ticket for {self.concert.artist} - {self.get_total_price()} €"

class Concert:
    def __init__(self, artist, city, base_price, max_capacity, active=True):
        self.artist = artist
        self.city = city
        self.base_price = base_price
        self.max_capacity = max_capacity
        self.tickets_sold = []
        self.active = active

    def calculate_revenue(self):
        total = 0.0
        for ticket in self.tickets_sold:
            total += ticket.get_total_price()
        return total

    def calculate_average_price(self):
        counter = 0
        for ticket in self.tickets_sold:
            counter += 1
        if counter == 0:
            return 0.0
        return self.calculate_revenue() / counter

    def tickets_available(self):
        counter = 0
        for ticket in self.tickets_sold:
            counter += 1
        return counter < self.max_capacity

    def __str__(self):
        return f"Concert of {self.artist} in {self.city}"

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.purchased_tickets = []
        self.attended_concerts = set()
        self.ratings = {}

    def buy_ticket(self, concert, ticket_type):
        if not concert.active:
            raise Exception(f"The concert of {concert.artist} is not active")
        if concert in self.attended_concerts:
            raise Exception(f"{self.name} has already attended the concert of {concert.artist}")
        if not concert.tickets_available():
            raise Exception(f"No tickets available for the concert of {concert.artist}")

        if ticket_type == "general":
            ticket = Ticket(concert)
        elif ticket_type == "stands":
            ticket = StandsTicket(concert, "1A")
        elif ticket_type == "floor":
            ticket = FloorTicket(concert, True)
        elif ticket_type == "vip":
            ticket = VIPTicket(concert, True)
        else:
            raise Exception(f"Unknown ticket type: {ticket_type}")

        concert.tickets_sold.append(ticket)
        self.purchased_tickets.append(ticket)
        self.attended_concerts.add(concert)

    def rate(self, concert, rating):
        if concert not in self.attended_concerts:
            raise Exception(f"{self.name} has not attended the concert of {concert.artist}")
        if rating < 0 or rating > 10:
            raise Exception("The rating must be between 0 and 10")
        self.ratings[concert] = rating

    def __str__(self):
        counter = 0
        for concert in self.attended_concerts:
            counter += 1
        return f"{self.name} (has attended {counter})"