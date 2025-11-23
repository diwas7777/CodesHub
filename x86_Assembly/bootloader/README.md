# Bootloader

A bootloader is a program that gets executed just after the computer is powered on. It is responsible for loading the OS from the disk into memory, and hand over the control to the OS kernel.

## Project Description

This project is a very simple implementation of a bootloader written in x86 Assembly. It does three main jobs:

- Load the required sectors from disk
- Setup the Global Descriptor Table
- Switch to 32-bit Protected Mode

## How to Test?

Step 1: Install QEMU and NASM
Step 2: Compile each .asm file using the command:
```Bash
nasm -f elf32 -o <output_file_name>.o <input_file_name>.asm
```
Step 3: Link all the .o files together using `ld`
```Bash
ld -m elf_i386 -nostdlib -nostartfiles -Ttext 0x7c00 --oformat binary <file1>.o <file2>.o -o boot.bin
```
Step 4: Run the binary:
```Bash
qemu-system-i386 -fda boot.bin
```