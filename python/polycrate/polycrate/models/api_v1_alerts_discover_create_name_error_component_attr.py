from typing import Literal

ApiV1AlertsDiscoverCreateNameErrorComponentAttr = Literal["name"]

API_V1_ALERTS_DISCOVER_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsDiscoverCreateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_alerts_discover_create_name_error_component_attr(
    value: str,
) -> ApiV1AlertsDiscoverCreateNameErrorComponentAttr:
    if value in API_V1_ALERTS_DISCOVER_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_DISCOVER_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
