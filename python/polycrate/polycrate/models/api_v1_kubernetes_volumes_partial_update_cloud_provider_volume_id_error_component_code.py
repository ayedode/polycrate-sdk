from typing import Literal

ApiV1KubernetesVolumesPartialUpdateCloudProviderVolumeIdErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_CLOUD_PROVIDER_VOLUME_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesVolumesPartialUpdateCloudProviderVolumeIdErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_volumes_partial_update_cloud_provider_volume_id_error_component_code(
    value: str,
) -> ApiV1KubernetesVolumesPartialUpdateCloudProviderVolumeIdErrorComponentCode:
    if value in API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_CLOUD_PROVIDER_VOLUME_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_CLOUD_PROVIDER_VOLUME_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
