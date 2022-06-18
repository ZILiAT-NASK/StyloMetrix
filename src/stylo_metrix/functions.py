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


from spacy.tokens import Doc
from stylo_metrix.reader import get_filepaths, read_file
from stylo_metrix.structures import StyloMetrixVector
from stylo_metrix.structures.errors import (
    WrongTypeError,
    EmptyListError,
    EmptyMetricsError,
    MisalignedMetricsError,
)
from stylo_metrix.writer import write_csv, write_npy


def analyze_dir(
        nlp,
        dir_path):
    try:
        files = get_filepaths(dir_path)
        doc_list = []
        for file in files:
            try:
                print(f"Analyzing {file}")
                name, text = read_file(file, True)
                doc = nlp(text)
                doc._.assign_name(name)
                doc_list.append(doc)
            except Exception as e:
                print("File failed", file, str(e))
        return doc_list
    except Exception as e:
        print("Analysis failed", dir_path, str(e))


def analyze_text(
        nlp,
        name,
        text):
    print(f"Analyzing file {name}")
    doc = nlp(text)
    doc._.assign_name(name)
    return doc


def save_csv(
        docs,
        target_path,
        name,
        codes=True,
        descriptions=True,
        aggregate=True,
        filenames=True,
        transpose=False,
        time=False):
    _validate_docs(docs)
    write_csv(docs, target_path, name, codes, descriptions, aggregate, filenames, transpose, time)


def save_npy(
        docs,
        target_path,
        name,
        transpose=False,
        time=False):
    _validate_docs(docs)
    write_npy(docs, target_path, name, transpose, time)


# def save_debug(
#         signatures,
#         target_path,
#         by="metric",
#         time=False):
#     _validate_docs(docs)
#     write_debug(signatures, target_path, by, time)

def add_metric(nlp, function):
    smv_index = [name for name, obj in nlp.components].index('stylo_metrix')
    comp = nlp.components[smv_index][1].components[-1]
    comp.add_metric(function)


def remove_empty_columns(docs_list):
    _validate_docs(docs_list)
    zeros = [{i for i, v in enumerate(doc._.smv) if v["value"] == 0} for doc in docs_list]
    inters = set.intersection(*zeros)
    new_doc_list = docs_list.copy()
    for doc in new_doc_list:
        doc._.smv = StyloMetrixVector(doc._.smv.name, [v for i, v in enumerate(doc._.smv) if i not in inters])
    return new_doc_list


def _validate_docs(docs):
    if not isinstance(docs, (list, tuple)):
        raise WrongTypeError()
    if len(docs) == 0:
        raise EmptyListError()
    if not (all(type(doc) == Doc for doc in docs)
            and all(doc.has_extension("smv") for doc in docs)):
        raise WrongTypeError()
    if len(docs[0]._.smv) == 0:
        raise EmptyMetricsError()
    if len(set("".join(doc._.smv.get_codes()) for doc in docs)) != 1:
        raise MisalignedMetricsError()
