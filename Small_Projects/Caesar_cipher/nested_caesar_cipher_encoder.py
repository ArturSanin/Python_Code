from caesar_cipher_encoder import caesar_cipher_encoder


def nested_caesar_cipher_encoder(text, shifting_parameters):
    """

    :param text: Some text, that contains only letters from the latin alphabet and some punctuation marks.
    :param shifting_parameters: A list of integers.
    :return: Text multiple times encrypted with Caesar encryption.
    """
    encoded_text = text
    for i in range(len(shifting_parameters)):
        encoded_text = caesar_cipher_encoder(encoded_text, shifting_parameters[i])
    return encoded_text
