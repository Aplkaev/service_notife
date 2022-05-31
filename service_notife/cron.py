import logging
from django.utils.timezone import utc

from .models import Mailing
from datetime import datetime

from .classes.CustomerMailing import CustomerMailing


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def check_mailing():
    logger.info("start")

    m = Mailing.objects.filter(start_time__lte=datetime.utcnow().replace(tzinfo=utc), end_time__gte=datetime.utcnow().replace(tzinfo=utc))
    for i in m:
        logger.info("send_mailing"+str(i.id))
        mailing = CustomerMailing(i.id)
        mailing.start()
        del mailing

    logger.info("end")