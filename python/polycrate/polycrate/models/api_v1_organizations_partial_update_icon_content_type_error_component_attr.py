from typing import Literal

ApiV1OrganizationsPartialUpdateIconContentTypeErrorComponentAttr = Literal["icon_content_type"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_ICON_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsPartialUpdateIconContentTypeErrorComponentAttr
] = {
    "icon_content_type",
}


def check_api_v1_organizations_partial_update_icon_content_type_error_component_attr(
    value: str,
) -> ApiV1OrganizationsPartialUpdateIconContentTypeErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_ICON_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_ICON_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
