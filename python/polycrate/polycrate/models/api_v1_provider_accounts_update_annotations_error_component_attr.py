from typing import Literal

ApiV1ProviderAccountsUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_PROVIDER_ACCOUNTS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_provider_accounts_update_annotations_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
