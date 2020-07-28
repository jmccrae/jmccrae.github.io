Programming Language Review
===========================

Ratings Scale
-------------

- 3.0: Best of the best, e.g., C for Speed
- 2.5: Extremely strong
- 2.0: Good
- 1.5: Average
- 1.0: Poor
- 0.5: Significantly makes the programming language hard to use
- 0.0: Absolute dealbreaker, the language is unusable IMHO

Categories
----------

- **Speed**: How fast programs written in this language are
- **Concisenes**: The typical lines of code used to express ideas in this language
- **Correctness**: How much the language prevents errors or guarantees correctness of programs
- **Learnability**: How easy it is to learn the language and how likely it is 
    to provide weird 'gotcha' moments
- **Collaboration**: The tooling to support effortless cross-system builds and
    the depth of libraries provided
- **Aesthetics**: How the language looks and feels and the 'coolness' factor

Java
----

**Speed**: Java has never been very fast for a compiled language and while
Java performs well on many benchmarks, class load times can mean that this is 
often not what is experienced in practice (2.0)

**Conciseness**: Java is the true master of unnecessary boilerplate and while 
recent versions have started to work against this, many constructs such as 
lambdas still just take more code than other languages (1.0)

**Correctness**: The types and the compile system help a lot here, but Java 
still allows for many of the worst kind of programming paradigms including
null pointers and a dodgy exception system (1.5)

**Learnability**: There is a reason why Java was for many years the teaching 
languages in most universities, it is very easy to learn (2.5)

**Collaboration**: Ant, Maven, Gradle and other tools invented and innovated 
on the nature of collaboration and the wealth of libraries (nearly all of which
work on any platform) is the true reason to use Java (3.0)

**Aesthetics**: Java is a typical curly-brace language so is mostly quite 
pleasant, however there is little cool about Java anymore (1.5)


C
-

**Speed**: Few can argue that C isn't the closest to machine code and fastest 
language there is (3.0)

**Conciseness**: Up to a point C is quite concise, but this can quickly 
disappear when writing complex code (1.5)

**Correctness**: Static-typing helps here but C is famous for letting you shoot
yourself in the foot (1.5)

**Learnability**: C is a very small language, however many of the concepts do
trip up learners (2.0)

**Collaboration***: Building cross-platform C is a nightmare and the C language
lacks some basic ideas (such as packages) to support this (0.5)

**Aesthetics**: C often verges towards unreadability and has lots of special
characters with esoteric meaning (1.0)

Rust 
----

