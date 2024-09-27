#!/usr/bin/python

from distutils.dir_util import copy_tree

backup_directory = '/all_media/backup'

def run_backup_process():
    copy_tree('/home/spikeygg/printer_data/spoolman/backups', '{}/spoolman'.format(backup_directory))

if __name__ == '__main__':
    run_backup_process()
