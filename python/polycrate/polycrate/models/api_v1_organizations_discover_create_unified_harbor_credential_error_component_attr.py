from typing import Literal

ApiV1OrganizationsDiscoverCreateUnifiedHarborCredentialErrorComponentAttr = Literal["unified_harbor_credential"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_UNIFIED_HARBOR_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateUnifiedHarborCredentialErrorComponentAttr
] = {
    "unified_harbor_credential",
}


def check_api_v1_organizations_discover_create_unified_harbor_credential_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateUnifiedHarborCredentialErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_UNIFIED_HARBOR_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_UNIFIED_HARBOR_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
