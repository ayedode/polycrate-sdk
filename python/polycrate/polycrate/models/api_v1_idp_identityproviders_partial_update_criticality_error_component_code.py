from typing import Literal

ApiV1IdpIdentityprovidersPartialUpdateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IdpIdentityprovidersPartialUpdateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_idp_identityproviders_partial_update_criticality_error_component_code(
    value: str,
) -> ApiV1IdpIdentityprovidersPartialUpdateCriticalityErrorComponentCode:
    if value in API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
