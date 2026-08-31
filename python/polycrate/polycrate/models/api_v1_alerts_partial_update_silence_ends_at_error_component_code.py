from typing import Literal

ApiV1AlertsPartialUpdateSilenceEndsAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_ALERTS_PARTIAL_UPDATE_SILENCE_ENDS_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsPartialUpdateSilenceEndsAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_alerts_partial_update_silence_ends_at_error_component_code(
    value: str,
) -> ApiV1AlertsPartialUpdateSilenceEndsAtErrorComponentCode:
    if value in API_V1_ALERTS_PARTIAL_UPDATE_SILENCE_ENDS_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_PARTIAL_UPDATE_SILENCE_ENDS_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
