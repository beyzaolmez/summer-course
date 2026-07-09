#include <cs50.h>
#include <math.h>
#include <stdio.h>

int main(void)
{
    // Prompt for an amount of change owed in dollars (must be non-negative)
    float dollars;
    do
    {
        dollars = get_float("Change owed: ");
    }
    while (dollars < 0);

    // Convert dollars to cents, rounding to avoid floating-point error
    int cents = round(dollars * 100);

    int coins = 0;

    // Greedily take the largest coin possible at each step
    coins += cents / 25;
    cents = cents % 25;

    coins += cents / 10;
    cents = cents % 10;

    coins += cents / 5;
    cents = cents % 5;

    coins += cents / 1;
    cents = cents % 1;

    // Report the minimum number of coins
    printf("%i\n", coins);
}
