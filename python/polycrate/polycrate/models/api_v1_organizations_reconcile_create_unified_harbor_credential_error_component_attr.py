from typing import Literal

ApiV1OrganizationsReconcileCreateUnifiedHarborCredentialErrorComponentAttr = Literal["unified_harbor_credential"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_UNIFIED_HARBOR_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsReconcileCreateUnifiedHarborCredentialErrorComponentAttr
] = {
    "unified_harbor_credential",
}


def check_api_v1_organizations_reconcile_create_unified_harbor_credential_error_component_attr(
    value: str,
) -> ApiV1OrganizationsReconcileCreateUnifiedHarborCredentialErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_UNIFIED_HARBOR_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_UNIFIED_HARBOR_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
