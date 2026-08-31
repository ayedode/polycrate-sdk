from typing import Literal

ApiV1ProviderAccountsCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_PROVIDER_ACCOUNTS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_provider_accounts_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
