[bits 16]

start:
    mov ah, 0x00
    mov al, 0x03
    int 0x10

    cli
    xor ax, ax
    mov ds, ax
    mov es, ax
    mov ax, 0x7000
    mov ss, ax
    mov sp, 0xFFFF

    ; Load Global Descriptor Table
    lgdt [gdt_descriptor]

    ; Switch to 32 bit protected mode
    mov eax, cr0
    or eax, 1
    mov cr0, eax

    jmp 0x08:protected_mode_start

gdt_start:
    dq 0x0000000000000000     ; Null descriptor
    dq 0x00CF9A000000FFFF     ; Code segment (0x08)
    dq 0x00CF92000000FFFF     ; Data segment (0x10)

; ---- 32 bit code ----

protected_mode_start:
    mov ax, 0x10     ; Data segment selector
    mov ds, ax
    mov es, ax
    mov ss, ax
    mov esp, 0x90000

    mov edi, 0xB8000
    mov ax, 0x0720
    mov ecx, 80*25
    rep stosw

    call print
    hlt
    jmp $

.next:
    lodsb
    test al, al
    je .done
    mov ah, 0x0F
    mov [edi], ax
    add edi, 2
    jmp .next
.done:
    pop esi
    ret
    hlt
    jmp $

message: db "Loading the kernel...", 0

times 5120 - ($ - $$) db 0