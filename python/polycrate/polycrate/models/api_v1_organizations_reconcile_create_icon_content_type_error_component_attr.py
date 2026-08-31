from typing import Literal

ApiV1OrganizationsReconcileCreateIconContentTypeErrorComponentAttr = Literal["icon_content_type"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_ICON_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsReconcileCreateIconContentTypeErrorComponentAttr
] = {
    "icon_content_type",
}


def check_api_v1_organizations_reconcile_create_icon_content_type_error_component_attr(
    value: str,
) -> ApiV1OrganizationsReconcileCreateIconContentTypeErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_ICON_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_ICON_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
