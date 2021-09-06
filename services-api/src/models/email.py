# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, EmailStr, Field, validator
from enum import Enum, IntEnum


# Shared properties


class EmailModel(BaseModel):
    """
    base of email model
    """
    to_email: List[EmailStr] =Field(..., title="To Email", description="Email address to send to")
    cc_email: List[EmailStr] =Field(..., title="CC Email", description="Email address to send to")
    bcc_email: List[EmailStr] =Field(..., title="BCC Email", description="Email address to send to")
    from_email: EmailStr=Field(..., title="From Email", description="Email address to send from")
    subject: EmailStr=Field(..., title="Subject", description="Email subject",example="New Order")
    body: EmailStr=Field(..., title="Body", description="Email body",example="Hello,\n\nThis is a test email.\n\nThanks,\n\nThe Dev Set Go Team")