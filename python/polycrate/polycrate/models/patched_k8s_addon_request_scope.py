from typing import Literal

PatchedK8SAddonRequestScope = Literal["system", "user"]

PATCHED_K8S_ADDON_REQUEST_SCOPE_VALUES: set[PatchedK8SAddonRequestScope] = {
    "system",
    "user",
}


def check_patched_k8s_addon_request_scope(value: str) -> PatchedK8SAddonRequestScope:
    if value in PATCHED_K8S_ADDON_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_K8S_ADDON_REQUEST_SCOPE_VALUES!r}")
