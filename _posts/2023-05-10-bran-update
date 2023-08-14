---
layout: post
title:  "Updating Bran and Current Challenges"
date:   2023-05-10 21:27:28 -0400
categories: project
---

# Issues, Ideas

## What went wrong

Bran was initially created as a sort of teaching tool for people to learn the basics of Turing machines, but it quickly started to take a life of its own. Once the basic were done, I started getting interested in turning bran into something more complex and interesting, and one of my biggest goals was to create a bran version of Assembly. What this required was a rewrite of a lot of what I'd currently created - in C.

I wasn't looking forward to that!

Surprisingly, the conversion process went really, really well. Outside of input, which remains the finickiest part of this entire project, the interpreter is now fully written in c, and much, much better written. The entire interpreter is contained between lazyqueue, lazystack, and interp. The two lazy data structures are simple versions of data structures, with little attention given to efficiency. I have plans to improve lazyqueue to include a circular array, and I might research ways to speed up lazystack's efficiency, but they're stopgaps so I can move forward with the project.


## Version 0.0.2

0.0.2 is a step back from 0.0.1 in terms of full features, but a step forward in terms of efficiency, clean code, and project concept. I'm hoping to get a few additional basic functions included, and then finish the rest of the 0.0.x series of branlang soon.

## Going Forward

I envision 0.0.x involving creating branlang, and adding the basics of QoL functionality. And make the whole thing in C. I still need a compiler and some small helper commands, and then I'd be done with the 0.0.x series. 0.1.x should be bran that allows to create user defined functions