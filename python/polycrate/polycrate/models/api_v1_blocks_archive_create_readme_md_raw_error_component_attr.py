from typing import Literal

ApiV1BlocksArchiveCreateReadmeMdRawErrorComponentAttr = Literal["readme_md_raw"]

API_V1_BLOCKS_ARCHIVE_CREATE_README_MD_RAW_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksArchiveCreateReadmeMdRawErrorComponentAttr
] = {
    "readme_md_raw",
}


def check_api_v1_blocks_archive_create_readme_md_raw_error_component_attr(
    value: str,
) -> ApiV1BlocksArchiveCreateReadmeMdRawErrorComponentAttr:
    if value in API_V1_BLOCKS_ARCHIVE_CREATE_README_MD_RAW_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_ARCHIVE_CREATE_README_MD_RAW_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
