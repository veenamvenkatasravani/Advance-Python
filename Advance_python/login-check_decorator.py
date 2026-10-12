def login_required(function):
    def wrapper(is_logged_in):
        if not is_logged_in:
            print("Please log in first")
            return

        return function(is_logged_in)

    return wrapper


@login_required
def dashboard(is_logged_in):
    print("Welcome to your dashboard!")


dashboard(False)
dashboard(True)