from typing import Literal

ApiV1BlocksCheckCreateChangelogPolyRawErrorComponentAttr = Literal["changelog_poly_raw"]

API_V1_BLOCKS_CHECK_CREATE_CHANGELOG_POLY_RAW_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksCheckCreateChangelogPolyRawErrorComponentAttr
] = {
    "changelog_poly_raw",
}


def check_api_v1_blocks_check_create_changelog_poly_raw_error_component_attr(
    value: str,
) -> ApiV1BlocksCheckCreateChangelogPolyRawErrorComponentAttr:
    if value in API_V1_BLOCKS_CHECK_CREATE_CHANGELOG_POLY_RAW_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_CHANGELOG_POLY_RAW_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
