from typing import Literal

ApiV1AlertsDiscoverCreateLastSeenErrorComponentAttr = Literal["last_seen"]

API_V1_ALERTS_DISCOVER_CREATE_LAST_SEEN_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsDiscoverCreateLastSeenErrorComponentAttr
] = {
    "last_seen",
}


def check_api_v1_alerts_discover_create_last_seen_error_component_attr(
    value: str,
) -> ApiV1AlertsDiscoverCreateLastSeenErrorComponentAttr:
    if value in API_V1_ALERTS_DISCOVER_CREATE_LAST_SEEN_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_DISCOVER_CREATE_LAST_SEEN_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