**Speed**: Rust promises and mostly delivers C-like speed even beating C in a 
few [benchmarks](https://benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/rust.html) 
(3.0)

**Conciseness**: Rust has a lot of modern features that encourage conciseness
including good lambdas and macros, but other features (for example `enum`s or 
deriving traits) seem to lead to a lot of code (2.0)

**Correctness**: This is one of Rust's focus and selling points, only 'research'
languages can compete here (3.0)

**Learnability**: Rust should be easy to learn with its quite small feature set.
Unfortunately the `trait` system is so different to other languages and the 
fact that most learns end up 'fighting with the borrow checker' really undermines
this (1.0)

**Collaboration**: Cargo is a great tool that makes working with Rust very easy
and the access to any C library is a boon here (2.5)

**Aesthetics**: A generally nice looking language with cool ideas but I do hate
having to put `&` or `.clone()` with (nearly) every function argument (2.0)

Python
------

**Speed**: Python is an interpreted language so will never win this category. 
However Python is not even as fast as Javascript. Many Python libraries of course
rely on calling C code, hence why Python is used in high-performance tasks such
as deep learning, but saying that your language is fast because you can also
use another language seems a self-defeating point (1.0)

**Conciseness**: Python is easy and also very quick to write, with one of the 
most intuitive and compact lambda syntaxes (3.0)

**Correctness**: Static checking is non-existent, there is a null
type, exceptions are very haphazard and testing is not as easy as other languages
(0.5)

**Learnability**: When I said universities *used* to teach Java, that is because
they have mostly moved to Python now (3.0)

**Collaboration**: In theory, there is a package system and `pip` and `easy_install`
make it easy to install packages... in theory. The practice is that often this
can be quite a challenge (1.5)

**Aesthetics**: I am personally indifferent to the curly-braces versus spacing
argument, but Python is certainly what I would like a programming language to
look like and it has plenty of cool 'pythonic' elements (3.0)

Scala
-----

**Speed**: Mostly the same speed as Java but more classes mean that it is often
a tad slower (2.0)

**Conciseness**: Scala's many paradigms can effectively produce some very concise
(if unreadable) code. More typical usage is still quite concise though (2.5)

**Correctness**: Scala claims to have many of the tools that allow for correct
programs although some of them (like null pointers) are optional and implementation
can create errors at unexpected points (2.0)

**Learnability**: Scala is not particularly easy-to-learn due to its many features
but few of these features really provide any gotchas (1.5)

**Collaboration**: Full compatibility with the JVM ecosystem is a 
great thing (3.0)

**Aesthetics**: Lots of nice features and a reasonable syntax make Scala code
quite beautiful and the language is full (maybe a bit too full) of cool features 
(2.0)

Kotlin (provisional)
--------------------

*I don't have much experience with this language yet so scores will likely be
revised*

**Speed**: It's a JVM language (2.0)

**Conciseness**: One of the main objectives is to be a less-verbose Java, on this
it mosty succeeds (2.0)

**Correctness**: Acutally removing null pointers helps a lot here (2.0)

**Learnability**: Very simple language with some nice tutorials (2.0)

**Collaboration**: Again it is a JVM language (3.0)

**Aesthetics**: Simple clean syntax (2.0)

Javascript
----------

**Speed**: Javascript has some very fast interpreters but they are still interpreters
and don't really compete with compiled languages (1.5)

**Conciseness**: As a scripting langauge Javascript is generally quite concise
although some of the cascades of callbacks found in some APIs and ugly syntax
for advanced features (e.g., classes) don't help (2.0)

**Correctness**: Not really a feature of Javascript and one of the reasons why
TypeScript was introduced (0.5)

**Learnability**: Javascript is very easy to learn, but also quite full of 'gotcha'
moments that cause more issue for new programmers than they should (2.0)

**Collaboration**: Node came and introduced a proper package system to JS, but
it seems to frequently not work or be hard to install (1.5)

**Aesthetics**: A simple clean syntax without much to criticise (2.0)

Perl
----

**Speed**: Slow even for an interpreted language (0.5)

**Conciseness**: Perl is the master of the one-liner, even if those one-liners
may take hours to understand (3.0)

**Correctness**: Perl has a strict mode (this better than Python) but still 
little in the way of safetry (1.0)

**Learnability**: Although it is easy to get started, I have never felt I really 
mastered Perl. The joke about `perl < /dev/random` compiling is valid here (2.0)

**Collaboration**: PPM is one of the oldest and most creaking package management
systems going (1.5)

**Aesthetics**: Perl is really fugly but full of cool ideas (1.0)

R
-

**Speed**: Sometimes you get it just right and the library functions work but
otherwise R's performance is truly dreadful (0.5)

**Conciseness**: For what R is designed for it does it concisely, for everything
else it can be a nightmare (2.0)

**Correctness**: As with most interpreted languages there are very few safety 
features (1.0)

**Learnability**: Pretty okay (if you are also learning a stats course at the
same time), but my experiences teaching it are that students find it hard (1.5)

**Collaboration**: CRAN actually works pretty well (2.0)

**Aesthetics**: Assignment with `<-` is a very subjective thing (I hate it),
there is some cool stuff here (1.5)

C++
---

**Speed**: Technically you could just write C code and call it C++ and get the
same performance. Even practically, the overheads of C++ constructs are pretty 
low (3.0)

**Conciseness**: Extra headers full of duplicate functions and more boilerplate
than C make this not a pleasant language to work with, even if a few modern
features in C++11 do help a litle (1.0)

**Correctness**: Much like with Scala, there are great features here but they
can easily be ignored to ensure C compatibility (2.0)

**Learnability**: This was the second language I learnt (after BASIC), but still
learners struggle with this language a lot and the compiler produces error messages
that look like they were written by eldritch beings from other dimensions (1.0)

**Collaboration**: Lots of duplicate and incompatible systems here that fail
to solve the problems with C (1.0)

**Aesthetics**: C++ is definitely fugly and most of its cool ideas are very
out-of-date now (1.0)

Overall
-------

| Language       | Speed | Concise | Correct | Learn | Collab | Looks | Total |
| -------------- |:-----:|:-------:|:-------:|:-----:|:------:|:-----:|:-----:|
| Rust           |  3.0  |   2.0   |   3.0   |  1.0  |  2.5   |  2.0  |  13.5 |
| Scala          |  2.0  |   2.5   |   2.0   |  1.5  |  3.0   |  2.0  |  13.0 |
| Kotlin         |  2.0  |   2.0   |   2.0   |  2.0  |  3.0   |  2.0  |  13.0 |
| Python         |  1.0  |   3.0   |   0.5   |  3.0  |  1.5   |  3.0  |  12.0 |
| Java           |  2.0  |   1.0   |   1.5   |  2.5  |  3.0   |  1.5  |  11.5 | 
| Javascript     |  1.5  |   2.0   |   0.5   |  2.0  |  1.5   |  2.0  |   9.5 |
| C              |  3.0  |   1.5   |   1.5   |  2.0  |  0.5   |  1.0  |   9.5 |
| C++            |  3.0  |   1.0   |   2.0   |  1.0  |  1.0   |  1.0  |   9.0 |
| R              |  0.5  |   2.0   |   1.0   |  1.5  |  2.0   |  1.5  |   8.5 |
| Perl           |  0.5  |   3.0   |   1.0   |  2.0  |  1.5   |  1.0  |   8.0 |
