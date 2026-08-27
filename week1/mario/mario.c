#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt for a height between 1 and 8 (re-prompt until valid)
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    // Build the two half-pyramids row by row
    for (int row = 0; row < height; row++)
    {
        // Left-side padding so the left pyramid is right-aligned
        for (int spaces = 0; spaces < height - row - 1; spaces++)
        {
            printf(" ");
        }

        // Left pyramid: row + 1 bricks
        for (int hashes = 0; hashes < row + 1; hashes++)
        {
            printf("#");
        }

        // Two-space gap between the pyramids
        printf("  ");

        // Right pyramid: row + 1 bricks
        for (int hashes = 0; hashes < row + 1; hashes++)
        {
            printf("#");
        }

        printf("\n");
    }
}
