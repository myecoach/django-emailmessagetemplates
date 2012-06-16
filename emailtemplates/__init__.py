"""
Tools for sending templated emails
"""

from models import EmailMessageTemplate, Log
from utils import send_mail, send_mass_mail, mail_admins, mail_managers

__all__ = [EmailMessageTemplate, Log, send_mail,
           send_mass_mail, mail_admins, mail_managers]
