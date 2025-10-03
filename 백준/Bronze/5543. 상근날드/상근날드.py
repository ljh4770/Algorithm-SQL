if __name__ == "__main__":
    burgers = [int(input()) for _ in range(3)]
    drinks = [int(input()) for _ in range(2)]

    print(min(burgers) + min(drinks) - 50)