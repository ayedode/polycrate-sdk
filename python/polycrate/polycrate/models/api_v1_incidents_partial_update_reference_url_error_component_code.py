from typing import Literal

ApiV1IncidentsPartialUpdateReferenceUrlErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_INCIDENTS_PARTIAL_UPDATE_REFERENCE_URL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IncidentsPartialUpdateReferenceUrlErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_incidents_partial_update_reference_url_error_component_code(
    value: str,
) -> ApiV1IncidentsPartialUpdateReferenceUrlErrorComponentCode:
    if value in API_V1_INCIDENTS_PARTIAL_UPDATE_REFERENCE_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_PARTIAL_UPDATE_REFERENCE_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
