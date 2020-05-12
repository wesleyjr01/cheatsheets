#! /bin/bash
WORKDIR="/var/www/html/pricing-service"
LOGFILE=$HOME/pricing.log
date >> $LOGFILE

source $WORKDIR/venv/bin/activate
python $WORKDIR/alert_updater.py >> $LOGFILE
echo >> $LOGFILE
