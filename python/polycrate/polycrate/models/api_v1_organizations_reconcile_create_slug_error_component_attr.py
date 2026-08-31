from typing import Literal

ApiV1OrganizationsReconcileCreateSlugErrorComponentAttr = Literal["slug"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_SLUG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsReconcileCreateSlugErrorComponentAttr
] = {
    "slug",
}


def check_api_v1_organizations_reconcile_create_slug_error_component_attr(
    value: str,
) -> ApiV1OrganizationsReconcileCreateSlugErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_SLUG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_SLUG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
