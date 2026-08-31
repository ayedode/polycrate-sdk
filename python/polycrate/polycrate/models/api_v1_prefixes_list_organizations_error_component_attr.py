from typing import Literal

ApiV1PrefixesListOrganizationsErrorComponentAttr = Literal["organizations"]

API_V1_PREFIXES_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PrefixesListOrganizationsErrorComponentAttr
] = {
    "organizations",
}


def check_api_v1_prefixes_list_organizations_error_component_attr(
    value: str,
) -> ApiV1PrefixesListOrganizationsErrorComponentAttr:
    if value in API_V1_PREFIXES_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
