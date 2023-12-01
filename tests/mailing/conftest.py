from datetime import datetime

import pytest

from mailing.schemas import MailingCreate


@pytest.fixture
def mailings_data():
    mailings = [
        MailingCreate(start=datetime.utcnow(), message="test mailing №:1"),
        MailingCreate(start=datetime.utcnow(), message="test mailing №:2"),
        MailingCreate(start=datetime.utcnow(), message="test mailing №:3"),
        MailingCreate(start=datetime.utcnow(), message="test mailing №:4"),
        MailingCreate(start=datetime.utcnow(), message="test mailing №:5"),
    ]
    return mailings
