from typing import Literal

ApiV1OrganizationsDiscoverCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_organizations_discover_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateArchivedAtErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
