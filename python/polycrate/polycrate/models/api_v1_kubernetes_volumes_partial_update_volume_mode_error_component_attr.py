from typing import Literal

ApiV1KubernetesVolumesPartialUpdateVolumeModeErrorComponentAttr = Literal["volume_mode"]

API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_VOLUME_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesPartialUpdateVolumeModeErrorComponentAttr
] = {
    "volume_mode",
}


def check_api_v1_kubernetes_volumes_partial_update_volume_mode_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesPartialUpdateVolumeModeErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_VOLUME_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_VOLUME_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
