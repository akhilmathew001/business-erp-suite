'''
Created on May 2, 2017

@author: Akhil Mathew
'''

import logging
import pdb
from datetime import datetime
from django.contrib.auth.signals import user_logged_in,user_logged_out
from django.dispatch import receiver

@receiver(user_logged_in)
def user_logged_in_logger(sender, user, request, **kwargs):
    #Call back function for the user_logged_in signal
    log = logging.getLogger(__name__)
    current_time = datetime.now()
    log.info('User %s logged in at %s',(user,current_time))
    
@receiver(user_logged_out)
def user_logged_out_logger(sender, user, request, **kwargs):
    #Call back function for the user_logged_out signal
    log = logging.getLogger(__name__)
    current_time = datetime.now()
    log.info('User %s logged in at %s',(user,current_time))   
