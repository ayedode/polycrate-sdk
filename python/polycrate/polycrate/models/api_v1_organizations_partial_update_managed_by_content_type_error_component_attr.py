from typing import Literal

ApiV1OrganizationsPartialUpdateManagedByContentTypeErrorComponentAttr = Literal["managed_by_content_type"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsPartialUpdateManagedByContentTypeErrorComponentAttr
] = {
    "managed_by_content_type",
}


def check_api_v1_organizations_partial_update_managed_by_content_type_error_component_attr(
    value: str,
) -> ApiV1OrganizationsPartialUpdateManagedByContentTypeErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
