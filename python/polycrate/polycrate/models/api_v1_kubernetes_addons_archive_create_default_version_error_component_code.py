from typing import Literal

ApiV1KubernetesAddonsArchiveCreateDefaultVersionErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_DEFAULT_VERSION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonsArchiveCreateDefaultVersionErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_addons_archive_create_default_version_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonsArchiveCreateDefaultVersionErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_DEFAULT_VERSION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_DEFAULT_VERSION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
