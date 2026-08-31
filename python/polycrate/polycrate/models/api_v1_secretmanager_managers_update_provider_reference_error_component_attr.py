from typing import Literal

ApiV1SecretmanagerManagersUpdateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_SECRETMANAGER_MANAGERS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersUpdateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_secretmanager_managers_update_provider_reference_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersUpdateProviderReferenceErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
