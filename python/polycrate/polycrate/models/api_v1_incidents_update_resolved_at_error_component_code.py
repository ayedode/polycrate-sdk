from typing import Literal

ApiV1IncidentsUpdateResolvedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_INCIDENTS_UPDATE_RESOLVED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IncidentsUpdateResolvedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_incidents_update_resolved_at_error_component_code(
    value: str,
) -> ApiV1IncidentsUpdateResolvedAtErrorComponentCode:
    if value in API_V1_INCIDENTS_UPDATE_RESOLVED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_UPDATE_RESOLVED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
