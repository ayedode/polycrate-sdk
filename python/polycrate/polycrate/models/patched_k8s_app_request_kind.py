from typing import Literal

PatchedK8SAppRequestKind = Literal["external", "helm", "polycrate"]

PATCHED_K8S_APP_REQUEST_KIND_VALUES: set[PatchedK8SAppRequestKind] = {
    "external",
    "helm",
    "polycrate",
}


def check_patched_k8s_app_request_kind(value: str) -> PatchedK8SAppRequestKind:
    if value in PATCHED_K8S_APP_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_K8S_APP_REQUEST_KIND_VALUES!r}")
