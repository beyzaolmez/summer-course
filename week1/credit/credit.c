#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt for a card number (must be non-negative)
    long number;
    do
    {
        number = get_long("Number: ");
    }
    while (number < 0);

    // Walk through the digits from right to left
    long remaining = number;
    int sum = 0;
    int position = 0;
    int length = 0;

    while (remaining > 0)
    {
        int digit = remaining % 10;

        if (position % 2 == 0)
        {
            // Every other digit (from the right) is added directly
            sum += digit;
        }
        else
        {
            // Double it, then add its digits (split if the product is > 9)
            int doubled = digit * 2;
            sum += doubled / 10 + doubled % 10;
        }

        remaining /= 10;
        position++;
        length++;
    }

    // Find the first two digits to identify the card issuer
    long trimmed = number;
    while (trimmed >= 100)
    {
        trimmed /= 10;
    }
    int start = (int) trimmed;

    // Validate with Luhn's checksum, then classify by length and prefix
    if (sum % 10 != 0)
    {
        printf("INVALID\n");
    }
    else if (length == 15 && (start == 34 || start == 37))
    {
        printf("AMEX\n");
    }
    else if (length == 16 && start >= 51 && start <= 55)
    {
        printf("MASTERCARD\n");
    }
    else if ((length == 13 || length == 16) && start / 10 == 4)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}
