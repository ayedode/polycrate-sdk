from typing import Literal

ApiV1ProviderAccountsUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_PROVIDER_ACCOUNTS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProviderAccountsUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_provider_accounts_update_annotations_error_component_code(
    value: str,
) -> ApiV1ProviderAccountsUpdateAnnotationsErrorComponentCode:
    if value in API_V1_PROVIDER_ACCOUNTS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
