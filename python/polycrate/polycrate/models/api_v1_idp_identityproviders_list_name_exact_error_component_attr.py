from typing import Literal

ApiV1IdpIdentityprovidersListNameExactErrorComponentAttr = Literal["name_exact"]

API_V1_IDP_IDENTITYPROVIDERS_LIST_NAME_EXACT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersListNameExactErrorComponentAttr
] = {
    "name_exact",
}


def check_api_v1_idp_identityproviders_list_name_exact_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersListNameExactErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_LIST_NAME_EXACT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_LIST_NAME_EXACT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
