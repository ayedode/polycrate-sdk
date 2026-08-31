from typing import Literal

ApiV1IncidentsPartialUpdateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_INCIDENTS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IncidentsPartialUpdateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_incidents_partial_update_criticality_error_component_code(
    value: str,
) -> ApiV1IncidentsPartialUpdateCriticalityErrorComponentCode:
    if value in API_V1_INCIDENTS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
