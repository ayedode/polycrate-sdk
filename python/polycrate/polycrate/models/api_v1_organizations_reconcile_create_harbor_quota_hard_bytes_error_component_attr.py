from typing import Literal

ApiV1OrganizationsReconcileCreateHarborQuotaHardBytesErrorComponentAttr = Literal["harbor_quota_hard_bytes"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_HARBOR_QUOTA_HARD_BYTES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsReconcileCreateHarborQuotaHardBytesErrorComponentAttr
] = {
    "harbor_quota_hard_bytes",
}


def check_api_v1_organizations_reconcile_create_harbor_quota_hard_bytes_error_component_attr(
    value: str,
) -> ApiV1OrganizationsReconcileCreateHarborQuotaHardBytesErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_HARBOR_QUOTA_HARD_BYTES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_HARBOR_QUOTA_HARD_BYTES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
