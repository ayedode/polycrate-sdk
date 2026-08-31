from typing import Literal

ApiV1OrganizationsReconcileCreatePriorityErrorComponentAttr = Literal["priority"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_PRIORITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsReconcileCreatePriorityErrorComponentAttr
] = {
    "priority",
}


def check_api_v1_organizations_reconcile_create_priority_error_component_attr(
    value: str,
) -> ApiV1OrganizationsReconcileCreatePriorityErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_PRIORITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_PRIORITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
