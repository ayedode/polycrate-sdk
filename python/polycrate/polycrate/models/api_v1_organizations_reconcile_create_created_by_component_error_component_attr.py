from typing import Literal

ApiV1OrganizationsReconcileCreateCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsReconcileCreateCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1_organizations_reconcile_create_created_by_component_error_component_attr(
    value: str,
) -> ApiV1OrganizationsReconcileCreateCreatedByComponentErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
