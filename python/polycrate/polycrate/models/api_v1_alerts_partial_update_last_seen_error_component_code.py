from typing import Literal

ApiV1AlertsPartialUpdateLastSeenErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_ALERTS_PARTIAL_UPDATE_LAST_SEEN_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsPartialUpdateLastSeenErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_alerts_partial_update_last_seen_error_component_code(
    value: str,
) -> ApiV1AlertsPartialUpdateLastSeenErrorComponentCode:
    if value in API_V1_ALERTS_PARTIAL_UPDATE_LAST_SEEN_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_PARTIAL_UPDATE_LAST_SEEN_ERROR_COMPONENT_CODE_VALUES!r}"
    )
