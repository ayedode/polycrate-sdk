from typing import Literal

ApiV1KubernetesControlplanesCreateNameErrorComponentAttr = Literal["name"]

API_V1_KUBERNETES_CONTROLPLANES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_kubernetes_controlplanes_create_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesCreateNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
