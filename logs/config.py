import logging

logging.basicConfig(
    filename="logs/mailings.log",
    level=logging.INFO,
    filemode="w",
    encoding="utf-8",
    format="%(asctime)s %(filename)s %(levelname)s: %(message)s",
)
mailinglog = logging.getLogger(__name__)
