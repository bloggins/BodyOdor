Vulnserver has 13 commands including the help command. Its is unique in the fact that it was designed with vulnerable and non-vulnerable commands. 
It is a great training aid to practise buffer overflows. Each vulnerable command allows for different buffer overflow techniques to be exercised. This exercise I used
use the KSTET command which allows for small buffer space to practise egghunter buffer overflows.

```
c:\Users\xvz\Desktop>nc.exe 127.0.0.1 9999
Welcome to Vulnerable Server!
HELP
Valid Commands:
HELP
STATS [stat_value]
RTIME [rtime_value]
LTIME [ltime_value]
SRUN [srun_value]
TRUN [trun_value] 
GMON [gmon_value]
GDOG [gdog_value]
KSTET [kstet_value] 
GTER [gter_value]   
HTER [hter_value]
LTER [lter_value]
KSTAN [lstan_value]
EXIT
```

Vulnerable Application:

https://github.com/stephenbradshaw/vulnserver

History / About vulnserver:

http://www.thegreycorner.com/p/vulnserver.html

Learn Egghunter:

https://www.corelan.be/index.php/2010/01/09/exploit-writing-tutorial-part-8-win32-egg-hunting/

https://www.exploit-db.com/docs/english/18482-egg-hunter---a-twist-in-buffer-overflow.pdf
