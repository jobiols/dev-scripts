# dev-scripts
###Docker based  infrastructure management for _Odoo_ 

This proyect support [semver](http://semver.org/) 
    
usage: odooenv.py [-h] [-p] [-i] [-R] [-S] [-r] [-s] [-l] [-v] [-n] [-u]
                  [-d DATABASE] [-w NEW_DATABASE] [-m MODULE] [-c CLIENT]
                  [--debug] [--no-dbfilter] [--no-repos] [-H] [--backup]
                  [--backup-list] [--restore] [-t TIMESTAMP]
                  [-Q repo test_file] [-j] [--cron-list] [--translate]
                  [--issues REPO] [-T--tag-repos]
                  [--checkout-tag CHECKOUT_TAG] [--undo-checkout-tag]

    ==========================================================================
    Odoo environment setup v4.2.1 by jeo Software <jorge.obiols@gmail.com>
    ==========================================================================
    
    optional arguments:
      -h, --help            show this help message and exit
      -p, --pull-all        Pull all images and repos for a client, need a -c
                            option
      -i, --install-cli     Install client, requires -c option. Pull repos and
                            generate odoo config file
      -R, --run-env         Run database and aeroo images.
      -S, --stop-env        Stop database and aeroo images.
      -r, --run-cli         Run client odoo images, requires -c options. Optional
      -s, --stop-cli        Stop client images, requires -c options.
      -l, --list            List all data in this server. Clients and images. with
                            --issues REPO list the github issues from repo
      -v, --verbose         Go verbose mode. Prints every command
      -n, --no-ip-install   Install no-ip on this server. Experimental
      -u, --update-db       Update database requires -d -c and -m options.
      -d DATABASE           Database name.
      -w NEW_DATABASE       New database name. Only for restore command
      -m MODULE             Module to update or all for updating all the
                            reegistered modules, you can specify multiple -m
                            options.
      -c CLIENT             Client name.
      --debug               This option has three efects: 1.- when doing an update
                            database, (option -u) it forces debug mode. 2.- When
                            running environment (option -R) it opens port 5432 to
                            access postgres server databases. 3.- when doing a
                            pull (option -p) it clones the full repo i.e. does not
                            issue --depth 1 to git
      --no-dbfilter         Eliminates dbfilter: The client can see any database.
                            Without this, the client can only see databases
                            starting with clientname_
      --no-repos            Does not clone or pull repos used with -i or -p
      -H, --server-help     List server help requires -c option (because needs to
                            run a image)
      --backup              Lauch backup. requires -d and -c options.
      --backup-list         List available backups with timestamps to restore.
      --restore             Launch restore requires -c, -d, -w and -t options.
      -t TIMESTAMP          Timestamp to restore database, see --backup-list for
                            available timestamps.
      -Q repo test_file, --quality-test repo test_file
                            Perform a test, arguments are Repo where test lives,
                            and yml/py test file to run (please include
                            extension). Need -d, -m and -c options Note: for the
                            test to run there must be an admin user with password
                            admin
      -j, --cron-jobs       Cron Backup. it adds cron jobs for doing backup to a
                            client database. backups twice a day at 12 AM and 12
                            PM. Needs a -c option to tell which client to backup.
      --cron-list           List available cron jobs
      --translate           Generate a po file for a module to translate, need a
                            -r and -m option
      --issues REPO         list formatted and priorized issues from github, used
                            with -l this option supports github API v3 priority is
                            the number between brackets in issue titleTHIS COMMAND
                            IS DEPRECATED IN FAVOR OF GITHUB PROJECTS
      -T--tag-repos         Tag all repos used by a client with a tag consisting
                            of client name and a timestamp. Need -c option
      --checkout-tag CHECKOUT_TAG
                            checkouts a tag from all the repos belonging to a
                            client needs -c option. If some repo does not have the
                            tag, reports the error and continues with next
                            repo.The tag was previously setted with -T option. To
                            undo this situation issue a --undo-checkout-tag
      --undo-checkout-tag   checkouts the normal branch (i.e. odoo version) for
                            all the repos belonging to the client. Needs -c
                            option. This revers the the repos modifyed for a
                            --checkout-tag to its normal state. Warning: if there
                            is any local change in a repo, the checkout will fail.
