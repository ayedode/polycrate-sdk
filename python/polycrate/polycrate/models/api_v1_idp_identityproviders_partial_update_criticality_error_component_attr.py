from typing import Literal

ApiV1IdpIdentityprovidersPartialUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersPartialUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_idp_identityproviders_partial_update_criticality_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersPartialUpdateCriticalityErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
