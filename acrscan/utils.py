#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import ffmpeg
import os
import logging
from fuzzywuzzy import fuzz
import time

logger = logging.getLogger(__name__)


def convert_media_file_to_wav(media_filename: str) -> str:
    """
    Convert the media file to wav.
    :param media_filename:
    :return:
    """

    if os.path.splitext(media_filename)[1] == '.wav':
        logger.debug(f'source file is already wav format, there is no need to convert the format. {media_filename}')
        return media_filename

    wav_filename = f'{os.path.splitext(media_filename)[0]}.wav'

    if os.path.exists(wav_filename):
        logger.debug(f'wav file already exsits, delete it.')
        os.remove(wav_filename)

    logger.debug(f'convert the media file to wav')

    ffmpeg.input(media_filename).output(wav_filename, **{'loglevel': 'quiet', 'ac': 1, 'ar': 8000}).run()

    logger.debug(f'Finished the convert task')

    if os.path.exists(wav_filename):
        return wav_filename

    return ''


def is_title_similar_or_equal(title_a: str, title_b: str, threshold: int) -> bool:
    """
    Determine if two strings are similar
    :param title_a:
    :param title_b:
    :param threshold:
    :return:
    """
    if fuzz.token_set_ratio(title_a, title_b) >= threshold:
        return True
    return False


def get_human_readable_time(seconds: int) -> str:
    """
    convert seconds to hh:mm:ss format
    :param seconds:
    :return:
    """
    return time.strftime("%H:%M:%S", time.gmtime(seconds))