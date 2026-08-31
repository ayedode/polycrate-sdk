from typing import Literal

ApiV1OrganizationsPartialUpdateHarborQuotaUpdatedAtErrorComponentAttr = Literal["harbor_quota_updated_at"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_HARBOR_QUOTA_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsPartialUpdateHarborQuotaUpdatedAtErrorComponentAttr
] = {
    "harbor_quota_updated_at",
}


def check_api_v1_organizations_partial_update_harbor_quota_updated_at_error_component_attr(
    value: str,
) -> ApiV1OrganizationsPartialUpdateHarborQuotaUpdatedAtErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_HARBOR_QUOTA_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_HARBOR_QUOTA_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
