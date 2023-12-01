#!/bin/bash

celery -A celery_:clr worker --loglevel=info --pool=solo