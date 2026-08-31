from typing import Literal

ApiV1KubernetesVolumesPartialUpdateVolumeModeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_VOLUME_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesVolumesPartialUpdateVolumeModeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_kubernetes_volumes_partial_update_volume_mode_error_component_code(
    value: str,
) -> ApiV1KubernetesVolumesPartialUpdateVolumeModeErrorComponentCode:
    if value in API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_VOLUME_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_VOLUME_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
