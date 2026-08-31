from typing import Literal

ApiV1OrganizationsReconcileCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsReconcileCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_organizations_reconcile_create_archived_error_component_attr(
    value: str,
) -> ApiV1OrganizationsReconcileCreateArchivedErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
