from typing import Literal

ApiV1OrganizationsDiscoverCreateApmVmuserManifestLastAppliedSha256ErrorComponentAttr = Literal[
    "apm_vmuser_manifest_last_applied_sha256"
]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_APM_VMUSER_MANIFEST_LAST_APPLIED_SHA_256_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateApmVmuserManifestLastAppliedSha256ErrorComponentAttr
] = {
    "apm_vmuser_manifest_last_applied_sha256",
}


def check_api_v1_organizations_discover_create_apm_vmuser_manifest_last_applied_sha_256_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateApmVmuserManifestLastAppliedSha256ErrorComponentAttr:
    if (
        value
        in API_V1_ORGANIZATIONS_DISCOVER_CREATE_APM_VMUSER_MANIFEST_LAST_APPLIED_SHA_256_ERROR_COMPONENT_ATTR_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_APM_VMUSER_MANIFEST_LAST_APPLIED_SHA_256_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
