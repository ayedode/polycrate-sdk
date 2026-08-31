from typing import Literal

ApiV1SecretmanagerManagersUpdateMetadataErrorComponentCode = Literal["invalid", "null"]

API_V1_SECRETMANAGER_MANAGERS_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1SecretmanagerManagersUpdateMetadataErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_secretmanager_managers_update_metadata_error_component_code(
    value: str,
) -> ApiV1SecretmanagerManagersUpdateMetadataErrorComponentCode:
    if value in API_V1_SECRETMANAGER_MANAGERS_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
