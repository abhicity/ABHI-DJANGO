[TOC]

# ___Arithmetic Operators (Python)___


| Operator | Operation      |
| :------: | -------------- |
|    +     | Addition       |
|    -     | Subtraction    |
|    *     | Multiplication |
|    **    | Exponential    |
|    /     | Division       |

### ___`[+]` Addition Operator___
| Sl No | a       |   +   | b       |   =   | Output              |
| :---: | ------- | :---: | ------- | :---: | ------------------- |
|   1   | int     |   +   | int     |   =   | int                 |
|   2   | float   |   +   | float   |   =   | float               |
|   3   | complex |   +   | complex |   =   | complex             |
|   4   | string  |   +   | string  |   =   | string              |
|   5   | bool    |   +   | bool    |   =   | int                 |
|   6   | None    |   +   | None    |   =   | unsupported operand |
|   7   | int     |   +   | float   |   =   | float               |
|   8   | int     |   +   | complex |   =   | complex             |
|   9   | int     |   +   | string  |   =   | unsupported operand |
|  10   | int     |   +   | bool    |   =   | int                 |
|  11   | int     |   +   | None    |   =   | unsupported operand |
|  12   | float   |   +   | complex |   =   | complex             |
|  13   | float   |   +   | string  |   =   | unsupported operand |
|  14   | float   |   +   | bool    |   =   | float               |
|  15   | float   |   +   | None    |   =   | unsupported operand |
|  16   | complex |   +   | string  |   =   | unsupported operand |
|  17   | complex |   +   | bool    |   =   | complex             |
|  18   | complex |   +   | None    |   =   | unsupported operand |
|  19   | string  |   +   | bool    |   =   | unsupported operand |
|  20   | string  |   +   | None    |   =   | unsupported operand |
|  21   | bool    |   +   | None    |   =   | unsupported operand |


### ___`[-]` Subtraction Operator___

| Sl No | a       |   -   | b       |   =   | Output              |
| :---: | ------- | :---: | ------- | :---: | ------------------- |
|   1   | int     |   -   | int     |   =   | int                 |
|   2   | float   |   -   | float   |   =   | float               |
|   3   | complex |   -   | complex |   =   | complex             |
|   4   | string  |   -   | string  |   =   | string              |
|   5   | bool    |   -   | bool    |   =   | int                 |
|   6   | None    |   -   | None    |   =   | unsupported operand |
|   7   | int     |   -   | float   |   =   | float               |
|   8   | int     |   -   | complex |   =   | complex             |
|   9   | int     |   -   | string  |   =   | unsupported operand |
|  10   | int     |   -   | bool    |   =   | int                 |
|  11   | int     |   -   | None    |   =   | unsupported operand |
|  12   | float   |   -   | complex |   =   | complex             |
|  13   | float   |   -   | string  |   =   | unsupported operand |
|  14   | float   |   -   | bool    |   =   | float               |
|  15   | float   |   -   | None    |   =   | unsupported operand |
|  16   | complex |   -   | string  |   =   | unsupported operand |
|  17   | complex |   -   | bool    |   =   | complex             |
|  18   | complex |   -   | None    |   =   | unsupported operand |
|  19   | string  |   -   | bool    |   =   | unsupported operand |
|  20   | string  |   -   | None    |   =   | unsupported operand |
|  21   | bool    |   -   | None    |   =   | unsupported operand |
---

---

### ___`[*]` Multiplication Operator___

