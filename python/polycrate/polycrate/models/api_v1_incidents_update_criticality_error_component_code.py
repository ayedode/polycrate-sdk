from typing import Literal

ApiV1IncidentsUpdateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_INCIDENTS_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IncidentsUpdateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_incidents_update_criticality_error_component_code(
    value: str,
) -> ApiV1IncidentsUpdateCriticalityErrorComponentCode:
    if value in API_V1_INCIDENTS_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
