from typing import Literal

ApiV1OrganizationsReconcileCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsReconcileCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_organizations_reconcile_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1OrganizationsReconcileCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
