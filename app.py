from secrets import token_urlsafe

def main():
    print("Hello from flask-api!")
    print(type(token_urlsafe(32)))
    print(token_urlsafe(32))


if __name__ == "__main__":
    main()
