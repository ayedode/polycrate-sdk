from typing import Literal

ApiV1DowntimesListIncidentsErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_DOWNTIMES_LIST_INCIDENTS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1DowntimesListIncidentsErrorComponentCode] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_downtimes_list_incidents_error_component_code(
    value: str,
) -> ApiV1DowntimesListIncidentsErrorComponentCode:
    if value in API_V1_DOWNTIMES_LIST_INCIDENTS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_LIST_INCIDENTS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
