from typing import Literal

ApiV1IncidentsUpdateStatusErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_INCIDENTS_UPDATE_STATUS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1IncidentsUpdateStatusErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_incidents_update_status_error_component_code(
    value: str,
) -> ApiV1IncidentsUpdateStatusErrorComponentCode:
    if value in API_V1_INCIDENTS_UPDATE_STATUS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_UPDATE_STATUS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
