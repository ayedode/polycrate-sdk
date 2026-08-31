from typing import Literal

ApiV1SecretmanagerManagersArchiveCreateDisplayNameErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1SecretmanagerManagersArchiveCreateDisplayNameErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_secretmanager_managers_archive_create_display_name_error_component_code(
    value: str,
) -> ApiV1SecretmanagerManagersArchiveCreateDisplayNameErrorComponentCode:
    if value in API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
