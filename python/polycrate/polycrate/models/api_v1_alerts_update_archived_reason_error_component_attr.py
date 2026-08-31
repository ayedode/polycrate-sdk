from typing import Literal

ApiV1AlertsUpdateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_ALERTS_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsUpdateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_alerts_update_archived_reason_error_component_attr(
    value: str,
) -> ApiV1AlertsUpdateArchivedReasonErrorComponentAttr:
    if value in API_V1_ALERTS_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
