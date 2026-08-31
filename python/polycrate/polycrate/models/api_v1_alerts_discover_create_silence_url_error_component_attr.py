from typing import Literal

ApiV1AlertsDiscoverCreateSilenceUrlErrorComponentAttr = Literal["silence_url"]

API_V1_ALERTS_DISCOVER_CREATE_SILENCE_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsDiscoverCreateSilenceUrlErrorComponentAttr
] = {
    "silence_url",
}


def check_api_v1_alerts_discover_create_silence_url_error_component_attr(
    value: str,
) -> ApiV1AlertsDiscoverCreateSilenceUrlErrorComponentAttr:
    if value in API_V1_ALERTS_DISCOVER_CREATE_SILENCE_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_DISCOVER_CREATE_SILENCE_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
