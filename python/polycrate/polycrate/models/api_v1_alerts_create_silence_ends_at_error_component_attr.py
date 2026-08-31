from typing import Literal

ApiV1AlertsCreateSilenceEndsAtErrorComponentAttr = Literal["silence_ends_at"]

API_V1_ALERTS_CREATE_SILENCE_ENDS_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsCreateSilenceEndsAtErrorComponentAttr
] = {
    "silence_ends_at",
}


def check_api_v1_alerts_create_silence_ends_at_error_component_attr(
    value: str,
) -> ApiV1AlertsCreateSilenceEndsAtErrorComponentAttr:
    if value in API_V1_ALERTS_CREATE_SILENCE_ENDS_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_CREATE_SILENCE_ENDS_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
