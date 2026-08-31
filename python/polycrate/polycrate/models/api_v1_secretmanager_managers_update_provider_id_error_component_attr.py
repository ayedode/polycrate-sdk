from typing import Literal

ApiV1SecretmanagerManagersUpdateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_SECRETMANAGER_MANAGERS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersUpdateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_secretmanager_managers_update_provider_id_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersUpdateProviderIdErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
