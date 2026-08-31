from typing import Literal

ApiV1AlertsUpdateSilenceEndsAtErrorComponentAttr = Literal["silence_ends_at"]

API_V1_ALERTS_UPDATE_SILENCE_ENDS_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsUpdateSilenceEndsAtErrorComponentAttr
] = {
    "silence_ends_at",
}


def check_api_v1_alerts_update_silence_ends_at_error_component_attr(
    value: str,
) -> ApiV1AlertsUpdateSilenceEndsAtErrorComponentAttr:
    if value in API_V1_ALERTS_UPDATE_SILENCE_ENDS_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_UPDATE_SILENCE_ENDS_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
