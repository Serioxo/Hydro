section .text
global _WinMain@16
_WinMain@16:
     push dword 34
     push dword 35
     pop eax
     pop ebx
     add eax, ebx
     push eax
     pop eax
     mov ebx, eax
     push dword 360
     push dword 400
     pop eax
     pop ebx
     sub eax, ebx
     push eax
     pop eax
     mov ebx, eax
     mov eax, 0
     syscall
