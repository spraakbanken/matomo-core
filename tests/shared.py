import typing as t

from syrupy import matchers


def make_matcher(**kwargs):  # noqa: ANN003, ANN201
    path_types: dict[str, tuple[type[t.Any], ...]] = {"gt_ms": (float,), "rand": (int,)}
    if kwargs:
        path_types.update(kwargs)
    return matchers.path_type(path_types)
