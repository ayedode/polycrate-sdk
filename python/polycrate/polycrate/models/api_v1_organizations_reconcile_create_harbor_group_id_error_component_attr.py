from typing import Literal

ApiV1OrganizationsReconcileCreateHarborGroupIdErrorComponentAttr = Literal["harbor_group_id"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_HARBOR_GROUP_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsReconcileCreateHarborGroupIdErrorComponentAttr
] = {
    "harbor_group_id",
}


def check_api_v1_organizations_reconcile_create_harbor_group_id_error_component_attr(
    value: str,
) -> ApiV1OrganizationsReconcileCreateHarborGroupIdErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_HARBOR_GROUP_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_HARBOR_GROUP_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
