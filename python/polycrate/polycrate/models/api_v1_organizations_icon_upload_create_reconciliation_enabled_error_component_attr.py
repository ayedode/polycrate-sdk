from typing import Literal

ApiV1OrganizationsIconUploadCreateReconciliationEnabledErrorComponentAttr = Literal["reconciliation_enabled"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateReconciliationEnabledErrorComponentAttr
] = {
    "reconciliation_enabled",
}


def check_api_v1_organizations_icon_upload_create_reconciliation_enabled_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateReconciliationEnabledErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
