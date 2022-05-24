# -*- coding: utf-8 -*-

import os
import time
import sys
import string
import argparse
from collections import namedtuple
from enum import Enum

Result = namedtupe('Result', 'status data')

HTTPStatus = Enum('Status','ok not_found error')

POP20_CC = ('CN IN US ID BR PK NG BD RU JP'
        'MX PH VN ET EG DE IR TR CD FR').split()


