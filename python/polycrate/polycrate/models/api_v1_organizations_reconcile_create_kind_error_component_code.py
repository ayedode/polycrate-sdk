from typing import Literal

ApiV1OrganizationsReconcileCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsReconcileCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_organizations_reconcile_create_kind_error_component_code(
    value: str,
) -> ApiV1OrganizationsReconcileCreateKindErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
