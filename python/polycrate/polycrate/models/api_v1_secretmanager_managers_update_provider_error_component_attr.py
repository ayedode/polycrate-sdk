from typing import Literal

ApiV1SecretmanagerManagersUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_SECRETMANAGER_MANAGERS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_secretmanager_managers_update_provider_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersUpdateProviderErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
