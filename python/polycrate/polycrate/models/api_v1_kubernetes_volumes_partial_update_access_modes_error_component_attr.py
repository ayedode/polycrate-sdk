from typing import Literal

ApiV1KubernetesVolumesPartialUpdateAccessModesErrorComponentAttr = Literal["access_modes"]

API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_ACCESS_MODES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesPartialUpdateAccessModesErrorComponentAttr
] = {
    "access_modes",
}


def check_api_v1_kubernetes_volumes_partial_update_access_modes_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesPartialUpdateAccessModesErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_ACCESS_MODES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_ACCESS_MODES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
