mapping = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}


def num_decodings(message):
    if not message:
        return 0

    length = len(message)
    dp = [0] * (length + 1)
    dp[0] = 1
    dp[1] = 0 if message[0] == "0" else 1

    for i in range(2, length + 1):
        one_digit = int(message[i - 1 : i])
        two_digits = int(message[i - 2 : i])

        if 1 <= one_digit <= 9:
            dp[i] += dp[i - 1]
        if 10 <= two_digits <= 26:
            dp[i] += dp[i - 2]

    return dp[length]


import ipdb


ipdb.set_trace()
# Example usage
encoded_message = "111"
result = num_decodings(encoded_message)
print(f"The number of ways the message '{encoded_message}' can be decoded is: {result}")
