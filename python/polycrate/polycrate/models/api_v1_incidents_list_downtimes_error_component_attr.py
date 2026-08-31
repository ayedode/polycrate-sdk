from typing import Literal

ApiV1IncidentsListDowntimesErrorComponentAttr = Literal["downtimes"]

API_V1_INCIDENTS_LIST_DOWNTIMES_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1IncidentsListDowntimesErrorComponentAttr] = {
    "downtimes",
}


def check_api_v1_incidents_list_downtimes_error_component_attr(
    value: str,
) -> ApiV1IncidentsListDowntimesErrorComponentAttr:
    if value in API_V1_INCIDENTS_LIST_DOWNTIMES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_LIST_DOWNTIMES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
