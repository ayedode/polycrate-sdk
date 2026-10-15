from typing import Literal

PatchedK8SAddonConfigRevisionRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PATCHED_K8S_ADDON_CONFIG_REVISION_REQUEST_CRITICALITY_TYPE_1_VALUES: set[
    PatchedK8SAddonConfigRevisionRequestCriticalityType1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_k8s_addon_config_revision_request_criticality_type_1(
    value: str,
) -> PatchedK8SAddonConfigRevisionRequestCriticalityType1:
    if value in PATCHED_K8S_ADDON_CONFIG_REVISION_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_K8S_ADDON_CONFIG_REVISION_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
