from typing import Literal

ApiV1ProviderAccountsCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_PROVIDER_ACCOUNTS_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_provider_accounts_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsCreateSlaTargetErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
