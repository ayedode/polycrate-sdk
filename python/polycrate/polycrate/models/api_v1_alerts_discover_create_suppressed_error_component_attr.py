from typing import Literal

ApiV1AlertsDiscoverCreateSuppressedErrorComponentAttr = Literal["suppressed"]

API_V1_ALERTS_DISCOVER_CREATE_SUPPRESSED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsDiscoverCreateSuppressedErrorComponentAttr
] = {
    "suppressed",
}


def check_api_v1_alerts_discover_create_suppressed_error_component_attr(
    value: str,
) -> ApiV1AlertsDiscoverCreateSuppressedErrorComponentAttr:
    if value in API_V1_ALERTS_DISCOVER_CREATE_SUPPRESSED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_DISCOVER_CREATE_SUPPRESSED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
