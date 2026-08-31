from typing import Literal

ApiV1IdpIdentityprovidersListCreatedByUsersErrorComponentAttr = Literal["created_by_users"]

API_V1_IDP_IDENTITYPROVIDERS_LIST_CREATED_BY_USERS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersListCreatedByUsersErrorComponentAttr
] = {
    "created_by_users",
}


def check_api_v1_idp_identityproviders_list_created_by_users_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersListCreatedByUsersErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_LIST_CREATED_BY_USERS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_LIST_CREATED_BY_USERS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
