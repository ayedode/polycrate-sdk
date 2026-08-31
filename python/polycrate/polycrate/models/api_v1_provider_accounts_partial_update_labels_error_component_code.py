from typing import Literal

ApiV1ProviderAccountsPartialUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProviderAccountsPartialUpdateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_provider_accounts_partial_update_labels_error_component_code(
    value: str,
) -> ApiV1ProviderAccountsPartialUpdateLabelsErrorComponentCode:
    if value in API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
