from typing import Literal

ApiV1KubernetesControlplanesListRegionErrorComponentAttr = Literal["region"]

API_V1_KUBERNETES_CONTROLPLANES_LIST_REGION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesListRegionErrorComponentAttr
] = {
    "region",
}


def check_api_v1_kubernetes_controlplanes_list_region_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesListRegionErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_LIST_REGION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_LIST_REGION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
