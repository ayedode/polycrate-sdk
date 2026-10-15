from typing import Literal

PatchedK8SAddonRequestEnforcement = Literal["optional", "recommended", "required"]

PATCHED_K8S_ADDON_REQUEST_ENFORCEMENT_VALUES: set[PatchedK8SAddonRequestEnforcement] = {
    "optional",
    "recommended",
    "required",
}


def check_patched_k8s_addon_request_enforcement(value: str) -> PatchedK8SAddonRequestEnforcement:
    if value in PATCHED_K8S_ADDON_REQUEST_ENFORCEMENT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_K8S_ADDON_REQUEST_ENFORCEMENT_VALUES!r}")
