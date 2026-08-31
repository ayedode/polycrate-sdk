from typing import Literal

ApiV1ProviderAccountsArchiveCreateLastReconciliationDurationSecondsErrorComponentCode = Literal[
    "invalid", "max_string_length"
]

API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProviderAccountsArchiveCreateLastReconciliationDurationSecondsErrorComponentCode
] = {
    "invalid",
    "max_string_length",
}


def check_api_v1_provider_accounts_archive_create_last_reconciliation_duration_seconds_error_component_code(
    value: str,
) -> ApiV1ProviderAccountsArchiveCreateLastReconciliationDurationSecondsErrorComponentCode:
    if (
        value
        in API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_CODE_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
