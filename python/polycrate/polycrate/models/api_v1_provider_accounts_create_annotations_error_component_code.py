from typing import Literal

ApiV1ProviderAccountsCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_PROVIDER_ACCOUNTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProviderAccountsCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_provider_accounts_create_annotations_error_component_code(
    value: str,
) -> ApiV1ProviderAccountsCreateAnnotationsErrorComponentCode:
    if value in API_V1_PROVIDER_ACCOUNTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
