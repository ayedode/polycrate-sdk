from typing import Literal

ApiV1PrefixesArchiveCreateDescriptionErrorComponentCode = Literal[
    "invalid", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_PREFIXES_ARCHIVE_CREATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PrefixesArchiveCreateDescriptionErrorComponentCode
] = {
    "invalid",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_prefixes_archive_create_description_error_component_code(
    value: str,
) -> ApiV1PrefixesArchiveCreateDescriptionErrorComponentCode:
    if value in API_V1_PREFIXES_ARCHIVE_CREATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_ARCHIVE_CREATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
