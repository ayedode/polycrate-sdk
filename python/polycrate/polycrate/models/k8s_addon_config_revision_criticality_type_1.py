from typing import Literal

K8SAddonConfigRevisionCriticalityType1 = Literal["", "high", "low", "medium"]

K8S_ADDON_CONFIG_REVISION_CRITICALITY_TYPE_1_VALUES: set[K8SAddonConfigRevisionCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_k8s_addon_config_revision_criticality_type_1(value: str) -> K8SAddonConfigRevisionCriticalityType1:
    if value in K8S_ADDON_CONFIG_REVISION_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {K8S_ADDON_CONFIG_REVISION_CRITICALITY_TYPE_1_VALUES!r}"
    )
