ansible-role-postfix
********************

Ansible role to setup Postfix


Variables
=========

postfix_package
   System package with Postfix.

   Default:

      postfix

postfix_default_release
   Default Postfix package release.

   Default: ""

postfix_service
   Postfix system service name.

   Default:

      {{ postfix_package }}

postfix_enabled
   Should Postfix service be enabled.

   Default:

      True

postfix_state
   Postfix service state.

   Default:

      started

postfix_conf_dir
   Directory with Postfix configuration file.

   Default:

      /etc/postfix

postfix_main_conf_template
   Main configuration file template.

   Default:

      main.cf.j2

postfix_master_conf_template
   Master configuration file template.

   Default:

      master.cf.j2

postfix_main_conf_file
   Main Postfix configuration file's path.

   Default:

      {{ postfix_conf_dir }}/main.cf

postfix_master_conf_file
   Master Postfix configuration file's path.

   Default:

      {{ postfix_conf_dir }}/master.cf

postfix_lookups
   Postfix lookup tables configuration files, e.g.:

      senders-sqlite.cf: |-
        dbpath = /var/vmail/mail.db
        query = SELECT username || '@' || domain FROM user WHERE username || '@' || domain = '%s'

   Default:

      {}

postfix_sqlite
   Should install SQLite extension.

   Default:

      True

postfix_sqlite_package
   Package with Postfix SQLite extension.

   Default:

      postfix-sqlite

postfix_conf
   Postfix configuration mapping.

   Default:

      {alias_database: 'hash:/etc/aliases', alias_maps: 'hash:/etc/aliases', append_dot_mydomain: 'no',
        biff: 'no', compatibility_level: '2', inet_interfaces: localhost, inet_protocols: ipv4,
        mailbox_size_limit: '0', mydestination: '$myhostname, {{ ansible_facts.hostname
          }}, localhost.localdomain, , localhost', myhostname: '{{ ansible_facts.fqdn }}',
        mynetworks: '127.0.0.0/8 [::ffff:127.0.0.0]/104 [::1]/128', myorigin: /etc/mailname,
        readme_directory: 'no', recipient_delimiter: +, relayhost: '', smtp_tls_session_cache_database: 'btree:${data_directory}/smtp_scache',
        smtpd_banner: $myhostname ESMTP $mail_name, smtpd_relay_restrictions: permit_mynetworks
          permit_sasl_authenticated defer_unauth_destination, smtpd_tls_cert_file: /etc/ssl/certs/ssl-cert-snakeoil.pem,
        smtpd_tls_key_file: /etc/ssl/private/ssl-cert-snakeoil.key, smtpd_tls_session_cache_database: 'btree:${data_directory}/smtpd_scache',
        smtpd_use_tls: 'yes'}

