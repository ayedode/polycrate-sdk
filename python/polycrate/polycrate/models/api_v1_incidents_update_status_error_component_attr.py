from typing import Literal

ApiV1IncidentsUpdateStatusErrorComponentAttr = Literal["status"]

API_V1_INCIDENTS_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1IncidentsUpdateStatusErrorComponentAttr] = {
    "status",
}


def check_api_v1_incidents_update_status_error_component_attr(
    value: str,
) -> ApiV1IncidentsUpdateStatusErrorComponentAttr:
    if value in API_V1_INCIDENTS_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
