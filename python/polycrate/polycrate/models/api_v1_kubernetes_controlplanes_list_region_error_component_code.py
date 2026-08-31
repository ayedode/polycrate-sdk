from typing import Literal

ApiV1KubernetesControlplanesListRegionErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_KUBERNETES_CONTROLPLANES_LIST_REGION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesControlplanesListRegionErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_kubernetes_controlplanes_list_region_error_component_code(
    value: str,
) -> ApiV1KubernetesControlplanesListRegionErrorComponentCode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_LIST_REGION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_LIST_REGION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
