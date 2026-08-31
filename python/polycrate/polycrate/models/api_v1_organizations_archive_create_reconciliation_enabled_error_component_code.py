from typing import Literal

ApiV1OrganizationsArchiveCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsArchiveCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_organizations_archive_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1OrganizationsArchiveCreateReconciliationEnabledErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
