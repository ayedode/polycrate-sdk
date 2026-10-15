from typing import Literal

K8SAddonRequestEnforcement = Literal["optional", "recommended", "required"]

K8S_ADDON_REQUEST_ENFORCEMENT_VALUES: set[K8SAddonRequestEnforcement] = {
    "optional",
    "recommended",
    "required",
}


def check_k8s_addon_request_enforcement(value: str) -> K8SAddonRequestEnforcement:
    if value in K8S_ADDON_REQUEST_ENFORCEMENT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_ADDON_REQUEST_ENFORCEMENT_VALUES!r}")
