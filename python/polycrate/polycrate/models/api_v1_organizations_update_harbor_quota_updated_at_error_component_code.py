from typing import Literal

ApiV1OrganizationsUpdateHarborQuotaUpdatedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_ORGANIZATIONS_UPDATE_HARBOR_QUOTA_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsUpdateHarborQuotaUpdatedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_organizations_update_harbor_quota_updated_at_error_component_code(
    value: str,
) -> ApiV1OrganizationsUpdateHarborQuotaUpdatedAtErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_UPDATE_HARBOR_QUOTA_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_HARBOR_QUOTA_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
