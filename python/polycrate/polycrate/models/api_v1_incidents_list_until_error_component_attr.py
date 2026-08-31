from typing import Literal

ApiV1IncidentsListUntilErrorComponentAttr = Literal["until"]

API_V1_INCIDENTS_LIST_UNTIL_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1IncidentsListUntilErrorComponentAttr] = {
    "until",
}


def check_api_v1_incidents_list_until_error_component_attr(value: str) -> ApiV1IncidentsListUntilErrorComponentAttr:
    if value in API_V1_INCIDENTS_LIST_UNTIL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_LIST_UNTIL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
