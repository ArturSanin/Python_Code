from to_morse_code import to_morse_code


test_string_1 = "HALLO"
test_string_2 = "hallo"
test_string_3 = "Hey, where is my car?"
test_string_4 = "SOS"
test_string_5 = ("Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut"
                 " labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores"
                 " et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
                 " Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut "
                 "labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores "
                 "et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.")


print(to_morse_code(test_string_1))
print(to_morse_code(test_string_2))
print(to_morse_code(test_string_3))
print(to_morse_code(test_string_4))
print(to_morse_code(test_string_5))
