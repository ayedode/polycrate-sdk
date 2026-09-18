from typing import Literal

ApiV1OrganizationsListSlugErrorComponentAttr = Literal["slug"]

API_V1_ORGANIZATIONS_LIST_SLUG_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1OrganizationsListSlugErrorComponentAttr] = {
    "slug",
}


def check_api_v1_organizations_list_slug_error_component_attr(
    value: str,
) -> ApiV1OrganizationsListSlugErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_LIST_SLUG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_LIST_SLUG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
