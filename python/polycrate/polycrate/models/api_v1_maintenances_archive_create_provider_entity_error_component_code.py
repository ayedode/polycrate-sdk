from typing import Literal

ApiV1MaintenancesArchiveCreateProviderEntityErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_MAINTENANCES_ARCHIVE_CREATE_PROVIDER_ENTITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesArchiveCreateProviderEntityErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_maintenances_archive_create_provider_entity_error_component_code(
    value: str,
) -> ApiV1MaintenancesArchiveCreateProviderEntityErrorComponentCode:
    if value in API_V1_MAINTENANCES_ARCHIVE_CREATE_PROVIDER_ENTITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_ARCHIVE_CREATE_PROVIDER_ENTITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
