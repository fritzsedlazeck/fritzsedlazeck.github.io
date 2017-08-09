---
header:
  image: test2.jpg
title: "MASon: Million Alignments In Seconds - A Platform Independent Pairwise Sequence Alignment Library for Next Generation Sequencing Data"
collection: publications
permalink: /publication/2012-02-01-MASon- MILLION ALIGNMENTS IN SECONDS - A Platform Independent Pairwise Sequence Alignment Library for Next Generation Sequencing Data
excerpt: ' '

date: 2012-02-01
venue: 'SciTePress'
paperurl: 'http://www.scitepress.org/DigitalLibrary/Link.aspx?doi=10.5220/0003775701950201'
citation: 'P. Rescheneder, A. von Haeseler, and <b>F.J. Sedlazeck</b> (2012). &quot;MASon: Million Alignments In Seconds - A Platform Independent Pairwise Sequence Alignment Library for Next Generation Sequencing Data.&quot; <i>Proceedings of the International Conference on Bioinformatics Models, Methods and Algorithms (BIOINFORMATICS 2012)</i>. 195-201.'
---

The advent of Next Generation Sequencing (NGS) technologies and the increase in read length and number of reads per run poses a computational challenge to bioinformatics. The demand for sensible, inexpensive, and fast methods to align reads to a reference genome is constantly increasing. Due to the high sensitivity the Smith-Waterman (SW) algorithm is best suited for that. However, its high demand for computational resources makes it unpractical. Here we present an optimal SWimplementation for NGS data and demonstrate the advantages of using common and inexpensive high performance architectures to improve the computing time of NGS applications. We implemented a C++ library (MASon) that exploits graphic cards (CUDA, OpenCL) and CPU vector instructions (SSE, OpenCL) to efficiently handle millions of short local pairwise sequence alignments (36bp - 1,000bp). All libraries can be easily integrated into existing and upcoming NGS applications and allow programmers to optimally utilize moder n hardware, ranging from desktop computers to high-end cluster.

[Download paper here](http://www.scitepress.org/DigitalLibrary/Link.aspx?doi=10.5220/0003775701950201)

