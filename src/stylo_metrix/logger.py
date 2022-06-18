# Copyright (C) 2022  NASK PIB
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import logging
import os
import sys
APP_LOGGER_NAME = 'LOGGER'
LOG_PATH = "../../log"
DEFAULT_LOG_FILE = "general.log"


def setup_logger(logger_name = APP_LOGGER_NAME):
    file_name = get_logging_path()
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    # sh = logging.StreamHandler(sys.stdout)
    # sh.setFormatter(formatter)
    logger.handlers.clear()
    # logger.addHandler(sh)
    fh = logging.FileHandler(file_name, mode='a')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger


def get_logger(module_name):
   return logging.getLogger(APP_LOGGER_NAME).getChild(module_name)


def get_logging_path():
    path = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), LOG_PATH), DEFAULT_LOG_FILE)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return path
