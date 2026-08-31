from typing import Literal

ApiV1OrganizationsReconcileCreatePriorityErrorComponentCode = Literal["invalid", "null"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_PRIORITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsReconcileCreatePriorityErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_organizations_reconcile_create_priority_error_component_code(
    value: str,
) -> ApiV1OrganizationsReconcileCreatePriorityErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_PRIORITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_PRIORITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
