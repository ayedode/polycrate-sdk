from typing import Literal

ApiV1BlocksRepairCreateReadmeMdRawErrorComponentAttr = Literal["readme_md_raw"]

API_V1_BLOCKS_REPAIR_CREATE_README_MD_RAW_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRepairCreateReadmeMdRawErrorComponentAttr
] = {
    "readme_md_raw",
}


def check_api_v1_blocks_repair_create_readme_md_raw_error_component_attr(
    value: str,
) -> ApiV1BlocksRepairCreateReadmeMdRawErrorComponentAttr:
    if value in API_V1_BLOCKS_REPAIR_CREATE_README_MD_RAW_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_REPAIR_CREATE_README_MD_RAW_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
