---
layout: page
title: Freshman Summer Coursework
permalink: /courses/freshmansummer/
exclude: true
---


# The Freshmen Experience III - Summer 2023

Man, this really was the semester I fell in love with CMU. I met some really cool people, did some really amazing work, and gained a newfound appreciation for Computer Systems. I've also decided that I absolutely want to transfer to Computer Science at CMU, and I'm going to do my best to do that.

## 15-213 Introduction to Computer Systems

Oh.

Oh I *loved* this class. This class took me from wanting to do something unspecific with computer science to *transferring to that major*, and do a concentration in this part of CS.

So, what did I do? 213 was an incredible introduction to basic parts of a computer, followed by a lab practicing the techniques used by those parts. We started with a few labs to get us familiar with C and Assembly, including Bomb Lab, which focused on GDB and reading assembly, and Attack Lab, which focused on buffer overflow and exploiting stack/memory vulnerability, using mostly assembly.

That was followed by a gauntlet of four of my favorite assignments at CMU. First, we learned about memory caching, and wrote a cache that simulated the operations that a real-life cache takes. We also optimized a matrix transposition function to take advantage of the cache design. After that, we took on memory allocation, by writing an implementation of malloc, C's memory allocator. We then optimized malloc using coalescing, to put freed memory blocks together, as and using a segmented list to simulate best-fit and increase throughput. Beyond that, we also implemented footerless blocks and miniblocks to improve utilization and optimize malloc beyond what libc has.

Malloclab was a huge assignment, and we continued forward with concurrency and wrote a tiny shell, which used our knowledge of processes to operate similarly to the linux shell. We also implemented signal handling to help our shell run for long periods of time without accruing waste. After shell lab, we wrote our own concurrent network proxy, using threads instead of processes. This network proxy was able to handle high stress, didn't waste resources, and also had a cache to speed up data fetching from websites. My proxy wasn't as fast as my local internet connection, but I was able to use it for low-stress browsing!

So, I just told you *everything* I did in 213, but honestly, I just love talking about that class. It was so much fun, and I really, really want to take some of the courses this unlocks like 15-410 Operating Systems, 15-411 Compilers, 15-346 Computer Architecture and 15-418 Parallel Computer Architecture. While I'm focused on transferring to CS in sophomore year, I will try to sneak in a few of these courses ASAP :)

Finally, shoutout Brian Railing for being a wonderful professor and inspiring my two projects that I'm working on as of the writing of this page, `Fillet`, a project following the Crafting Interpreter's book (and translating the code to Rust), and a read-through and analysis of the Linux 0.0.1 kernel.

## 21-241 Matrices and Linear Transformations

I did not enjoy this class. I had taken a Matrices class in High School, and it turns out that should've counted for credit because this was a waste of a half-summer. I've never been more burned out than after this final.

## 99-270 Summer Undergraduate Research Apprenticeship

This was a really interesting summer project that helped me gain a deeper appreciation for the work put into HFT research. We focused on finding patterns in how Designated Market Makers split orders between multiple exchanges, and also looking into the order-splitting phenomenon and finding out how DMMs handled large call or put orders. Finally, my group packaged our findings into a presentation we gave to our professor advisor. We wrote our code in Python using the Numpy package.

[Back]({% link courses.markdown %})