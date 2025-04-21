# Card Sorter

Simple tool for sorting my MTG cards.

# Problem statement

I have a large collection of Magic: The Gathering cards which are sorted alphabetically. Occasionally
I'll buy new cards, which I then need to add to the collection. I can't just jam them into the
collection mindlessly though. That would break the system!

Adding individual cards is easy: look at each card and flip through the collection alphabetically
until I get to the new card's alphabetical slot, then drop it in. But that takes awhile. And there's
an inefficiency: sometimes I have a bunch of cards that might fit into a single slot, so doing a new
alphabetical search is time-consuming. What if I could have a program that looked at my current
collection, my new cards, and told me how to group my new cards into packets and where I should put
them in my collection?

* Input:
    * a sorted list of named Cards, each with names as Strings and sorted alphabetically on this field.
    * an unsorted list of named Cards.
* Output:
    * An unsorted list of groups of cards. Each group is alphabetically sorted and gives me each
    card that should go within the packet. Bonus points if I also know which cards in the collection
    go before and after.

# Developer dependencies
* poetry
* python dependencies (recommend using pipx)
    * pre-commit: run instructions at https://pre-commit.com/#quick-start

# To Do:
* x

## Maybe
* reconsider having special classes for CardGroups. Aren't they really just lists?
* clean up utils. they're kinda messy. could separate into clearly layered input methods
