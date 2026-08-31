from typing import Literal

ApiV1BlocksCreateChangelogPolyRawErrorComponentAttr = Literal["changelog_poly_raw"]

API_V1_BLOCKS_CREATE_CHANGELOG_POLY_RAW_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksCreateChangelogPolyRawErrorComponentAttr
] = {
    "changelog_poly_raw",
}


def check_api_v1_blocks_create_changelog_poly_raw_error_component_attr(
    value: str,
) -> ApiV1BlocksCreateChangelogPolyRawErrorComponentAttr:
    if value in API_V1_BLOCKS_CREATE_CHANGELOG_POLY_RAW_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CREATE_CHANGELOG_POLY_RAW_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
