from typing import Literal

ApiV1ProviderAccountsUpdateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_PROVIDER_ACCOUNTS_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsUpdateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_provider_accounts_update_sla_availability_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsUpdateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
