from typing import Literal

ApiV1IncidentsUpdateResolvedAtErrorComponentAttr = Literal["resolved_at"]

API_V1_INCIDENTS_UPDATE_RESOLVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsUpdateResolvedAtErrorComponentAttr
] = {
    "resolved_at",
}


def check_api_v1_incidents_update_resolved_at_error_component_attr(
    value: str,
) -> ApiV1IncidentsUpdateResolvedAtErrorComponentAttr:
    if value in API_V1_INCIDENTS_UPDATE_RESOLVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_UPDATE_RESOLVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
