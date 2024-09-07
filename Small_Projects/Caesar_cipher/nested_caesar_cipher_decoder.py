from caesar_cipher_decoder import caesar_cipher_decoder


def nested_caesar_cipher_decoder(encoded_text, shifting_parameters):
    """

    :param encoded_text: Text encrypted using nested Caesar encryption.
    :param shifting_parameters: The shifting parameters used in the nested Caesar encryption.
    :return: Original text. Note for this to work, you need to now the original shifting parameters used for the
    encryption.
    """
    decoded_text = encoded_text
    for i in range(len(shifting_parameters)):
        decoded_text = caesar_cipher_decoder(decoded_text, shifting_parameters[- (i + 1)])
    return decoded_text
