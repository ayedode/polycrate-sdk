from typing import Literal

ApiV1OrganizationsReconcileCreateCachedEndpointCountErrorComponentAttr = Literal["cached_endpoint_count"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_CACHED_ENDPOINT_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsReconcileCreateCachedEndpointCountErrorComponentAttr
] = {
    "cached_endpoint_count",
}


def check_api_v1_organizations_reconcile_create_cached_endpoint_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsReconcileCreateCachedEndpointCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_CACHED_ENDPOINT_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_CACHED_ENDPOINT_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
