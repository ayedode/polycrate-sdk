from typing import Literal

ApiV1OrganizationsReconcileCreateColorErrorComponentAttr = Literal["color"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_COLOR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsReconcileCreateColorErrorComponentAttr
] = {
    "color",
}


def check_api_v1_organizations_reconcile_create_color_error_component_attr(
    value: str,
) -> ApiV1OrganizationsReconcileCreateColorErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_COLOR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_COLOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
