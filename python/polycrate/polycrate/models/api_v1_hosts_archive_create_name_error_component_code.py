from typing import Literal

ApiV1HostsArchiveCreateNameErrorComponentCode = Literal[
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
]

API_V1_HOSTS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES: set[ApiV1HostsArchiveCreateNameErrorComponentCode] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_hosts_archive_create_name_error_component_code(
    value: str,
) -> ApiV1HostsArchiveCreateNameErrorComponentCode:
    if value in API_V1_HOSTS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
