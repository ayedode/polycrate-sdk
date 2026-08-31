from typing import Literal

ApiV1BlocksArchiveCreateChangelogPolyRawErrorComponentCode = Literal[
    "invalid", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCKS_ARCHIVE_CREATE_CHANGELOG_POLY_RAW_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksArchiveCreateChangelogPolyRawErrorComponentCode
] = {
    "invalid",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_blocks_archive_create_changelog_poly_raw_error_component_code(
    value: str,
) -> ApiV1BlocksArchiveCreateChangelogPolyRawErrorComponentCode:
    if value in API_V1_BLOCKS_ARCHIVE_CREATE_CHANGELOG_POLY_RAW_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_ARCHIVE_CREATE_CHANGELOG_POLY_RAW_ERROR_COMPONENT_CODE_VALUES!r}"
    )
