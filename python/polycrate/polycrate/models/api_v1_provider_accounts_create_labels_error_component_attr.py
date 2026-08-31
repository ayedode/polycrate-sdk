from typing import Literal

ApiV1ProviderAccountsCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_PROVIDER_ACCOUNTS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_provider_accounts_create_labels_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsCreateLabelsErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
