import logging, time, random

logging.basicConfig(filename="http.log", level=logging.INFO)
logger = logging.getLogger("http")

class AuthenticationError(Exception):
    pass

class FailedRequest(Exception):
    pass

class TooManyRequests(Exception):
    pass

class User:

    def __init__(self, login, role):
        self._login = login
        self._role = role

    @property
    def login(self):
        return self._login

    @property
    def role(self):
        return self._role

    def __str__(self):
        return f"User: {self.login}, role: {self.role}"

class Request:

    def __init__(self, path, user = None):

        self._path = path
        self._user = user

    @property
    def path(self):
        return self._path

    @property
    def user(self):
        return self._user

    def __str__(self):
        return f"Path: {self.path}, \n {str(self.user)}"

############# Exercise 1 ####################
def logging_decorator(func):
    def inner(request, *args, **kwargs):
        logger.info(f"Starting function call: {request}")
        start = time.time()
        result = func(request, *args, **kwargs)
        duration = time.time() - start
        logger.info(f"End of function call: {request}, duration: {duration}s")
        return result
    return inner

############# Exercise 2 ####################
def authentication_decorator(required_role = None):
    def outer(func):
        def inner(request, *args, **kwargs):
            if request.user is None:
                raise AuthenticationError("No user provided in the request.")
            if required_role is not None:
                if request.user.role != required_role and request.user.role != "admin":
                    raise AuthenticationError(f"Unauthorized request. Required role: '{required_role}'.")
            return func(request, *args, **kwargs)
        return inner
    return outer

############# Exercise 3 ####################
def retry_decorator(max_attempts):
    def outer(func):
        def inner(*args, **kwargs):
            for counter in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if counter < max_attempts - 1:
                        time.sleep(0.5)
                    else:
                        raise FailedRequest(f"Exceeded maximum number of attempts: {max_attempts}.")
        return inner
    return outer

############# Exercise 4 ####################
def antispam_decorator(limit = 5):
    def outer(cls_):
        class InnerClass(cls_):
            _counters = {}

            def _check_limit(self, request):
                login = request.user.login if request.user else "guest"
                self._counters[login] = self._counters.get(login, 0) + 1
                return self._counters[login] <= limit

        for name in dir(cls_):
            if name.startswith("_"):
                continue
            el = getattr(cls_, name)
            if callable(el):
                def wrapper(wrapped_method):
                    def method(self, request, *args, **kwargs):
                        if not self._check_limit(request):
                            raise TooManyRequests("Exceeded request limit.")
                        return wrapped_method(self, request, *args, **kwargs)
                    return method
                setattr(InnerClass, name, wrapper(el))

        return InnerClass
    return outer


@antispam_decorator()
class Forum:

    def __init__(self):
        self._threads = ["a", "b", "c"]

    def _stats(self):
        print(self._threads)

    def open_thread(self, request):
        print(f"new thread, request: {request}")

    def add_reply(self, request):
        print(f"new reply, request: {request}")

if __name__ == "__main__":

    user = User("jan", "user")
    admin = User("ela", "admin")

    r_user = Request("/my_profile", user)
    r_admin = Request("/admin_panel", admin)
    r_guest = Request("/home")

    def process_request(request):
        time.sleep(random.uniform(0.01, 0.5))
        return "result"

    ##########################################

    print()
    print()

    @logging_decorator
    def test_logging(request):
        return process_request(request)

    test_logging(r_user)
    test_logging(r_admin)
    test_logging(r_guest)

    ##########################################

    print()
    print()

    @authentication_decorator("user")
    def test_authentication(request):
        return process_request(request)

    try:
        test_authentication(r_user)
    except:
        print("This shouldn't happen.")
    else:
        print("Authorization went fine.")

    try:
        test_authentication(r_admin)
    except:
        print("This shouldn't happen.")
    else:
        print("Authorization went fine.")

    try:
        test_authentication(r_guest)
    except:
        print("Unauthorized login caught.")


    ##########################################

    print()
    print()

    counter = [1]
    @retry_decorator(5)
    def test_retry(request, counter = counter):
        if counter[0] > 3:
            print(f"Succeeded on attempt {counter[0]}")
        else:
            print(f"Failed, attempt {counter[0]}")
            counter[0] += 1
            raise

    test_retry(r_user)

    #########################################

    print()
    print()

    def test_antispam():

        forum = Forum()

        counting_attempts = 0

        for i in range(10):

            if i % 2 == 0:

                counting_attempts += 1

                try:
                    if random.choice([True, False]):
                        forum.open_thread(r_user)
                    else:
                        forum.add_reply(r_user)
                except:
                    print(f"Antispam activated, counting attempts: {counting_attempts}, total: {i+1}")
                else:
                    print(f"Request executed, counting attempts: {counting_attempts}, total: {i+1}")

            else:
                # shouldn't count
                forum._stats()

    test_antispam()
