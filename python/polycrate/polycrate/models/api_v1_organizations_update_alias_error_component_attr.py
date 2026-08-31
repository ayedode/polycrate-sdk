from typing import Literal

ApiV1OrganizationsUpdateAliasErrorComponentAttr = Literal["alias"]

API_V1_ORGANIZATIONS_UPDATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1OrganizationsUpdateAliasErrorComponentAttr] = {
    "alias",
}


def check_api_v1_organizations_update_alias_error_component_attr(
    value: str,
) -> ApiV1OrganizationsUpdateAliasErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_UPDATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
