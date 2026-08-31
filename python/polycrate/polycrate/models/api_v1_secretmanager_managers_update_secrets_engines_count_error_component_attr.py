from typing import Literal

ApiV1SecretmanagerManagersUpdateSecretsEnginesCountErrorComponentAttr = Literal["secrets_engines_count"]

API_V1_SECRETMANAGER_MANAGERS_UPDATE_SECRETS_ENGINES_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersUpdateSecretsEnginesCountErrorComponentAttr
] = {
    "secrets_engines_count",
}


def check_api_v1_secretmanager_managers_update_secrets_engines_count_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersUpdateSecretsEnginesCountErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_UPDATE_SECRETS_ENGINES_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_UPDATE_SECRETS_ENGINES_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
