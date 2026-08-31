from typing import Literal

ApiV1ProviderAccountsUpdateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_PROVIDER_ACCOUNTS_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsUpdateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_provider_accounts_update_slo_target_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsUpdateSloTargetErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
