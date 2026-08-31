from typing import Literal

ApiV1DomainsDomainsArchiveCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainsArchiveCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_domains_domains_archive_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1DomainsDomainsArchiveCreateReconciliationEnabledErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
