from typing import Literal

ApiV1OrganizationsPartialUpdateApmVmuserManifestLastAppliedSha256ErrorComponentAttr = Literal[
    "apm_vmuser_manifest_last_applied_sha256"
]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_APM_VMUSER_MANIFEST_LAST_APPLIED_SHA_256_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsPartialUpdateApmVmuserManifestLastAppliedSha256ErrorComponentAttr
] = {
    "apm_vmuser_manifest_last_applied_sha256",
}


def check_api_v1_organizations_partial_update_apm_vmuser_manifest_last_applied_sha_256_error_component_attr(
    value: str,
) -> ApiV1OrganizationsPartialUpdateApmVmuserManifestLastAppliedSha256ErrorComponentAttr:
    if (
        value
        in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_APM_VMUSER_MANIFEST_LAST_APPLIED_SHA_256_ERROR_COMPONENT_ATTR_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_APM_VMUSER_MANIFEST_LAST_APPLIED_SHA_256_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