postfix_services
   master.cf entries.

   Default:

      - {chroot: y, command: smtpd, maxproc: '-', name: smtp, private: n, type: inet, unpriv: '-',
        wakeup: '-'}
      - {chroot: y, command: pickup, maxproc: '1', name: pickup, private: n, type: unix,
        unpriv: '-', wakeup: '60'}
      - {chroot: y, command: cleanup, maxproc: '0', name: cleanup, private: n, type: unix,
        unpriv: '-', wakeup: '-'}
      - {chroot: n, command: qmgr, maxproc: '1', name: qmgr, private: n, type: unix, unpriv: '-',
        wakeup: '300'}
      - {chroot: y, command: tlsmgr, maxproc: '1', name: tlsmgr, private: '-', type: unix,
        unpriv: '-', wakeup: '1000?'}
      - {chroot: y, command: trivial-rewrite, maxproc: '-', name: rewrite, private: '-',
        type: unix, unpriv: '-', wakeup: '-'}
      - {chroot: y, command: bounce, maxproc: '0', name: bounce, private: '-', type: unix,
        unpriv: '-', wakeup: '-'}
      - {chroot: y, command: bounce, maxproc: '0', name: defer, private: '-', type: unix,
        unpriv: '-', wakeup: '-'}
      - {chroot: y, command: bounce, maxproc: '0', name: trace, private: '-', type: unix,
        unpriv: '-', wakeup: '-'}
      - {chroot: y, command: verify, maxproc: '1', name: verify, private: '-', type: unix,
        unpriv: '-', wakeup: '-'}
      - {chroot: y, command: flush, maxproc: '0', name: flush, private: n, type: unix, unpriv: '-',
        wakeup: '1000?'}
      - {chroot: n, command: proxymap, maxproc: '-', name: proxymap, private: '-', type: unix,
        unpriv: '-', wakeup: '-'}
      - {chroot: n, command: proxymap, maxproc: '1', name: proxywrite, private: '-', type: unix,
        unpriv: '-', wakeup: '-'}
      - {chroot: y, command: smtp, maxproc: '-', name: smtp, private: '-', type: unix, unpriv: '-',
        wakeup: '-'}
      - {chroot: y, command: smtp, maxproc: '-', name: relay, private: '-', type: unix,
        unpriv: '-', wakeup: '-'}
      - {chroot: y, command: showq, maxproc: '-', name: showq, private: n, type: unix, unpriv: '-',
        wakeup: '-'}
      - {chroot: y, command: error, maxproc: '-', name: error, private: '-', type: unix,
        unpriv: '-', wakeup: '-'}
      - {chroot: y, command: error, maxproc: '-', name: retry, private: '-', type: unix,
        unpriv: '-', wakeup: '-'}
      - {chroot: y, command: discard, maxproc: '-', name: discard, private: '-', type: unix,
        unpriv: '-', wakeup: '-'}
      - {chroot: n, command: local, maxproc: '-', name: local, private: '-', type: unix,
        unpriv: n, wakeup: '-'}
      - {chroot: n, command: virtual, maxproc: '-', name: virtual, private: '-', type: unix,
        unpriv: n, wakeup: '-'}
      - {chroot: y, command: lmtp, maxproc: '-', name: lmtp, private: '-', type: unix, unpriv: '-',
        wakeup: '-'}
      - {chroot: y, command: anvil, maxproc: '1', name: anvil, private: '-', type: unix,
        unpriv: '-', wakeup: '-'}
      - {chroot: y, command: scache, maxproc: '1', name: scache, private: '-', type: unix,
        unpriv: '-', wakeup: '-'}
      - args: [flags=Fqhu user=uucp argv=uux -r -n -z -a$sender - $nexthop!rmail ($recipient)]
        chroot: n
        command: pipe
        maxproc: '-'
        name: maildrop
        private: '-'
        type: unix
        unpriv: n
        wakeup: '-'
      - args: [flags=Fqhu user=uucp argv=uux -r -n -z -a$sender - $nexthop!rmail ($recipient)]
        chroot: n
        command: pipe
        maxproc: '-'
        name: uucp
        private: '-'
        type: unix
        unpriv: n
        wakeup: '-'
      - args: [flags=F user=ftn argv=/usr/lib/ifmail/ifmail -r $nexthop ($recipient)]
        chroot: n
        command: pipe
        maxproc: '-'
        name: ifmail
        private: '-'
        type: unix
        unpriv: n
        wakeup: '-'
      - args: [flags=Fq. user=bsmtp argv=/usr/lib/bsmtp/bsmtp -t$nexthop -f$sender $recipient]
        chroot: n
        command: pipe
        maxproc: '-'
        name: bsmtp
        private: '-'
        type: unix
        unpriv: n
        wakeup: '-'
      - args: ['flags=R user=scalemail argv=/usr/lib/scalemail/bin/scalemail-store ${nexthop}
            ${user} ${extension}']
        chroot: n
        command: pipe
        maxproc: '2'
        name: scalemail-backend
        private: '-'
        type: unix
        unpriv: n
        wakeup: '-'
      - args: [flags=FR user=list argv=/usr/lib/mailman/bin/postfix-to-mailman.py, '${nexthop}
            ${user}']
        chroot: n
        command: pipe
        maxproc: '-'
        name: mailman
        private: '-'
        type: unix
        unpriv: n
        wakeup: '-'


Examples
========

   ---
   - hosts: instance
     tasks:
       - name: Install mailx for tests
         apt:
           name: bsd-mailx

       - name: Create /etc/mailname
         copy:
           content: "{{ ansible_facts.hostname }}\n"
           dest: /etc/mailname
           owner: root
           group: root
           mode: 0644

       - import_role:
           name: postfix


Documentation
=============

Compile:

   $ pip3 install -r requirements.txt
   $ make man

View:

   $ man ./docs/man/ansible-role-postfix.1
