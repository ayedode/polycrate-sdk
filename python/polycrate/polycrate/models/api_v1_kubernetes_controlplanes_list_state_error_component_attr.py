from typing import Literal

ApiV1KubernetesControlplanesListStateErrorComponentAttr = Literal["state"]

API_V1_KUBERNETES_CONTROLPLANES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesListStateErrorComponentAttr
] = {
    "state",
}


def check_api_v1_kubernetes_controlplanes_list_state_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesListStateErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
