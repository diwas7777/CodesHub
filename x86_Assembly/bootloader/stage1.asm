[bits 16]
[org 0x7C00]

    xor si, si

print:
    mov ah, 0x0E
    mov al, byte [msg + si]
    cmp al, 0
    js load_stage2
    int 0x10
    inc si
    jmp print

load_stage2:
    cli
    xor ax, ax
    mov ds, ax
    mov ax, 0x9000
    mov es, ax
    xor bx, bx

    mov ah, 0x02
    mov al, 10       ; Number of sectors to read
    mov ch, 0        ; Cylinder = 0
    mov cl, 2        ; Read from Sector 2
    mov dh, 0        ; Head = 0
    mov dl, 0x80     ; Boot drive

    int 0x13
    jc load_fail

    jmp es:bx

load_fail:
    mov si, fail_msg
    call print
    jmp $

fail_msg:
    db "Failed to load Stage 2...", 0

msg:
    db "Loading Stage 2...", 0

times 512 - ($ - $$) db 0
dw 0xAA55
