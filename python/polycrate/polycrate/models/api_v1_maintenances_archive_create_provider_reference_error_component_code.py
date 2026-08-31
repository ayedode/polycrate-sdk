from typing import Literal

ApiV1MaintenancesArchiveCreateProviderReferenceErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_MAINTENANCES_ARCHIVE_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesArchiveCreateProviderReferenceErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_maintenances_archive_create_provider_reference_error_component_code(
    value: str,
) -> ApiV1MaintenancesArchiveCreateProviderReferenceErrorComponentCode:
    if value in API_V1_MAINTENANCES_ARCHIVE_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_ARCHIVE_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
