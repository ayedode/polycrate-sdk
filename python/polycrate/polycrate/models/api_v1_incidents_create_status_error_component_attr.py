from typing import Literal

ApiV1IncidentsCreateStatusErrorComponentAttr = Literal["status"]

API_V1_INCIDENTS_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1IncidentsCreateStatusErrorComponentAttr] = {
    "status",
}


def check_api_v1_incidents_create_status_error_component_attr(
    value: str,
) -> ApiV1IncidentsCreateStatusErrorComponentAttr:
    if value in API_V1_INCIDENTS_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
