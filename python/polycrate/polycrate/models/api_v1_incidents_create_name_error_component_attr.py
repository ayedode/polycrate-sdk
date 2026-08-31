from typing import Literal

ApiV1IncidentsCreateNameErrorComponentAttr = Literal["name"]

API_V1_INCIDENTS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1IncidentsCreateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_incidents_create_name_error_component_attr(value: str) -> ApiV1IncidentsCreateNameErrorComponentAttr:
    if value in API_V1_INCIDENTS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
