from typing import Literal

SloObjectTypeEnum = Literal["Endpoint", "K8sCluster"]

SLO_OBJECT_TYPE_ENUM_VALUES: set[SloObjectTypeEnum] = {
    "Endpoint",
    "K8sCluster",
}


def check_slo_object_type_enum(value: str) -> SloObjectTypeEnum:
    if value in SLO_OBJECT_TYPE_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SLO_OBJECT_TYPE_ENUM_VALUES!r}")
