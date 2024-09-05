from Caesar_cipher_encoder import caesar_cipher_encoder
from Caesar_cipher_decoder import caesar_cipher_decoder


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


Test_text_6 = "Lorem ipsum 4 dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
Test_text_6_encoded = caesar_cipher_encoder(Test_text_6, 50)
Test_text_6_decoded = caesar_cipher_decoder(Test_text_6_encoded, 50)
print(Test_text_6_encoded)
print(Test_text_6_decoded)
