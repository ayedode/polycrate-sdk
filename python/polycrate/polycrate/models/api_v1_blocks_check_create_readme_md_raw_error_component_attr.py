from typing import Literal

ApiV1BlocksCheckCreateReadmeMdRawErrorComponentAttr = Literal["readme_md_raw"]

API_V1_BLOCKS_CHECK_CREATE_README_MD_RAW_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksCheckCreateReadmeMdRawErrorComponentAttr
] = {
    "readme_md_raw",
}


def check_api_v1_blocks_check_create_readme_md_raw_error_component_attr(
    value: str,
) -> ApiV1BlocksCheckCreateReadmeMdRawErrorComponentAttr:
    if value in API_V1_BLOCKS_CHECK_CREATE_README_MD_RAW_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_README_MD_RAW_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
