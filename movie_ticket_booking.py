def available_seats(total_seats, booked_seats):
    return [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]

def book_seat(booked_seats, seat):
    if seat not in booked_seats:
        booked_seats.append(seat)
        return True
    return False

def cancel_seat(booked_seats, seat):
    if seat in booked_seats:
        booked_seats.remove(seat)
        return True
    return False

if __name__ == "__main__":
    total_seats = 10
    booked_seats = [2, 5, 7]
    
    print("Available seats:", available_seats(total_seats, booked_seats))
    
    book_seat(booked_seats, 3)
    print("Booked seats after booking 3:", booked_seats)
    
    cancel_seat(booked_seats, 5)
    print("Booked seats after cancelling 5:", booked_seats)