from typing import Literal

ApiV1IncidentsPartialUpdateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_INCIDENTS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IncidentsPartialUpdateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_incidents_partial_update_archived_error_component_code(
    value: str,
) -> ApiV1IncidentsPartialUpdateArchivedErrorComponentCode:
    if value in API_V1_INCIDENTS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
