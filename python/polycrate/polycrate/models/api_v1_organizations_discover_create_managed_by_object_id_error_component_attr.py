from typing import Literal

ApiV1OrganizationsDiscoverCreateManagedByObjectIdErrorComponentAttr = Literal["managed_by_object_id"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateManagedByObjectIdErrorComponentAttr
] = {
    "managed_by_object_id",
}


def check_api_v1_organizations_discover_create_managed_by_object_id_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateManagedByObjectIdErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
