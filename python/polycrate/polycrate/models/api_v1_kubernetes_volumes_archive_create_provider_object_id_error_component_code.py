from typing import Literal

ApiV1KubernetesVolumesArchiveCreateProviderObjectIdErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "required", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_PROVIDER_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesVolumesArchiveCreateProviderObjectIdErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_volumes_archive_create_provider_object_id_error_component_code(
    value: str,
) -> ApiV1KubernetesVolumesArchiveCreateProviderObjectIdErrorComponentCode:
    if value in API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_PROVIDER_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_PROVIDER_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
