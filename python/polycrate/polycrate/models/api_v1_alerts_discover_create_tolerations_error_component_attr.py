from typing import Literal

ApiV1AlertsDiscoverCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_ALERTS_DISCOVER_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsDiscoverCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_alerts_discover_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1AlertsDiscoverCreateTolerationsErrorComponentAttr:
    if value in API_V1_ALERTS_DISCOVER_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_DISCOVER_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
