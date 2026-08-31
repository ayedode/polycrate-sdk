from typing import Literal

ApiV1OrganizationsDiscoverCreateUnifiedHarborCredentialErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_UNIFIED_HARBOR_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsDiscoverCreateUnifiedHarborCredentialErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_organizations_discover_create_unified_harbor_credential_error_component_code(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateUnifiedHarborCredentialErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_UNIFIED_HARBOR_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_UNIFIED_HARBOR_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
