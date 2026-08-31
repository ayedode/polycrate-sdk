from typing import Literal

ApiV1KubernetesControlplanesPartialUpdateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesPartialUpdateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_kubernetes_controlplanes_partial_update_debug_mode_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesPartialUpdateDebugModeErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
