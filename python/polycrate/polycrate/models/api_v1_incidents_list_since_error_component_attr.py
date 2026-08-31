from typing import Literal

ApiV1IncidentsListSinceErrorComponentAttr = Literal["since"]

API_V1_INCIDENTS_LIST_SINCE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1IncidentsListSinceErrorComponentAttr] = {
    "since",
}


def check_api_v1_incidents_list_since_error_component_attr(value: str) -> ApiV1IncidentsListSinceErrorComponentAttr:
    if value in API_V1_INCIDENTS_LIST_SINCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_LIST_SINCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
