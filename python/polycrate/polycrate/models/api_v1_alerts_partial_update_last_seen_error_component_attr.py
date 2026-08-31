from typing import Literal

ApiV1AlertsPartialUpdateLastSeenErrorComponentAttr = Literal["last_seen"]

API_V1_ALERTS_PARTIAL_UPDATE_LAST_SEEN_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsPartialUpdateLastSeenErrorComponentAttr
] = {
    "last_seen",
}


def check_api_v1_alerts_partial_update_last_seen_error_component_attr(
    value: str,
) -> ApiV1AlertsPartialUpdateLastSeenErrorComponentAttr:
    if value in API_V1_ALERTS_PARTIAL_UPDATE_LAST_SEEN_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_PARTIAL_UPDATE_LAST_SEEN_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
