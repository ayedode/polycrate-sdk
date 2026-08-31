from typing import Literal

ApiV1KubernetesVolumesCreateAccessModesErrorComponentAttr = Literal["access_modes"]

API_V1_KUBERNETES_VOLUMES_CREATE_ACCESS_MODES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesCreateAccessModesErrorComponentAttr
] = {
    "access_modes",
}


def check_api_v1_kubernetes_volumes_create_access_modes_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesCreateAccessModesErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_CREATE_ACCESS_MODES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_CREATE_ACCESS_MODES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
