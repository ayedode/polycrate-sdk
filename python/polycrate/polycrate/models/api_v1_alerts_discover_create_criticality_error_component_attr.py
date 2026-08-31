from typing import Literal

ApiV1AlertsDiscoverCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_ALERTS_DISCOVER_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsDiscoverCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_alerts_discover_create_criticality_error_component_attr(
    value: str,
) -> ApiV1AlertsDiscoverCreateCriticalityErrorComponentAttr:
    if value in API_V1_ALERTS_DISCOVER_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_DISCOVER_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
