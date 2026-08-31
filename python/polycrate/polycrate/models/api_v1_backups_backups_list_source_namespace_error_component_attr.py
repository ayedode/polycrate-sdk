from typing import Literal

ApiV1BackupsBackupsListSourceNamespaceErrorComponentAttr = Literal["source_namespace"]

API_V1_BACKUPS_BACKUPS_LIST_SOURCE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsListSourceNamespaceErrorComponentAttr
] = {
    "source_namespace",
}


def check_api_v1_backups_backups_list_source_namespace_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsListSourceNamespaceErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_LIST_SOURCE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_LIST_SOURCE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
