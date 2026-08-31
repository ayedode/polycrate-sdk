from typing import Literal

ApiV1IdpIdentityprovidersListOrganizationsErrorComponentAttr = Literal["organizations"]

API_V1_IDP_IDENTITYPROVIDERS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersListOrganizationsErrorComponentAttr
] = {
    "organizations",
}


def check_api_v1_idp_identityproviders_list_organizations_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersListOrganizationsErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
