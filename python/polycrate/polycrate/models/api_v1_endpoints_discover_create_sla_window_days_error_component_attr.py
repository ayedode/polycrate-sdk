from typing import Literal

ApiV1EndpointsDiscoverCreateSlaWindowDaysErrorComponentAttr = Literal["sla_window_days"]

API_V1_ENDPOINTS_DISCOVER_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsDiscoverCreateSlaWindowDaysErrorComponentAttr
] = {
    "sla_window_days",
}


def check_api_v1_endpoints_discover_create_sla_window_days_error_component_attr(
    value: str,
) -> ApiV1EndpointsDiscoverCreateSlaWindowDaysErrorComponentAttr:
    if value in API_V1_ENDPOINTS_DISCOVER_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_DISCOVER_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
