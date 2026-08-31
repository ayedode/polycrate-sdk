from typing import Literal

ApiV1OrganizationsReconcileCreateKindErrorComponentAttr = Literal["kind"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsReconcileCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_organizations_reconcile_create_kind_error_component_attr(
    value: str,
) -> ApiV1OrganizationsReconcileCreateKindErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
