class StyloMetrixError(Exception):
    msg: str

    def __str__(self):
        return self.msg


class WrongTypeError(StyloMetrixError):
    msg = f"Trying to save wrong datatype (other than list of docs with \"metrics\" attribute)."

    def __init__(self):
        pass

    def __repr__(self):
        return str(self)


class EmptyListError(StyloMetrixError):
    msg = f"Trying to save empty list of StyloMetric vectors."

    def __init__(self):
        pass

    def __repr__(self):
        return str(self)


class AddMetricAlreadyExistsError(StyloMetrixError):
    msg = f"Metric already exists in metrics list."

    def __init__(self):
        pass

    def __repr__(self):
        return str(self)


class EmptyMetricsError(StyloMetrixError):
    msg = f"Trying to write empty vectors of metrics."

    def __init__(self):
        pass

    def __repr__(self):
        return str(self)


class MisalignedMetricsError(StyloMetrixError):
    msg = f"Vectors don't have matching metrics."

    def __init__(self):
        pass

    def __repr__(self):
        return str(self)
