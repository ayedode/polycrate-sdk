from typing import Literal

ApiV1SecretmanagerManagersPartialUpdateSecretsEnginesCountErrorComponentAttr = Literal["secrets_engines_count"]

API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_SECRETS_ENGINES_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersPartialUpdateSecretsEnginesCountErrorComponentAttr
] = {
    "secrets_engines_count",
}


def check_api_v1_secretmanager_managers_partial_update_secrets_engines_count_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersPartialUpdateSecretsEnginesCountErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_SECRETS_ENGINES_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_SECRETS_ENGINES_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
