from typing import Literal

ApiV1IdpIdentityprovidersPartialUpdateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IdpIdentityprovidersPartialUpdateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_idp_identityproviders_partial_update_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1IdpIdentityprovidersPartialUpdateReconciliationEnabledErrorComponentCode:
    if value in API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
