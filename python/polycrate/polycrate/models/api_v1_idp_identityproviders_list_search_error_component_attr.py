from typing import Literal

ApiV1IdpIdentityprovidersListSearchErrorComponentAttr = Literal["search"]

API_V1_IDP_IDENTITYPROVIDERS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersListSearchErrorComponentAttr
] = {
    "search",
}


def check_api_v1_idp_identityproviders_list_search_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersListSearchErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
