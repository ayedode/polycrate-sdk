from typing import Literal

ApiV1IncidentsPartialUpdateResolvedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_INCIDENTS_PARTIAL_UPDATE_RESOLVED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IncidentsPartialUpdateResolvedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_incidents_partial_update_resolved_at_error_component_code(
    value: str,
) -> ApiV1IncidentsPartialUpdateResolvedAtErrorComponentCode:
    if value in API_V1_INCIDENTS_PARTIAL_UPDATE_RESOLVED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_PARTIAL_UPDATE_RESOLVED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
