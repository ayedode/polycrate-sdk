from typing import Literal

ApiV1OrganizationsCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_ORGANIZATIONS_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_organizations_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1OrganizationsCreateReconciliationEnabledErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
