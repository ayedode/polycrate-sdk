from typing import Literal

ApiV1OrganizationsDiscoverCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsDiscoverCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_organizations_discover_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateReconciliationEnabledErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
