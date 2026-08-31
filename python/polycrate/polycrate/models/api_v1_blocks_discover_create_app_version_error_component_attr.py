from typing import Literal

ApiV1BlocksDiscoverCreateAppVersionErrorComponentAttr = Literal["app_version"]

API_V1_BLOCKS_DISCOVER_CREATE_APP_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksDiscoverCreateAppVersionErrorComponentAttr
] = {
    "app_version",
}


def check_api_v1_blocks_discover_create_app_version_error_component_attr(
    value: str,
) -> ApiV1BlocksDiscoverCreateAppVersionErrorComponentAttr:
    if value in API_V1_BLOCKS_DISCOVER_CREATE_APP_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_DISCOVER_CREATE_APP_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
