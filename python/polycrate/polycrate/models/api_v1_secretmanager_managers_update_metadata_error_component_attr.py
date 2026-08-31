from typing import Literal

ApiV1SecretmanagerManagersUpdateMetadataErrorComponentAttr = Literal["metadata"]

API_V1_SECRETMANAGER_MANAGERS_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersUpdateMetadataErrorComponentAttr
] = {
    "metadata",
}


def check_api_v1_secretmanager_managers_update_metadata_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersUpdateMetadataErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
