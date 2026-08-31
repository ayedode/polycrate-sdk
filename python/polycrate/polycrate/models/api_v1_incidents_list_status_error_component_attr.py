from typing import Literal

ApiV1IncidentsListStatusErrorComponentAttr = Literal["status"]

API_V1_INCIDENTS_LIST_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1IncidentsListStatusErrorComponentAttr] = {
    "status",
}


def check_api_v1_incidents_list_status_error_component_attr(value: str) -> ApiV1IncidentsListStatusErrorComponentAttr:
    if value in API_V1_INCIDENTS_LIST_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_LIST_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
