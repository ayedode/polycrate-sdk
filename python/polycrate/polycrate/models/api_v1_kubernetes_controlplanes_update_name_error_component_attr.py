from typing import Literal

ApiV1KubernetesControlplanesUpdateNameErrorComponentAttr = Literal["name"]

API_V1_KUBERNETES_CONTROLPLANES_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_kubernetes_controlplanes_update_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesUpdateNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
