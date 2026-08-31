from typing import Literal

ApiV1SecretmanagerManagersPartialUpdateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersPartialUpdateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_secretmanager_managers_partial_update_provider_reference_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersPartialUpdateProviderReferenceErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
