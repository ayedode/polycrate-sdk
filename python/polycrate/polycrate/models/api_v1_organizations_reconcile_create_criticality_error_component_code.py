from typing import Literal

ApiV1OrganizationsReconcileCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsReconcileCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_organizations_reconcile_create_criticality_error_component_code(
    value: str,
) -> ApiV1OrganizationsReconcileCreateCriticalityErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
