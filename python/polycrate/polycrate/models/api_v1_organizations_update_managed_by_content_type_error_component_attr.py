from typing import Literal

ApiV1OrganizationsUpdateManagedByContentTypeErrorComponentAttr = Literal["managed_by_content_type"]

API_V1_ORGANIZATIONS_UPDATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsUpdateManagedByContentTypeErrorComponentAttr
] = {
    "managed_by_content_type",
}


def check_api_v1_organizations_update_managed_by_content_type_error_component_attr(
    value: str,
) -> ApiV1OrganizationsUpdateManagedByContentTypeErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_UPDATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
