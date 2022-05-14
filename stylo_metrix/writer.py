import os
from datetime import datetime

import numpy as np
import pandas as pd

from stylo_metrix.utils import mean, median, stdev


def write_csv(
        docs,
        target_path,
        name,
        codes,
        descriptions,
        aggregate,
        filenames,
        transpose,
        time):
    if not os.path.exists(target_path):
        os.makedirs(target_path)
        print(f">>> Created directory {target_path}")

    filename = f"{target_path}/{name}" + (f"_{_get_time()}" if time else "") + ".csv"

    data = np.array([doc._.sm.get_values() for doc in docs], dtype=float)
    names = []
    if aggregate:
        data = np.vstack([np.apply_along_axis(stdev, 0, data), data])
        data = np.vstack([np.apply_along_axis(mean, 0, data[1:]), data])
        data = np.vstack([np.apply_along_axis(median, 0, data[2:]), data])
        names.extend(["MEDIAN", "MEAN", "SD"])

    data = [[str(num).replace('.', ',') for num in row] for row in data]

    if descriptions:
        data = np.vstack([docs[0]._.sm.get_names(), data])
        names.insert(0, "DESCRIPTION")
    if codes:
        data = np.vstack([docs[0]._.sm.get_codes(), data])
        names.insert(0, "CODE")

    if filenames:
        names.extend([doc._.name for doc in docs])
        data = np.hstack([np.expand_dims(np.array(names), 0).T, data])

    if transpose:
        data = data.T

    # np.savetxt(filename, data, delimiter=";", fmt="%s") # fails writing Polish special chars in Linux
    df = pd.DataFrame(data)
    df.to_csv(filename, sep=';', encoding='utf-8-sig', header=False, index=False)
    print(f">>> Saved output as {filename}")


def write_npy(
        docs,
        target_path,
        name,
        transpose,
        time):
    filename = f"{target_path}/{name}" + (f"_{_get_time()}" if time else "") + ".npy"
    data = np.array([doc._.sm.get_values() for doc in docs])
    if transpose:
        data = data.T
    np.save(filename, data)
    print(f">>> Saved output as {filename}")


def write_text(content, path):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)


def _get_time():
    return datetime.now().strftime("%Y-%m-%d_%H-%M")
