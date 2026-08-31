from typing import Literal

ApiV1OrganizationsArchiveCreateHarborQuotaUpdatedAtErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "overflow"
]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_HARBOR_QUOTA_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsArchiveCreateHarborQuotaUpdatedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_organizations_archive_create_harbor_quota_updated_at_error_component_code(
    value: str,
) -> ApiV1OrganizationsArchiveCreateHarborQuotaUpdatedAtErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_HARBOR_QUOTA_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_HARBOR_QUOTA_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
