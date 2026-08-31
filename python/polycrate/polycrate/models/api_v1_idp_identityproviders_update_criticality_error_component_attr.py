from typing import Literal

ApiV1IdpIdentityprovidersUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_IDP_IDENTITYPROVIDERS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_idp_identityproviders_update_criticality_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersUpdateCriticalityErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
