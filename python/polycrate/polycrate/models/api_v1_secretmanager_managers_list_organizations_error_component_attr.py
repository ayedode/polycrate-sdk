from typing import Literal

ApiV1SecretmanagerManagersListOrganizationsErrorComponentAttr = Literal["organizations"]

API_V1_SECRETMANAGER_MANAGERS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersListOrganizationsErrorComponentAttr
] = {
    "organizations",
}


def check_api_v1_secretmanager_managers_list_organizations_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersListOrganizationsErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
