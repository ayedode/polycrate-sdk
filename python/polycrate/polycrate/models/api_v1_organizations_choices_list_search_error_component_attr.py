from typing import Literal

ApiV1OrganizationsChoicesListSearchErrorComponentAttr = Literal["search"]

API_V1_ORGANIZATIONS_CHOICES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsChoicesListSearchErrorComponentAttr
] = {
    "search",
}


def check_api_v1_organizations_choices_list_search_error_component_attr(
    value: str,
) -> ApiV1OrganizationsChoicesListSearchErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_CHOICES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CHOICES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
