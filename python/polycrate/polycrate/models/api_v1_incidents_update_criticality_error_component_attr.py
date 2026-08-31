from typing import Literal

ApiV1IncidentsUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_INCIDENTS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_incidents_update_criticality_error_component_attr(
    value: str,
) -> ApiV1IncidentsUpdateCriticalityErrorComponentAttr:
    if value in API_V1_INCIDENTS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
