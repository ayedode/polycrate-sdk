from typing import Literal

ApiV1MaintenancesCreateReferenceUrlErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_MAINTENANCES_CREATE_REFERENCE_URL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesCreateReferenceUrlErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_maintenances_create_reference_url_error_component_code(
    value: str,
) -> ApiV1MaintenancesCreateReferenceUrlErrorComponentCode:
    if value in API_V1_MAINTENANCES_CREATE_REFERENCE_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_CREATE_REFERENCE_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
