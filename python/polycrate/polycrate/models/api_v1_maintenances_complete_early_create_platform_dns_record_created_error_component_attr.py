from typing import Literal

ApiV1MaintenancesCompleteEarlyCreatePlatformDnsRecordCreatedErrorComponentAttr = Literal["platform_dns_record_created"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreatePlatformDnsRecordCreatedErrorComponentAttr
] = {
    "platform_dns_record_created",
}


def check_api_v1_maintenances_complete_early_create_platform_dns_record_created_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreatePlatformDnsRecordCreatedErrorComponentAttr:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
