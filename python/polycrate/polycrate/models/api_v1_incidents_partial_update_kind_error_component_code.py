from typing import Literal

ApiV1IncidentsPartialUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_INCIDENTS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IncidentsPartialUpdateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_incidents_partial_update_kind_error_component_code(
    value: str,
) -> ApiV1IncidentsPartialUpdateKindErrorComponentCode:
    if value in API_V1_INCIDENTS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
