from typing import Literal

ApiV1OrganizationsCreateAliasErrorComponentAttr = Literal["alias"]

API_V1_ORGANIZATIONS_CREATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1OrganizationsCreateAliasErrorComponentAttr] = {
    "alias",
}


def check_api_v1_organizations_create_alias_error_component_attr(
    value: str,
) -> ApiV1OrganizationsCreateAliasErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_CREATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
