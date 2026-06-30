# One-Hot Encoding

Machine learning models work with numbers, not text.

One-hot encoding converts categorical values into binary columns.

Example:

Color

Red

Blue

Green

becomes

Red Blue Green

1    0    0

0    1    0

0    0    1

This prevents models from assuming one category is greater than another.