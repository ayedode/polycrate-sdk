from typing import Literal

ApiV1OrganizationsReconcileCreateHarborProjectIdErrorComponentAttr = Literal["harbor_project_id"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_HARBOR_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsReconcileCreateHarborProjectIdErrorComponentAttr
] = {
    "harbor_project_id",
}


def check_api_v1_organizations_reconcile_create_harbor_project_id_error_component_attr(
    value: str,
) -> ApiV1OrganizationsReconcileCreateHarborProjectIdErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_HARBOR_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_HARBOR_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
