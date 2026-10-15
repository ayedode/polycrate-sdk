from typing import Literal

K8SAddonEnforcement = Literal["optional", "recommended", "required"]

K8S_ADDON_ENFORCEMENT_VALUES: set[K8SAddonEnforcement] = {
    "optional",
    "recommended",
    "required",
}


def check_k8s_addon_enforcement(value: str) -> K8SAddonEnforcement:
    if value in K8S_ADDON_ENFORCEMENT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_ADDON_ENFORCEMENT_VALUES!r}")
