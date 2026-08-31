from typing import Literal

ApiV1OrganizationsIconUploadCreateApmVmuserManifestLastAppliedSha256ErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_APM_VMUSER_MANIFEST_LAST_APPLIED_SHA_256_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsIconUploadCreateApmVmuserManifestLastAppliedSha256ErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_organizations_icon_upload_create_apm_vmuser_manifest_last_applied_sha_256_error_component_code(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateApmVmuserManifestLastAppliedSha256ErrorComponentCode:
    if (
        value
        in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_APM_VMUSER_MANIFEST_LAST_APPLIED_SHA_256_ERROR_COMPONENT_CODE_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_APM_VMUSER_MANIFEST_LAST_APPLIED_SHA_256_ERROR_COMPONENT_CODE_VALUES!r}"
    )
