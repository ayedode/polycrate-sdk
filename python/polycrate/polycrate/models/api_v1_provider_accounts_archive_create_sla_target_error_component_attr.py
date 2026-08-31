from typing import Literal

ApiV1ProviderAccountsArchiveCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsArchiveCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_provider_accounts_archive_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsArchiveCreateSlaTargetErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
