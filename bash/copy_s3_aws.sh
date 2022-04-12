#!/usr/bin/env bash

# AWS CREDS
export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""
export AWS_SESSION_TOKEN=""

# check if the first two command lines are passed in when calling bashcript
if [ -z "$1" ] 
then
    echo "Pass in as first argument the environemnt: ['dev', 'staging', 'production']
    Aborting..."

    exit 0
elif [ -z "$2" ]
then 
    echo "Pass in as second argument the logstream type: ['data-provider', 'scraper-response', 'search-logs']
    Aborting..."

    exit 0
fi



# check the first command line argument have valid values
if [ $1 == 'dev' ] || [ $1 == 'prod' ]
then
    echo "$1 is a valid first command line argument, continuing..."
else
    echo "$1 is an invalid first command line argument, please enter one of these: ['dev', 'prod']"
    exit 0
fi



# check the second command line argument have valid values
if [ $2 == 'data-provider' ] || [ $2 == 'scraper-response' ] || [ $2 == 'search-logs' ]
then
    echo "$2 is a valid second command line argument, continuing..."
else
    echo "$2 is an invalid second command line argument, please enter one of these: ['data-provider', 'scraper-response', 'search-logs']"
    exit 0
fi


case $2 in
  "data-provider")
    aws s3 cp \
    --recursive \
    --include "*" \
    --exclude "*search-logs*" \
    --exclude "*scraper-response*" \
    "s3://some-origin-bucket" "s3://some-destination-bucket-$1/eventbridge/data-provider-response-logs/"
    ;;

  "scraper-response")
    aws s3 cp \
    --recursive \
    --include "*" \
    --exclude "*search-logs*" \
    --exclude "*data-provider*" \
    "s3://some-origin-bucket" "s3://some-destination-bucket-$1/eventbridge/scraper-response-logs/"
    ;;

  "search-logs")
    aws s3 cp \
    --recursive \
    --include "*" \
    --exclude "*scraper-response*" \
    --exclude "*data-provider*" \
    "s3://some-origin-bucket" "s3://some-destination-bucket-$1/eventbridge/search-logs/"
    ;;

  *)
    echo -n "Didnt copy any files, please use a proper logstream pattern as second command line argument!"
    exit 0
    ;;
esac

echo "Finished Copying the files!"