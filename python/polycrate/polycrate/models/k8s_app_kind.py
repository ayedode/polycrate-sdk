from typing import Literal

K8SAppKind = Literal["external", "helm", "polycrate"]

K8S_APP_KIND_VALUES: set[K8SAppKind] = {
    "external",
    "helm",
    "polycrate",
}


def check_k8s_app_kind(value: str) -> K8SAppKind:
    if value in K8S_APP_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_APP_KIND_VALUES!r}")
