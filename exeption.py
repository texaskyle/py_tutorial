def division():
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        results = numerator / denominator

    except ZeroDivisionError:
        print("cannot divide a number by zero")
    except TypeError:
        print("enter only integers")
    except ValueError:
        print("Input only numbers not strings")
    except Exception:
        print("Something went wrong!!")
    else:
        return results
    finally:
        print("This will always execute")


print(division())
