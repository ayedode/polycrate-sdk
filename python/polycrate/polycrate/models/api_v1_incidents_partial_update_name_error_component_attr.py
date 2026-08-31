from typing import Literal

ApiV1IncidentsPartialUpdateNameErrorComponentAttr = Literal["name"]

API_V1_INCIDENTS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsPartialUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_incidents_partial_update_name_error_component_attr(
    value: str,
) -> ApiV1IncidentsPartialUpdateNameErrorComponentAttr:
    if value in API_V1_INCIDENTS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
