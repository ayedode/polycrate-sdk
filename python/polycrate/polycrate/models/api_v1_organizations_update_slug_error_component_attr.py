from typing import Literal

ApiV1OrganizationsUpdateSlugErrorComponentAttr = Literal["slug"]

API_V1_ORGANIZATIONS_UPDATE_SLUG_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1OrganizationsUpdateSlugErrorComponentAttr] = {
    "slug",
}


def check_api_v1_organizations_update_slug_error_component_attr(
    value: str,
) -> ApiV1OrganizationsUpdateSlugErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_UPDATE_SLUG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_SLUG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
