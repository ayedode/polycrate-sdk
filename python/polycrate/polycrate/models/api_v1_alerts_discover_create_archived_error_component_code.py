from typing import Literal

ApiV1AlertsDiscoverCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_ALERTS_DISCOVER_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsDiscoverCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_alerts_discover_create_archived_error_component_code(
    value: str,
) -> ApiV1AlertsDiscoverCreateArchivedErrorComponentCode:
    if value in API_V1_ALERTS_DISCOVER_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_DISCOVER_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
