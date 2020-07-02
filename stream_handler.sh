#!/bin/bash

HOME=/home/wesley
NGXLOG=/var/log/nginx
LOGDIR=/home/wesley/nginxlogs
GRGX="Linux\|Ubuntu\|Android\|Windows\|Macintosh\|iPhone"
SRGX='.*\[([0-9][0-9]\/[^ ]+\/[0-9][0-9][0-9][0-9]).*(\(.*?;.*\)).*'

sudo cat $NGXLOG/access.log | grep $GRGX | sed -E "s/$SRGX/\1\--\2/" |  sort | uniq -c >> $LOGDIR/log
