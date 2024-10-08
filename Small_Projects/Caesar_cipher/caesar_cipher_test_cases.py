from caesar_cipher_encoder import caesar_cipher_encoder
from caesar_cipher_decoder import caesar_cipher_decoder
from nested_caesar_cipher_encoder import nested_caesar_cipher_encoder
from nested_caesar_cipher_decoder import nested_caesar_cipher_decoder

Test_text_1 = "Lorem ipsum dolor sit amet"
Test_text_1_encoded = caesar_cipher_encoder(Test_text_1, 25)
Test_text_1_decoded = caesar_cipher_decoder(Test_text_1_encoded, 25)
print(Test_text_1_encoded)
print(Test_text_1_decoded)


Test_text_2 = "sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat"
Test_text_2_encoded = caesar_cipher_encoder(Test_text_2, 14)
Test_text_2_decoded = caesar_cipher_decoder(Test_text_2_encoded, 14)
print(Test_text_2_encoded)
print(Test_text_2_decoded)


Test_text_3 = "At vero eos et accusam et justo duo dolores et ea rebum"
Test_text_3_encoded = caesar_cipher_encoder(Test_text_3, 10)
Test_text_3_decoded = caesar_cipher_decoder(Test_text_3_encoded, 10)
print(Test_text_3_encoded)
print(Test_text_3_decoded)


Test_text_4 = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
Test_text_4_encoded = caesar_cipher_encoder(Test_text_4, 50)
Test_text_4_decoded = caesar_cipher_decoder(Test_text_4_encoded, 50)
print(Test_text_4_encoded)
print(Test_text_4_decoded)


Test_text_5 = "Hallo? What! Nothing, ; . :"
Test_text_5_encoded = caesar_cipher_encoder(Test_text_5, 50)
Test_text_5_decoded = caesar_cipher_decoder(Test_text_5_encoded, 50)
print(Test_text_5_encoded)
print(Test_text_5_decoded)


# Test_text_6 = "Lorem ipsum 4 dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
# Test_text_6_encoded = caesar_cipher_encoder(Test_text_6, 50)
# Test_text_6_decoded = caesar_cipher_decoder(Test_text_6_encoded, 50)
# print(Test_text_6_encoded)
# print(Test_text_6_decoded)


Test_text_1_nested_encoded = nested_caesar_cipher_encoder(Test_text_1, [1, 2, 3, 4, 5])
Test_text_1_nested_decoded = nested_caesar_cipher_decoder(Test_text_1_nested_encoded, [1, 2, 3, 4, 5])
print(Test_text_1_nested_encoded)
print(Test_text_1_nested_decoded)


Test_text_2_nested_encoded = nested_caesar_cipher_encoder(Test_text_2, [10, 20, 30, 40, 50])
Test_text_2_nested_decoded = nested_caesar_cipher_decoder(Test_text_2_nested_encoded, [10, 20, 30, 40, 50])
print(Test_text_2_nested_encoded)
print(Test_text_2_nested_decoded)


Test_text_3_nested_encoded = nested_caesar_cipher_encoder(Test_text_3, [-10, -20, -30, -40, -50])
Test_text_3_nested_decoded = nested_caesar_cipher_decoder(Test_text_3_nested_encoded, [-10, -20, -30, -40, -50])
print(Test_text_3_nested_encoded)
print(Test_text_3_nested_decoded)


Test_text_4_nested_encoded = nested_caesar_cipher_encoder(Test_text_4, [5, -10, 15, -20, 25])
Test_text_4_nested_decoded = nested_caesar_cipher_decoder(Test_text_4_nested_encoded, [5, -10, 15, -20, 25])
print(Test_text_4_nested_encoded)
print(Test_text_4_nested_decoded)


Test_text_5_nested_encoded = nested_caesar_cipher_encoder(Test_text_5, [8, 50, 12])
Test_text_5_nested_decoded = nested_caesar_cipher_decoder(Test_text_5_nested_encoded, [8, 50, 12])
print(Test_text_5_nested_encoded)
print(Test_text_5_nested_decoded)


print(Test_text_1_encoded == nested_caesar_cipher_encoder(Test_text_1, [25]))
print(Test_text_2_encoded == nested_caesar_cipher_encoder(Test_text_2, [14]))
print(Test_text_3_encoded == nested_caesar_cipher_encoder(Test_text_3, [10]))
print(Test_text_4_encoded == nested_caesar_cipher_encoder(Test_text_4, [50]))
print(Test_text_5_encoded == nested_caesar_cipher_encoder(Test_text_5, [50]))


print(Test_text_1_decoded == nested_caesar_cipher_decoder(Test_text_1_encoded, [25]))
print(Test_text_2_decoded == nested_caesar_cipher_decoder(Test_text_2_encoded, [14]))
print(Test_text_3_decoded == nested_caesar_cipher_decoder(Test_text_3_encoded, [10]))
print(Test_text_4_decoded == nested_caesar_cipher_decoder(Test_text_4_encoded, [50]))
print(Test_text_5_decoded == nested_caesar_cipher_decoder(Test_text_5_encoded, [50]))
