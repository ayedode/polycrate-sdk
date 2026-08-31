from typing import Literal

ApiV1IncidentsListDowntimesErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_INCIDENTS_LIST_DOWNTIMES_ERROR_COMPONENT_CODE_VALUES: set[ApiV1IncidentsListDowntimesErrorComponentCode] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_incidents_list_downtimes_error_component_code(
    value: str,
) -> ApiV1IncidentsListDowntimesErrorComponentCode:
    if value in API_V1_INCIDENTS_LIST_DOWNTIMES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_LIST_DOWNTIMES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
