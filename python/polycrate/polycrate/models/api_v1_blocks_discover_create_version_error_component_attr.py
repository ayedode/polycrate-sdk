from typing import Literal

ApiV1BlocksDiscoverCreateVersionErrorComponentAttr = Literal["version"]

API_V1_BLOCKS_DISCOVER_CREATE_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksDiscoverCreateVersionErrorComponentAttr
] = {
    "version",
}


def check_api_v1_blocks_discover_create_version_error_component_attr(
    value: str,
) -> ApiV1BlocksDiscoverCreateVersionErrorComponentAttr:
    if value in API_V1_BLOCKS_DISCOVER_CREATE_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_DISCOVER_CREATE_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
