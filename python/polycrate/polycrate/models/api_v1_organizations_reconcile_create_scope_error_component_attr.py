from typing import Literal

ApiV1OrganizationsReconcileCreateScopeErrorComponentAttr = Literal["scope"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsReconcileCreateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_organizations_reconcile_create_scope_error_component_attr(
    value: str,
) -> ApiV1OrganizationsReconcileCreateScopeErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
