from typing import Literal

ApiV1BlocksArchiveCreateReadmeMdRawErrorComponentCode = Literal[
    "invalid", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCKS_ARCHIVE_CREATE_README_MD_RAW_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksArchiveCreateReadmeMdRawErrorComponentCode
] = {
    "invalid",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_blocks_archive_create_readme_md_raw_error_component_code(
    value: str,
) -> ApiV1BlocksArchiveCreateReadmeMdRawErrorComponentCode:
    if value in API_V1_BLOCKS_ARCHIVE_CREATE_README_MD_RAW_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_ARCHIVE_CREATE_README_MD_RAW_ERROR_COMPONENT_CODE_VALUES!r}"
    )
