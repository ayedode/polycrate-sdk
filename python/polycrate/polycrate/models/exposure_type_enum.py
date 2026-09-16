from typing import Literal

ExposureTypeEnum = Literal["gateway", "ingress", "loadbalancer"]

EXPOSURE_TYPE_ENUM_VALUES: set[ExposureTypeEnum] = {
    "gateway",
    "ingress",
    "loadbalancer",
}


def check_exposure_type_enum(value: str) -> ExposureTypeEnum:
    if value in EXPOSURE_TYPE_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {EXPOSURE_TYPE_ENUM_VALUES!r}")
