from typing import Literal

ApiV1IncidentsCreateOccurredAtErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "null", "overflow", "required"
]

API_V1_INCIDENTS_CREATE_OCCURRED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IncidentsCreateOccurredAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "null",
    "overflow",
    "required",
}


def check_api_v1_incidents_create_occurred_at_error_component_code(
    value: str,
) -> ApiV1IncidentsCreateOccurredAtErrorComponentCode:
    if value in API_V1_INCIDENTS_CREATE_OCCURRED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_CREATE_OCCURRED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
