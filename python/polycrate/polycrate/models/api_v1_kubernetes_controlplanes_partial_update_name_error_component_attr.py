from typing import Literal

ApiV1KubernetesControlplanesPartialUpdateNameErrorComponentAttr = Literal["name"]

API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesPartialUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_kubernetes_controlplanes_partial_update_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesPartialUpdateNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
