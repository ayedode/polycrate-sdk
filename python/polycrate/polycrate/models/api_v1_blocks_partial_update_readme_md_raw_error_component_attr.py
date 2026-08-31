from typing import Literal

ApiV1BlocksPartialUpdateReadmeMdRawErrorComponentAttr = Literal["readme_md_raw"]

API_V1_BLOCKS_PARTIAL_UPDATE_README_MD_RAW_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksPartialUpdateReadmeMdRawErrorComponentAttr
] = {
    "readme_md_raw",
}


def check_api_v1_blocks_partial_update_readme_md_raw_error_component_attr(
    value: str,
) -> ApiV1BlocksPartialUpdateReadmeMdRawErrorComponentAttr:
    if value in API_V1_BLOCKS_PARTIAL_UPDATE_README_MD_RAW_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PARTIAL_UPDATE_README_MD_RAW_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
