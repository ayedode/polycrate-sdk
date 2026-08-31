from typing import Literal

ApiV1KubernetesVolumesArchiveCreateCloudProviderVolumeIdErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_CLOUD_PROVIDER_VOLUME_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesVolumesArchiveCreateCloudProviderVolumeIdErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_volumes_archive_create_cloud_provider_volume_id_error_component_code(
    value: str,
) -> ApiV1KubernetesVolumesArchiveCreateCloudProviderVolumeIdErrorComponentCode:
    if value in API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_CLOUD_PROVIDER_VOLUME_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_CLOUD_PROVIDER_VOLUME_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
