from typing import Literal

ApiV1IncidentsCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_INCIDENTS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[ApiV1IncidentsCreateKindErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_incidents_create_kind_error_component_code(value: str) -> ApiV1IncidentsCreateKindErrorComponentCode:
    if value in API_V1_INCIDENTS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
