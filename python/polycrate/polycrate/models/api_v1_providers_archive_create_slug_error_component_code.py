from typing import Literal

ApiV1ProvidersArchiveCreateSlugErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed", "unique"
]

API_V1_PROVIDERS_ARCHIVE_CREATE_SLUG_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProvidersArchiveCreateSlugErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
    "unique",
}


def check_api_v1_providers_archive_create_slug_error_component_code(
    value: str,
) -> ApiV1ProvidersArchiveCreateSlugErrorComponentCode:
    if value in API_V1_PROVIDERS_ARCHIVE_CREATE_SLUG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ARCHIVE_CREATE_SLUG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
