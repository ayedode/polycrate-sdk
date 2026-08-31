from typing import Literal

ApiV1IdpIdentityprovidersPartialUpdateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersPartialUpdateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_idp_identityproviders_partial_update_archived_at_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersPartialUpdateArchivedAtErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
