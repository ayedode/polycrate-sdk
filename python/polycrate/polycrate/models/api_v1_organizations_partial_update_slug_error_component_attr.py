from typing import Literal

ApiV1OrganizationsPartialUpdateSlugErrorComponentAttr = Literal["slug"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_SLUG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsPartialUpdateSlugErrorComponentAttr
] = {
    "slug",
}


def check_api_v1_organizations_partial_update_slug_error_component_attr(
    value: str,
) -> ApiV1OrganizationsPartialUpdateSlugErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_SLUG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_SLUG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
