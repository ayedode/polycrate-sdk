from typing import Literal

ApiV1OrganizationsReconcileCreateDomainsErrorComponentAttr = Literal["domains"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_DOMAINS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsReconcileCreateDomainsErrorComponentAttr
] = {
    "domains",
}


def check_api_v1_organizations_reconcile_create_domains_error_component_attr(
    value: str,
) -> ApiV1OrganizationsReconcileCreateDomainsErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_DOMAINS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_DOMAINS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
