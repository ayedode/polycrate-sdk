from typing import Literal

ApiV1IdpIdentityprovidersUpdateReconciliationEnabledErrorComponentAttr = Literal["reconciliation_enabled"]

API_V1_IDP_IDENTITYPROVIDERS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersUpdateReconciliationEnabledErrorComponentAttr
] = {
    "reconciliation_enabled",
}


def check_api_v1_idp_identityproviders_update_reconciliation_enabled_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersUpdateReconciliationEnabledErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
