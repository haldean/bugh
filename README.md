bugh: Backup Github
====

`bugh` creates read-only local backups of all repositories in your Github
account, to protect you from hacking, catastrophic data loss, and your own
destructive power. To install, run:  

    sudo pip install bugh

After installing, run `bugh [your Github username]` from the directory
in which you would like to mirror your repositories. The first invocation clones
every repository in your Github account. Repeated invocations will run `git
pull` in already-cloned repositories, and will clone repositories that don't
exist locally.

Currently, `bugh` only mirrors the master branch of each repository; future
versions will allow mirroring all branches in a repository. It also does not
support mirroring private repositories.

`bugh` is made by [Will Haldean Brown][1] and is distributed under the GPLv3.

[1]:http://haldean.org
