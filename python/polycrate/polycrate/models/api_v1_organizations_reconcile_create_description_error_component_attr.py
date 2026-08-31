from typing import Literal

ApiV1OrganizationsReconcileCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsReconcileCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_organizations_reconcile_create_description_error_component_attr(
    value: str,
) -> ApiV1OrganizationsReconcileCreateDescriptionErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
