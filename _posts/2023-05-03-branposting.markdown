---
layout: post
title:  "Bran, a BF Tutorial"
date:   2023-05-03 13:22:47 -0400
categories: project
---

# The Bran Project

This was a toy project I worked on between finals during freshman spring. The idea was to create a simple brainf\*ck interperter that would allow me to do step by step parsing of the code, as well as a letting me easily view and manipulate the data that I was working with. This was based on a similar idea I had for another simple language, deadfish, and I wanted Bran to help people essentially understand how to create computation on a very very low level. It's a teaching tool, since you can step through any processs and explain it to somebody!

## Version 0.0.1

0.0.1 just contains the basics of bran, the bran compiler, bfcc.c0 which works on .bf files to create functions, and the bran shell, bfsh.c0. The shell is currently in development for more complexity, though I'm also currently working to create a system to accept input, which would allow more complex creations to be made out of Bran