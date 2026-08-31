from typing import Literal

ApiV1IncidentsUpdateDowntimeIdsErrorComponentAttr = Literal["downtime_ids"]

API_V1_INCIDENTS_UPDATE_DOWNTIME_IDS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsUpdateDowntimeIdsErrorComponentAttr
] = {
    "downtime_ids",
}


def check_api_v1_incidents_update_downtime_ids_error_component_attr(
    value: str,
) -> ApiV1IncidentsUpdateDowntimeIdsErrorComponentAttr:
    if value in API_V1_INCIDENTS_UPDATE_DOWNTIME_IDS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_UPDATE_DOWNTIME_IDS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
