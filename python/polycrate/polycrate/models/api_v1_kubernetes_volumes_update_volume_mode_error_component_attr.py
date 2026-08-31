from typing import Literal

ApiV1KubernetesVolumesUpdateVolumeModeErrorComponentAttr = Literal["volume_mode"]

API_V1_KUBERNETES_VOLUMES_UPDATE_VOLUME_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesUpdateVolumeModeErrorComponentAttr
] = {
    "volume_mode",
}


def check_api_v1_kubernetes_volumes_update_volume_mode_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesUpdateVolumeModeErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_UPDATE_VOLUME_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_UPDATE_VOLUME_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
