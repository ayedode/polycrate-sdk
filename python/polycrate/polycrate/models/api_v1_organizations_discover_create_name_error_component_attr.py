from typing import Literal

ApiV1OrganizationsDiscoverCreateNameErrorComponentAttr = Literal["name"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_organizations_discover_create_name_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateNameErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
