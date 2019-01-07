import os
import time
import uuid

import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_postfix_running(host):
    assert host.service('postfix').is_running


def test_postfix_enabled(host):
    assert host.service('postfix').is_enabled


def test_smtp_port_listening(host):
    assert host.socket('tcp://127.0.0.1:25').is_listening


def test_local_mail_relay(host):
    subject = uuid.uuid4().hex
    mailbox = '/var/spool/mail/root'
    host.run_expect([0], 'echo | mail root -s "%s"' % (subject))
    time.sleep(1)
    assert host.file(mailbox).contains('Subject: %s' % (subject))
    host.run('rm -f %s' % (mailbox))
