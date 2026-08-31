from typing import Literal

ApiV1BlocksRunDiscoveryCreateChangelogPolyRawErrorComponentAttr = Literal["changelog_poly_raw"]

API_V1_BLOCKS_RUN_DISCOVERY_CREATE_CHANGELOG_POLY_RAW_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRunDiscoveryCreateChangelogPolyRawErrorComponentAttr
] = {
    "changelog_poly_raw",
}


def check_api_v1_blocks_run_discovery_create_changelog_poly_raw_error_component_attr(
    value: str,
) -> ApiV1BlocksRunDiscoveryCreateChangelogPolyRawErrorComponentAttr:
    if value in API_V1_BLOCKS_RUN_DISCOVERY_CREATE_CHANGELOG_POLY_RAW_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RUN_DISCOVERY_CREATE_CHANGELOG_POLY_RAW_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
