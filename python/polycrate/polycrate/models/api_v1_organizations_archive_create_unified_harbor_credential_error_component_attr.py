from typing import Literal

ApiV1OrganizationsArchiveCreateUnifiedHarborCredentialErrorComponentAttr = Literal["unified_harbor_credential"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_UNIFIED_HARBOR_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsArchiveCreateUnifiedHarborCredentialErrorComponentAttr
] = {
    "unified_harbor_credential",
}


def check_api_v1_organizations_archive_create_unified_harbor_credential_error_component_attr(
    value: str,
) -> ApiV1OrganizationsArchiveCreateUnifiedHarborCredentialErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_UNIFIED_HARBOR_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_UNIFIED_HARBOR_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
