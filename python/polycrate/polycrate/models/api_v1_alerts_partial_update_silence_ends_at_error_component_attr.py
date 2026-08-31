from typing import Literal

ApiV1AlertsPartialUpdateSilenceEndsAtErrorComponentAttr = Literal["silence_ends_at"]

API_V1_ALERTS_PARTIAL_UPDATE_SILENCE_ENDS_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsPartialUpdateSilenceEndsAtErrorComponentAttr
] = {
    "silence_ends_at",
}


def check_api_v1_alerts_partial_update_silence_ends_at_error_component_attr(
    value: str,
) -> ApiV1AlertsPartialUpdateSilenceEndsAtErrorComponentAttr:
    if value in API_V1_ALERTS_PARTIAL_UPDATE_SILENCE_ENDS_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_PARTIAL_UPDATE_SILENCE_ENDS_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
