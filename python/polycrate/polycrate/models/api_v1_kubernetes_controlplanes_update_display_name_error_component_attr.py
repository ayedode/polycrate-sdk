from typing import Literal

ApiV1KubernetesControlplanesUpdateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_KUBERNETES_CONTROLPLANES_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesUpdateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_kubernetes_controlplanes_update_display_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesUpdateDisplayNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
