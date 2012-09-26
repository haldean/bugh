bugh: Backup Github
====

`bugh` creates read-only local backups of all repositories in your Github
account, to protect you from hacking, catastrophic data loss, and your own
destructive power. To use, run `sudo python setup.py install`, then run `bugh
[your Github username]` from the directory in which you would like to mirror
your repositories.

Currently, `bugh` only mirrors the master branch of each repository; future
versions will allow mirroring all branches in a repository. It also does not
support mirroring private repositories.

`bugh` is made by [Will Haldean Brown][1] and is distributed under the GPLv3.

[1]:http://haldean.org
