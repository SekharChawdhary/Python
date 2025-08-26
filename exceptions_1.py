def register_user(username, age, email):
    try:
        if len(username) < 6:
            raise ValueError("Username must be 6 letters or above")
        if age < 1 or age > 100:
            raise ValueError("Age must be 1-100")
        if '@' not in email or '.' not in email:
            raise ValueError("Invalid email")
    except ValueError as e:
        print(f"Registration failed:{e}")
    else:
        print(f"{username}Registration success:")
register_user('Sekhar ',25," sekharabboori@gmail.com")
        