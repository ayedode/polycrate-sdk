from typing import Literal

ApiV1KubernetesVolumesPartialUpdateAccessModesErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_ACCESS_MODES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesVolumesPartialUpdateAccessModesErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_volumes_partial_update_access_modes_error_component_code(
    value: str,
) -> ApiV1KubernetesVolumesPartialUpdateAccessModesErrorComponentCode:
    if value in API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_ACCESS_MODES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_ACCESS_MODES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
