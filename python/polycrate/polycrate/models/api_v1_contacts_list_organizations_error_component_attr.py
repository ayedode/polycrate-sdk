from typing import Literal

ApiV1ContactsListOrganizationsErrorComponentAttr = Literal["organizations"]

API_V1_CONTACTS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactsListOrganizationsErrorComponentAttr
] = {
    "organizations",
}


def check_api_v1_contacts_list_organizations_error_component_attr(
    value: str,
) -> ApiV1ContactsListOrganizationsErrorComponentAttr:
    if value in API_V1_CONTACTS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
