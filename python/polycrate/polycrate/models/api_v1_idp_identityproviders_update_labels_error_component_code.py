from typing import Literal

ApiV1IdpIdentityprovidersUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_IDP_IDENTITYPROVIDERS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IdpIdentityprovidersUpdateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_idp_identityproviders_update_labels_error_component_code(
    value: str,
) -> ApiV1IdpIdentityprovidersUpdateLabelsErrorComponentCode:
    if value in API_V1_IDP_IDENTITYPROVIDERS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
