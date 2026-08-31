from typing import Literal

ApiV1AlertsDiscoverCreateSilenceEndsAtErrorComponentAttr = Literal["silence_ends_at"]

API_V1_ALERTS_DISCOVER_CREATE_SILENCE_ENDS_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsDiscoverCreateSilenceEndsAtErrorComponentAttr
] = {
    "silence_ends_at",
}


def check_api_v1_alerts_discover_create_silence_ends_at_error_component_attr(
    value: str,
) -> ApiV1AlertsDiscoverCreateSilenceEndsAtErrorComponentAttr:
    if value in API_V1_ALERTS_DISCOVER_CREATE_SILENCE_ENDS_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_DISCOVER_CREATE_SILENCE_ENDS_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
