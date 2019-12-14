def sample():
    try:
        return 10
    except:
        return 20
    finally:
        return 30

print(sample())
