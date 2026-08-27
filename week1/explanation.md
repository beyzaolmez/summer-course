# Additional Assignment: How the Credit Algorithm Works

For the Week 1 additional assignment I chose **Credit** and explain below how
its algorithm works, why it works, and where it falls short.

## What the program does

`credit.c` reads a card number and prints one of `AMEX`, `MASTERCARD`, `VISA`,
or `INVALID`. It answers two separate questions:

1. **Is the number mathematically valid?** (Luhn's checksum)
2. **If so, which company issued it?** (length + starting digits)

## How it works

### 1. Luhn's algorithm (validity)

Luhn's algorithm is a checksum that catches most accidental typos. Reading the
digits from **right to left**:

1. Take every **second** digit (the 2nd, 4th, 6th ... from the right) and
   **multiply it by 2**. If the product is greater than 9, add its two digits
   together (e.g. `8 * 2 = 16 -> 1 + 6 = 7`).
2. Sum those results.
3. Add that to the sum of the digits that were **not** multiplied.
4. If the grand total ends in `0` (i.e. `sum % 10 == 0`), the number passes.

In the code I isolate each digit with `number % 10`, then chop it off with
`number /= 10`. A `position` counter tells me whether a digit is in a
"doubling" slot (`position % 2 == 1`, since counting starts at 0 from the
right). I also count `length` in the same loop.

### 2. Classifying the issuer

Card companies use fixed rules:

- **American Express:** 15 digits, starts with `34` or `37`.
- **MasterCard:** 16 digits, starts with `51`–`55`.
- **Visa:** 13 or 16 digits, starts with `4`.

To read the leading digits I divide the number by 10 until only two digits
remain (`while (trimmed >= 100) trimmed /= 10;`), which lets me compare the
first two digits directly.

## Why it works

Luhn's algorithm works because doubling alternate digits makes the checksum
sensitive to **both** a wrong digit and to two adjacent digits being swapped —
the two most common human input errors. Any single-digit mistake changes the
total so it no longer ends in `0`, so the number is rejected. The issuer check
works simply because these prefixes and lengths are assigned by an
international standard (ISO/IEC 7812), so the ranges are reliable.

## Limitations

- **Validity is not authenticity.** Luhn only proves the number is
  *well-formed*. A made-up number that happens to pass the checksum will be
  reported as a valid card — it does not mean the card, funds, or account
  actually exist. Real verification needs the issuing bank.
- **Only three issuers.** Discover, JCB, Diners Club, etc. all fail Luhn-valid
  but get labelled `INVALID` because the program only knows AMEX/MC/Visa
  prefixes.
- **`long` size limits.** Very large card numbers could overflow a `long`, and
  leading zeros are lost because the input is stored as a number, not a string.
- **No structure beyond digits.** It ignores spaces or dashes a user might
  type, which `get_long` would reject rather than clean up.
