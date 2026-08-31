from typing import Literal

ApiV1SecretmanagerManagersPartialUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersPartialUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_secretmanager_managers_partial_update_provider_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersPartialUpdateProviderErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
