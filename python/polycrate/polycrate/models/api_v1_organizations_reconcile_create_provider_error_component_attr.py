from typing import Literal

ApiV1OrganizationsReconcileCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsReconcileCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_organizations_reconcile_create_provider_error_component_attr(
    value: str,
) -> ApiV1OrganizationsReconcileCreateProviderErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
