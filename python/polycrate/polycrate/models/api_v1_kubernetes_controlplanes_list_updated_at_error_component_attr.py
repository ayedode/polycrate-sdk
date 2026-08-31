from typing import Literal

ApiV1KubernetesControlplanesListUpdatedAtErrorComponentAttr = Literal["updated_at"]

API_V1_KUBERNETES_CONTROLPLANES_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesListUpdatedAtErrorComponentAttr
] = {
    "updated_at",
}


def check_api_v1_kubernetes_controlplanes_list_updated_at_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesListUpdatedAtErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
