---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
header:
  image: test2.jpg
---


My research focuses on the development of scalable algorithms to assess the variability in terms of single nucleotide polymorphisms as well as structural variations within and among populations. I am particular interested in developing and applying algorithms that utilize previous observation from biology to achieve high accuracy and a fast runtime utilizing hardware infrastructures like graphic processing units (GPU) or grid engines. 

High throughput sequencing (HTS) has become a standard method in molecular biological research.  Consortium projects like the 1000 genome or the 10k genomes project show a clear trend to sequence more genomes or transcriptomes to assess the variability within organisms or among whole populations or even eco systems. In the same time, it is recognized that standard programs are not capable to achieve the speed and the accuracy (e.g. in terms of correctly mapped reads) in every scenario. Indeed, the questions related to the easily accessible regions of genomes are almost solved. What remains are regions in the genome that are hard to assess due to their high polymorphism or low complexity (e.g. repeats).  This demands for algorithms that while preforming a through out search still have a short runtime to be able to cope with the flood of data. My research explores the possibilities to robustly assess and investigate regions of the genome that are highly variable and most often the driver for evolution or genetic diseases like cancer. 


## Research Interest
 * Structural Variations
 * Sequence Alignment
 * High Performance and Multi-Core Computing
 * Human Genetics
 * Non model organisms


# Selected Software Packages


### [1. FALCON](https://github.com/PacificBiosciences/FALCON)
  Phased Diploid Genome Assembly with PacBio sequencing reads  
  [Github](https://github.com/PacificBiosciences/FALCON){: .btn}

### [2. GenomeScope](https://github.com/schatzlab/genomescope)   
  Kmer based analysis for genome length, heterozygosity and repeat rate for short reads.  
  [Homepage](http://qb.cshl.edu/genomescope/){: .btn .btn--info}  
  [Github](https://github.com/schatzlab/genomescope){: .btn} 

### [3. LRSim](https://github.com/aquaskyline/LRSIM) 
  10x Genomics read simulator.  
  [Github](https://github.com/aquaskyline/LRSIM){: .btn} 

### [4. MUMmer SGE](https://github.com/fritzsedlazeck/sge_mummer) 
  Parallization script for MUMMer.  
  [Github](https://github.com/fritzsedlazeck/sge_mummer){: .btn} 

### [5. NGMLR](https://github.com/philres/ngmlr) 
  Long read mapper to improve mapping and SV calling   
  [Github](https://github.com/philres/ngmlr){: .btn} 

### [6. NGM](https://github.com/Cibiv/NextGenMap) 
  Short read mapper especially suitable for high SNP rates  
  [Github](https://github.com/Cibiv/NextGenMap){: .btn} 

### [7. Teaser](http://teaser.cibiv.univie.ac.at/) 
  Benchmarking framework for short read mapper.  
  [Homepage](http://teaser.cibiv.univie.ac.at/){: .btn .btn--info}    
  [Github](https://github.com/cibiv/teaser/){: .btn} 

### [8. Sniffles](https://github.com/fritzsedlazeck/Sniffles) 
  Structural variation caller for PacBio and Oxford Nanopore reads.  
  [Github](https://github.com/fritzsedlazeck/Sniffles){: .btn} 

### [9. SURVIVOR](https://github.com/fritzsedlazeck/SURVIVOR) 
  Tool set for simulating/evaluating SVs, merging and comparing SVs within and among samples, and includes various methods to reformat or summarize SVs.  
  [Github](https://github.com/fritzsedlazeck/SURVIVOR){: .btn}

### [10. SURVIVOR_ant](https://github.com/fritzsedlazeck/SURVIVOR_ant) 
  Method to annotate SVs using gff, bed or other vcf files.
  [Github](https://github.com/fritzsedlazeck/SURVIVOR_ant){: .btn}


{% include base_path %}
