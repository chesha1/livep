#!/bin/bash
mv /root/record_files/[2-4]* /root/OneDrive/录播存档/
onedrive --synchronize --upload-only --no-remote-delete
onedrive --synchronize --upload-only --no-remote-delete
rm -rf /root/OneDrive/录播存档/*
