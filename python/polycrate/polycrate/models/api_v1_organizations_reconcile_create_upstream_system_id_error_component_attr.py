from typing import Literal

ApiV1OrganizationsReconcileCreateUpstreamSystemIdErrorComponentAttr = Literal["upstream_system_id"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_UPSTREAM_SYSTEM_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsReconcileCreateUpstreamSystemIdErrorComponentAttr
] = {
    "upstream_system_id",
}


def check_api_v1_organizations_reconcile_create_upstream_system_id_error_component_attr(
    value: str,
) -> ApiV1OrganizationsReconcileCreateUpstreamSystemIdErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_UPSTREAM_SYSTEM_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_UPSTREAM_SYSTEM_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
