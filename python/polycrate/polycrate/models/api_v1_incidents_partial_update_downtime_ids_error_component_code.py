from typing import Literal

ApiV1IncidentsPartialUpdateDowntimeIdsErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "not_a_list", "null"
]

API_V1_INCIDENTS_PARTIAL_UPDATE_DOWNTIME_IDS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IncidentsPartialUpdateDowntimeIdsErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "not_a_list",
    "null",
}


def check_api_v1_incidents_partial_update_downtime_ids_error_component_code(
    value: str,
) -> ApiV1IncidentsPartialUpdateDowntimeIdsErrorComponentCode:
    if value in API_V1_INCIDENTS_PARTIAL_UPDATE_DOWNTIME_IDS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_PARTIAL_UPDATE_DOWNTIME_IDS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
