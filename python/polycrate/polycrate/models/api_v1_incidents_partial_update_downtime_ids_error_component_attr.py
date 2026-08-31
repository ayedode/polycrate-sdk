from typing import Literal

ApiV1IncidentsPartialUpdateDowntimeIdsErrorComponentAttr = Literal["downtime_ids"]

API_V1_INCIDENTS_PARTIAL_UPDATE_DOWNTIME_IDS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsPartialUpdateDowntimeIdsErrorComponentAttr
] = {
    "downtime_ids",
}


def check_api_v1_incidents_partial_update_downtime_ids_error_component_attr(
    value: str,
) -> ApiV1IncidentsPartialUpdateDowntimeIdsErrorComponentAttr:
    if value in API_V1_INCIDENTS_PARTIAL_UPDATE_DOWNTIME_IDS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_PARTIAL_UPDATE_DOWNTIME_IDS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
