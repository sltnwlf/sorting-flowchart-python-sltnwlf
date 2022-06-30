# Sorting flowchart

## Story

Your friend Maria found an old and dusty notebook with flowcharts on its almost completely faded pages.
She asked you to help her write the Python script equivalent of the flowcharts.
- The first flowchart looks like a simple sorting algorithm that repeatedly steps through the list,
compares each pair of adjacent items and swaps them if they are in the wrong order.
- The second flowchart seems to divide the list into smaller lists to find the searched value.
- The third flowchart looks for prime numbers.


## What are you going to learn?

- Write code based on a flowchart.
- Sort numbers without built-in functions.
- Use for and while loops.
- Use algorithms.
- Refactor to clean code. This makes code easier to read and maintain
  without changing any features.

## Tasks

1. Implement the algorithm described by [this flowchart](media/progbasics/bubble-sort-flowchart.png).
    - Running the program returns the following numbers in a list: [1, 2, 56, 32, 51, 2, 8, 92, 15]
    - Running the program returns the above numbers in a list in ascending order. The order is not hardcoded. The steps seen in the flowchart are used. [1, 2, 2, 8, 15, 32, 51, 56, 92]

2. Implement the algorithm described by [this flowchart](media/progbasics/binary-search-flowchart.png).
    - Running the program returns the following numbers in a list: [1, 2, 4, 7, 11, 22, 38, 42, 43]
    - Running the program returns an index of searched values in a list. If there are no values, -1 is returned. (i.e. if the value is 4, 2 is returned)

3. [OPTIONAL] Implement the algorithm described by [this flowchart](media/progbasics/sieve-of-eratosthenes-flowchart.png).
    - Running the program returns a list of all prime numbers, that are lesser or equal to the parameter N.

4. Refactor your solution: use functions for better readability and maintenance.
    - Running the program results in exactly the same behavior before and after refactoring.
    - Variable names in the program are meaningful, non-abbreviated nouns.
    - Function names in the program are meaningful, non-abbreviated verbs.
    - There is no unnecessary (dead) code or comments in the program.
    - There are no duplicate code parts or code parts doing the same thing differently in the program.
    - There are no functions doing more than one thing in the program.
    - After each modification the changes are committed, the program can be run, and the behavior is exactly the same as at the beginning.
    - Commit messages are meaningful.

## General requirements

None

## Hints

- Bubble sort: There are two loops and both of them can be implemented with `while` or `for`.
  Think about which one is more suited to what situation.
- Bubble sort: One loop is an outer loop and one is an inner loop. Do you know which one is which?
- Protect the main part of the program (outside of the functions) with
an `if __name__ == "__main__":` [code snippet](https://docs.python.org/3/library/__main__.html) while refactoring.


## Background materials

- <i class="far fa-exclamation"></i> [About Flowcharts](project/curriculum/materials/pages/general/flowcharts.md)
- <i class="far fa-exclamation"></i> [Basics of clean code](project/curriculum/materials/competencies/clean-code.md.html)
- <i class="far fa-exclamation"></i> [Refactoring in action](project/curriculum/materials/competencies/clean-code/refactoring.md.html)
- <i class="far fa-exclamation"></i> [About nice commit messages](https://chris.beams.io/posts/git-commit/)
- <i class="far fa-video"></i> [Bubble-sort with Hungarian ("Csángó") folk dance](https://www.youtube.com/watch?v=lyZQPjUT5B4)
- <i class="far fa-exclamation"></i> [Divide and conquer](https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm)
- <i class="far fa-exclamation"></i> [Binary search](https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search)
- <i class="far fa-exclamation"></i> [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#/media/File:Sieve_of_Eratosthenes_animation.gif)
- <i class="far fa-exclamation"></i> [What is `if __name__ == "__main__"`??](https://thepythonguru.com/what-is-if-__name__-__main__/)

