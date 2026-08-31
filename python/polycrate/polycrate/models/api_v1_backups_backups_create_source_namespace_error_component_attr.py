from typing import Literal

ApiV1BackupsBackupsCreateSourceNamespaceErrorComponentAttr = Literal["source_namespace"]

API_V1_BACKUPS_BACKUPS_CREATE_SOURCE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsCreateSourceNamespaceErrorComponentAttr
] = {
    "source_namespace",
}


def check_api_v1_backups_backups_create_source_namespace_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsCreateSourceNamespaceErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_CREATE_SOURCE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_CREATE_SOURCE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
