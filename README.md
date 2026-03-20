# .dot-hyphen

**.dot-hyphen** is an esoteric programming language created by me in 2026. The language came to be as a result of me toying with the fact that $-(-x)=+x$. The language also draws some inspiration from [Lambda Calculus](https://esolangs.org/wiki/Lambda_calculus) for the philosophy that everything is an expression, although as you'll see, the language is inherently impure unlike most calculus-like languages.

# Memory Model

**.dot-hyphen** operates of a single unbounded-length array consisting of unbounded-valued **signed** integers, all of which are initialized to `0`. The address space of the array can be negative. 

# Syntax and Semantics

The language only has two syntax constructions, both of which are expressions:

* `.x-y`: Can be interpreted as `array[x] -= y; return array[x]` in other languages. The order of evaluation is `x`, then `y`, then `.x-y`.
* Non-negative integers: `0`, `1`, `2`, ...

The entire program is basically a giant nested-expression made using these two constructions.

The root expression is evaluated nonstop. At each evaluation, if the result of the root expression is within the ASCII range, it is outputted as an ASCII character.

# Get Started

Write a `.dot-hyphen` code with your favorite text-editor (or directly in the terminal if you're a psycho). Then, pipe into the interpreter like follows
```sh
cat source-file.dot-hyphen | python dothyphen.py
```

There are also some options you can try:
* `-d` or `--debug`: print integers instead of ASCII characters and ignore the ASCII range limitation for outputs.
* `-l` or `--limit`: takes an argument `n`. Limit execution to `n` iterations.
