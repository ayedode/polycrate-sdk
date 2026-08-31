from typing import Literal

ApiV1MaintenancesCreatePlatformDnsRecordCreatedErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCES_CREATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesCreatePlatformDnsRecordCreatedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenances_create_platform_dns_record_created_error_component_code(
    value: str,
) -> ApiV1MaintenancesCreatePlatformDnsRecordCreatedErrorComponentCode:
    if value in API_V1_MAINTENANCES_CREATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_CREATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
