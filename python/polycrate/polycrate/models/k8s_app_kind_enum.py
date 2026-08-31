from typing import Literal

K8SAppKindEnum = Literal["external", "helm", "polycrate"]

K8S_APP_KIND_ENUM_VALUES: set[K8SAppKindEnum] = {
    "external",
    "helm",
    "polycrate",
}


def check_k8s_app_kind_enum(value: str) -> K8SAppKindEnum:
    if value in K8S_APP_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_APP_KIND_ENUM_VALUES!r}")
