from typing import Literal

ApiV1OrganizationsPartialUpdateHarborQuotaUsedBytesErrorComponentAttr = Literal["harbor_quota_used_bytes"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_HARBOR_QUOTA_USED_BYTES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsPartialUpdateHarborQuotaUsedBytesErrorComponentAttr
] = {
    "harbor_quota_used_bytes",
}


def check_api_v1_organizations_partial_update_harbor_quota_used_bytes_error_component_attr(
    value: str,
) -> ApiV1OrganizationsPartialUpdateHarborQuotaUsedBytesErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_HARBOR_QUOTA_USED_BYTES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_HARBOR_QUOTA_USED_BYTES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
