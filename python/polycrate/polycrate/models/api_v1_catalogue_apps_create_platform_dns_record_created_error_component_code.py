from typing import Literal

ApiV1CatalogueAppsCreatePlatformDnsRecordCreatedErrorComponentCode = Literal["invalid", "null"]

API_V1_CATALOGUE_APPS_CREATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsCreatePlatformDnsRecordCreatedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_catalogue_apps_create_platform_dns_record_created_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsCreatePlatformDnsRecordCreatedErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_CREATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_CREATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
