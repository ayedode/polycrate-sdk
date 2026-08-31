from typing import Literal

ApiV1AlertsDiscoverCreateLastSeenErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_ALERTS_DISCOVER_CREATE_LAST_SEEN_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsDiscoverCreateLastSeenErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_alerts_discover_create_last_seen_error_component_code(
    value: str,
) -> ApiV1AlertsDiscoverCreateLastSeenErrorComponentCode:
    if value in API_V1_ALERTS_DISCOVER_CREATE_LAST_SEEN_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_DISCOVER_CREATE_LAST_SEEN_ERROR_COMPONENT_CODE_VALUES!r}"
    )
