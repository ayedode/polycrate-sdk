from typing import Literal

ApiV1AlertsUpdateLastSeenErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_ALERTS_UPDATE_LAST_SEEN_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AlertsUpdateLastSeenErrorComponentCode] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_alerts_update_last_seen_error_component_code(
    value: str,
) -> ApiV1AlertsUpdateLastSeenErrorComponentCode:
    if value in API_V1_ALERTS_UPDATE_LAST_SEEN_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_UPDATE_LAST_SEEN_ERROR_COMPONENT_CODE_VALUES!r}"
    )
