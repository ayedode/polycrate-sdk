from typing import Literal

ApiV1DowntimesListIncidentsErrorComponentAttr = Literal["incidents"]

API_V1_DOWNTIMES_LIST_INCIDENTS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1DowntimesListIncidentsErrorComponentAttr] = {
    "incidents",
}


def check_api_v1_downtimes_list_incidents_error_component_attr(
    value: str,
) -> ApiV1DowntimesListIncidentsErrorComponentAttr:
    if value in API_V1_DOWNTIMES_LIST_INCIDENTS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_LIST_INCIDENTS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
