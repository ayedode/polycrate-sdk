from typing import Literal

ApiV1AlertsDiscoverCreateBlockErrorComponentAttr = Literal["block"]

API_V1_ALERTS_DISCOVER_CREATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsDiscoverCreateBlockErrorComponentAttr
] = {
    "block",
}


def check_api_v1_alerts_discover_create_block_error_component_attr(
    value: str,
) -> ApiV1AlertsDiscoverCreateBlockErrorComponentAttr:
    if value in API_V1_ALERTS_DISCOVER_CREATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_DISCOVER_CREATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
