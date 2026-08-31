from typing import Literal

ApiV1ProviderAccountsArchiveCreateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsArchiveCreateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_provider_accounts_archive_create_slo_availability_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsArchiveCreateSloAvailabilityErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
