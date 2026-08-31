from typing import Literal

ApiV1OrganizationsReconcileCreateActiveErrorComponentCode = Literal["invalid", "null"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsReconcileCreateActiveErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_organizations_reconcile_create_active_error_component_code(
    value: str,
) -> ApiV1OrganizationsReconcileCreateActiveErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
