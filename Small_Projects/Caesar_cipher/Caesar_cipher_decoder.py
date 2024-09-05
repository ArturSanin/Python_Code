from Caesar_cipher_encoder import caesar_cipher_encoder


def caesar_cipher_decoder(encoded_text, shifting_parameter):
    """

    :param encoded_text: Text encrypted using Caesar encryption.
    :param shifting_parameter: Shifts every letter back.
    :return: Original text. Note for this to work, you need to now the original shifting parameter used for the
    encryption.
    """
    return caesar_cipher_encoder(encoded_text, 25 - shifting_parameter + 1)

