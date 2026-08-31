from typing import Literal

ApiV1IncidentsListSinceErrorComponentCode = Literal["invalid"]

API_V1_INCIDENTS_LIST_SINCE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1IncidentsListSinceErrorComponentCode] = {
    "invalid",
}


def check_api_v1_incidents_list_since_error_component_code(value: str) -> ApiV1IncidentsListSinceErrorComponentCode:
    if value in API_V1_INCIDENTS_LIST_SINCE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_LIST_SINCE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
