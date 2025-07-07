def solution(phone_book):
    phone_book.sort()  # Sort the phone book

    for i in range(len(phone_book) - 1):
        # Check if the current number is a prefix of the next number
        if phone_book[i+1].startswith(phone_book[i]):
            return False

    return True