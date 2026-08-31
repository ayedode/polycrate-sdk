from typing import Literal

Role28FEnum = Literal["generic", "k8s-controlplane", "k8s-worker"]

ROLE_28F_ENUM_VALUES: set[Role28FEnum] = {
    "generic",
    "k8s-controlplane",
    "k8s-worker",
}


def check_role_28f_enum(value: str) -> Role28FEnum:
    if value in ROLE_28F_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_28F_ENUM_VALUES!r}")
