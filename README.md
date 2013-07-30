




skypelog  from: https://github.com/kristianlm/skypelog
parse.py from: http://www.len.ro/work/skype-logs-archiving-on-linux/
log.sh (edit it with your username/folders) runs both, and does a search/replace for čšž chars


# Skypelog

A simple tool to read binary DBB databases and output its text equivalent.

This could be used to read the Skype chatlogs (stored unencrypted as `chatmsg256.dbb` under `~/.Skype/<username>/`) 
on some Skype versions. It may not work on the newest Windows-versions but on my Linux with Skype 2.2,
those DBB files show up.

Try this after building: 

```bash
$ ./skypelog chatmsg*.dbb | sort | less
```

and have fun!

I took the one skypelog.c from 
[here](http://www.hackerfactor.com/blog/index.php?/archives/231-Skype-Logs.html)
and made it into a 
[GBT](http://en.wikipedia.org/wiki/GNU_build_system)
project. If you're new to the GNU build tools like me, here's how you get this built:

```bash
$ aclocal
$ autoconf
$ automake -a
$ ./configure 
$ make
$ sudo make install
```

Best of luck!
