from typing import Literal

SloObjectType = Literal["Endpoint", "K8sCluster"]

SLO_OBJECT_TYPE_VALUES: set[SloObjectType] = {
    "Endpoint",
    "K8sCluster",
}


def check_slo_object_type(value: str) -> SloObjectType:
    if value in SLO_OBJECT_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SLO_OBJECT_TYPE_VALUES!r}")
