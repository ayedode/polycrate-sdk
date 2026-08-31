from typing import Literal

ApiV1BlocksCreateReadmeMdRawErrorComponentAttr = Literal["readme_md_raw"]

API_V1_BLOCKS_CREATE_README_MD_RAW_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksCreateReadmeMdRawErrorComponentAttr] = {
    "readme_md_raw",
}


def check_api_v1_blocks_create_readme_md_raw_error_component_attr(
    value: str,
) -> ApiV1BlocksCreateReadmeMdRawErrorComponentAttr:
    if value in API_V1_BLOCKS_CREATE_README_MD_RAW_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CREATE_README_MD_RAW_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
