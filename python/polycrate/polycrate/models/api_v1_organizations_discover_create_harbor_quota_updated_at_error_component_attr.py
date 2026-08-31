from typing import Literal

ApiV1OrganizationsDiscoverCreateHarborQuotaUpdatedAtErrorComponentAttr = Literal["harbor_quota_updated_at"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_HARBOR_QUOTA_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateHarborQuotaUpdatedAtErrorComponentAttr
] = {
    "harbor_quota_updated_at",
}


def check_api_v1_organizations_discover_create_harbor_quota_updated_at_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateHarborQuotaUpdatedAtErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_HARBOR_QUOTA_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_HARBOR_QUOTA_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
