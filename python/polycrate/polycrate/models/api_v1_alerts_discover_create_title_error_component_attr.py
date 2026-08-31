from typing import Literal

ApiV1AlertsDiscoverCreateTitleErrorComponentAttr = Literal["title"]

API_V1_ALERTS_DISCOVER_CREATE_TITLE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsDiscoverCreateTitleErrorComponentAttr
] = {
    "title",
}


def check_api_v1_alerts_discover_create_title_error_component_attr(
    value: str,
) -> ApiV1AlertsDiscoverCreateTitleErrorComponentAttr:
    if value in API_V1_ALERTS_DISCOVER_CREATE_TITLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_DISCOVER_CREATE_TITLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
