# Python DSA Notes

My personal notes and practice code while learning data structures and algorithms in Python. Each file is a standalone script you can run directly — they are meant to be read, edited and re-run, not imported as a library.

## Contents

| File | Topic |
| --- | --- |
| `Taking_multiple_inputs.py` | Reading a single value and several space-separated values from the user with `input()`, `map()` and `split()` |
| `2D_array.py` | Building an `N x M` matrix, filling it from input, and transposing it two ways — in place and into a new matrix |
| `LinkedList.py` | Singly linked list with a `Node` class: insert at head, insert at tail, `__len__` and `__str__` |
| `Binary_tree.py` | Binary tree built from `Node` objects, with preorder, inorder and postorder traversal |

## Running a file

```bash
python <filename>.py
```

For example:

```bash
python LinkedList.py
```

Some scripts ask for input:

- `Taking_multiple_inputs.py` — one number, then a line of numbers separated by spaces
- `2D_array.py` — number of rows, number of columns, then each cell value one by one

`LinkedList.py` and `Binary_tree.py` need no input; they just print their output.

## Notes / TODO

- `2D_array.py`: the in-place transpose assumes a square matrix (`N == M`). For non-square matrices the transposed copy below it is the one to use.
- `LinkedList.py`: currently only inserts; delete, search and reverse are not written yet.

## Requirements

Python 3.8+ and nothing else — no third-party packages.
