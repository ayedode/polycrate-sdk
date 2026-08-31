from typing import Literal

ApiV1OrganizationsReconcileCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsReconcileCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_organizations_reconcile_create_criticality_error_component_attr(
    value: str,
) -> ApiV1OrganizationsReconcileCreateCriticalityErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
