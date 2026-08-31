from typing import Literal

ApiV1AlertroutersArchiveCreateLabelNamespaceErrorComponentAttr = Literal["label_namespace"]

API_V1_ALERTROUTERS_ARCHIVE_CREATE_LABEL_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersArchiveCreateLabelNamespaceErrorComponentAttr
] = {
    "label_namespace",
}


def check_api_v1_alertrouters_archive_create_label_namespace_error_component_attr(
    value: str,
) -> ApiV1AlertroutersArchiveCreateLabelNamespaceErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_ARCHIVE_CREATE_LABEL_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_ARCHIVE_CREATE_LABEL_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
