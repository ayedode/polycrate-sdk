from typing import Literal

K8SAppRequestKind = Literal["external", "helm", "polycrate"]

K8S_APP_REQUEST_KIND_VALUES: set[K8SAppRequestKind] = {
    "external",
    "helm",
    "polycrate",
}


def check_k8s_app_request_kind(value: str) -> K8SAppRequestKind:
    if value in K8S_APP_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_APP_REQUEST_KIND_VALUES!r}")
