from typing import Literal

ApiV1AlertsUpdateArchivedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_ALERTS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AlertsUpdateArchivedAtErrorComponentCode] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_alerts_update_archived_at_error_component_code(
    value: str,
) -> ApiV1AlertsUpdateArchivedAtErrorComponentCode:
    if value in API_V1_ALERTS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
