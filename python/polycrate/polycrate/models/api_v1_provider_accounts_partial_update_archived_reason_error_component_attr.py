from typing import Literal

ApiV1ProviderAccountsPartialUpdateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsPartialUpdateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_provider_accounts_partial_update_archived_reason_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsPartialUpdateArchivedReasonErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
