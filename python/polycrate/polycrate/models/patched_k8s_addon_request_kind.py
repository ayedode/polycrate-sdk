from typing import Literal

PatchedK8SAddonRequestKind = Literal["generic"]

PATCHED_K8S_ADDON_REQUEST_KIND_VALUES: set[PatchedK8SAddonRequestKind] = {
    "generic",
}


def check_patched_k8s_addon_request_kind(value: str) -> PatchedK8SAddonRequestKind:
    if value in PATCHED_K8S_ADDON_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_K8S_ADDON_REQUEST_KIND_VALUES!r}")
