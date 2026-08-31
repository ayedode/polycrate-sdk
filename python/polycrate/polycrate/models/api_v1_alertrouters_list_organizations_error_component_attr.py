from typing import Literal

ApiV1AlertroutersListOrganizationsErrorComponentAttr = Literal["organizations"]

API_V1_ALERTROUTERS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersListOrganizationsErrorComponentAttr
] = {
    "organizations",
}


def check_api_v1_alertrouters_list_organizations_error_component_attr(
    value: str,
) -> ApiV1AlertroutersListOrganizationsErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
