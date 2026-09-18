from typing import Literal

ApiV1OrganizationsChoicesListSlugErrorComponentAttr = Literal["slug"]

API_V1_ORGANIZATIONS_CHOICES_LIST_SLUG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsChoicesListSlugErrorComponentAttr
] = {
    "slug",
}


def check_api_v1_organizations_choices_list_slug_error_component_attr(
    value: str,
) -> ApiV1OrganizationsChoicesListSlugErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_CHOICES_LIST_SLUG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CHOICES_LIST_SLUG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
