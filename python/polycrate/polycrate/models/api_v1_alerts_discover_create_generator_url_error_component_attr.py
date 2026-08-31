from typing import Literal

ApiV1AlertsDiscoverCreateGeneratorUrlErrorComponentAttr = Literal["generator_url"]

API_V1_ALERTS_DISCOVER_CREATE_GENERATOR_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsDiscoverCreateGeneratorUrlErrorComponentAttr
] = {
    "generator_url",
}


def check_api_v1_alerts_discover_create_generator_url_error_component_attr(
    value: str,
) -> ApiV1AlertsDiscoverCreateGeneratorUrlErrorComponentAttr:
    if value in API_V1_ALERTS_DISCOVER_CREATE_GENERATOR_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_DISCOVER_CREATE_GENERATOR_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
