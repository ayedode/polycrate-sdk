from typing import Literal

ApiV1OrganizationsIconUploadCreateLastReconciliationDurationSecondsErrorComponentAttr = Literal[
    "last_reconciliation_duration_seconds"
]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateLastReconciliationDurationSecondsErrorComponentAttr
] = {
    "last_reconciliation_duration_seconds",
}


def check_api_v1_organizations_icon_upload_create_last_reconciliation_duration_seconds_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateLastReconciliationDurationSecondsErrorComponentAttr:
    if (
        value
        in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_ATTR_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
