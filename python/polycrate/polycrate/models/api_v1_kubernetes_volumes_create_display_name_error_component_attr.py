from typing import Literal

ApiV1KubernetesVolumesCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_KUBERNETES_VOLUMES_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_kubernetes_volumes_create_display_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesCreateDisplayNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