| Sl No | a       |   *   | b       |   =   | Output              |
| :---: | ------- | :---: | ------- | :---: | ------------------- |
|   1   | int     |   *   | int     |   =   | int                 |
|   2   | float   |   *   | float   |   =   | float               |
|   3   | complex |   *   | complex |   =   | complex             |
|   4   | string  |   *   | string  |   =   | can't multiply      |
|   5   | bool    |   *   | bool    |   =   | int                 |
|   6   | None    |   *   | None    |   =   | unsupported operand |
|   7   | int     |   *   | float   |   =   | float               |
|   8   | int     |   *   | complex |   =   | complex             |
|   9   | int     |   *   | string  |   =   | string              |
|  10   | int     |   *   | bool    |   =   | int                 |
|  11   | int     |   *   | None    |   =   | unsupported operand |
|  12   | float   |   *   | complex |   =   | complex             |
|  13   | float   |   *   | string  |   =   | can't multiply      |
|  14   | float   |   *   | bool    |   =   | float               |
|  15   | float   |   *   | None    |   =   | unsupported operand |
|  16   | complex |   *   | string  |   =   | unsupported operand |
|  17   | complex |   *   | bool    |   =   | complex             |
|  18   | complex |   *   | None    |   =   | unsupported operand |
|  19   | string  |   *   | bool    |   =   | can't multiply      |
|  20   | string  |   *   | None    |   =   | can't multiply      |
|  21   | bool    |   *   | None    |   =   | unsupported operand |
---
---

### ___`[**]` Exponential Operator___

| Sl No | a       |  **   | b       |   =   | Output              |
| :---: | ------- | :---: | ------- | :---: | ------------------- |
|   1   | int     |  **   | int     |   =   | int                 |
|   2   | float   |  **   | float   |   =   | float               |
|   3   | complex |   *   | complex |   =   | complex             |
|   4   | string  |  **   | string  |   =   | unsupported operand |
|   5   | bool    |  **   | bool    |   =   | int                 |
|   6   | None    |  **   | None    |   =   | unsupported operand |
|   7   | int     |  **   | float   |   =   | float               |
|   8   | int     |  **   | complex |   =   | complex             |
|   9   | int     |  **   | string  |   =   | unsupported operand |
|  10   | int     |  **   | bool    |   =   | int                 |
|  11   | int     |  **   | None    |   =   | unsupported operand |
|  12   | float   |  **   | complex |   =   | complex             |
|  13   | float   |  **   | string  |   =   | unsupported operand |
|  14   | float   |  **   | bool    |   =   | float               |
|  15   | float   |  **   | None    |   =   | unsupported operand |
|  16   | complex |  **   | string  |   =   | unsupported operand |
|  17   | complex |  **   | bool    |   =   | complex             |
|  18   | complex |  **   | None    |   =   | unsupported operand |
|  19   | string  |  **   | bool    |   =   | unsupported operand |
|  20   | string  |  **   | None    |   =   | unsupported operand |
|  21   | bool    |  **   | None    |   =   | unsupported operand |
---
---

### ___`[/]` Division Operator___

| Sl No | a       |   /   | b       |   =   | Output              |
| :---: | ------- | :---: | ------- | :---: | ------------------- |
|   1   | int     |   /   | int     |   =   | float               |
|   2   | float   |   /   | float   |   =   | float               |
|   3   | complex |   /   | complex |   =   | complex             |
|   4   | string  |   /   | string  |   =   | unsupported operand |
|   5   | bool    |   /   | bool    |   =   | division by zero    |
|   6   | None    |   /   | None    |   =   | unsupported operand |
|   7   | int     |   /   | float   |   =   | float               |
|   8   | int     |   /   | complex |   =   | complex             |
|   9   | int     |   /   | string  |   =   | unsupported operand |
|  10   | int     |   /   | bool    |   =   | float               |
|  11   | int     |   /   | None    |   =   | unsupported operand |
|  12   | float   |   /   | complex |   =   | complex             |
|  13   | float   |   /   | string  |   =   | unsupported operand |
|  14   | float   |   /   | bool    |   =   | float               |
|  15   | float   |   /   | None    |   =   | unsupported operand |
|  16   | complex |   /   | string  |   =   | unsupported operand |
|  17   | complex |   /   | bool    |   =   | complex             |
|  18   | complex |   /   | None    |   =   | unsupported operand |
|  19   | string  |   /   | bool    |   =   | unsupported operand |
|  20   | string  |   /   | None    |   =   | unsupported operand |
|  21   | bool    |   /   | None    |   =   | unsupported operand |
---
---

