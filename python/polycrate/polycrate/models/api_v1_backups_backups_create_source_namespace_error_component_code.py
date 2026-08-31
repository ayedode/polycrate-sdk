from typing import Literal

ApiV1BackupsBackupsCreateSourceNamespaceErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BACKUPS_BACKUPS_CREATE_SOURCE_NAMESPACE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupsCreateSourceNamespaceErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_backups_backups_create_source_namespace_error_component_code(
    value: str,
) -> ApiV1BackupsBackupsCreateSourceNamespaceErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUPS_CREATE_SOURCE_NAMESPACE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_CREATE_SOURCE_NAMESPACE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
