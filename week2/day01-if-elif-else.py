# Lesson
# if/elif/else lets a script branch based on conditions. Python uses indentation (not braces) to define blocks — this is not optional, it's the syntax.

# Challenge — write this as a script
# Write a script that takes an HTTP status code (int) and prints 'Success', 'Redirect', 'Client Error', or 'Server Error' depending on the range it falls in (2xx/3xx/4xx/5xx).

HTTP_code       = int(input('Enter HTTP status code: '))
success_status  = 200
redirect_status = 300
client_error    = 400
server_error    = 500

if HTTP_code >= 200 and HTTP_code < 300:
    print("Success.")
elif HTTP_code >= 300 and HTTP_code < 400:
    print("Redirect.")
elif HTTP_code >= 400 and HTTP_code < 500:
    print("Client Error.")
elif HTTP_code >= 500 and HTTP_code < 600:
    print("Server Error.")
else:
    print("Invalid code")
