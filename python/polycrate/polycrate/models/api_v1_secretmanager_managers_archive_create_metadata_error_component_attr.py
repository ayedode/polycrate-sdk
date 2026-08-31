from typing import Literal

ApiV1SecretmanagerManagersArchiveCreateMetadataErrorComponentAttr = Literal["metadata"]

API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersArchiveCreateMetadataErrorComponentAttr
] = {
    "metadata",
}


def check_api_v1_secretmanager_managers_archive_create_metadata_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersArchiveCreateMetadataErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
