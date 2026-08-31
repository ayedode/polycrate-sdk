from typing import Literal

ApiV1IncidentsListUntilErrorComponentCode = Literal["invalid"]

API_V1_INCIDENTS_LIST_UNTIL_ERROR_COMPONENT_CODE_VALUES: set[ApiV1IncidentsListUntilErrorComponentCode] = {
    "invalid",
}


def check_api_v1_incidents_list_until_error_component_code(value: str) -> ApiV1IncidentsListUntilErrorComponentCode:
    if value in API_V1_INCIDENTS_LIST_UNTIL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_LIST_UNTIL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
