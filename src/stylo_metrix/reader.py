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


import os
import re


def get_filepaths(dir_path):
    if not os.path.isdir(dir_path):
        raise Exception
    data = [os.path.join(dir_path, file) for file in os.listdir(dir_path) if file.lower().endswith('.txt')]
    if len(data) == 0:
        raise Exception
    data.sort(key=str.lower)
    return data


def read_file(path, accept_empty):
    def is_empty(content):
        return re.search(r'^\s*$', content)

    def get_filename(path):
        return os.path.split(path)[1][:-4]

    if not path.lower().endswith('.txt'):
        raise Exception
    try:
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
            if not accept_empty and is_empty(content):
                raise Exception
            content = content.replace("radem", "rodem")  # patch na KeyError w nlp("radem") po stronie Morfeusza
            name = get_filename(path)
            return name, content
    except FileNotFoundError:
        raise Exception
    except OSError:
        raise Exception
    except Exception:
        raise Exception
