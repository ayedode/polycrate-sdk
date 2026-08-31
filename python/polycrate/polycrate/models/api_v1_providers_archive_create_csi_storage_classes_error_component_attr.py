from typing import Literal

ApiV1ProvidersArchiveCreateCsiStorageClassesErrorComponentAttr = Literal["csi_storage_classes"]

API_V1_PROVIDERS_ARCHIVE_CREATE_CSI_STORAGE_CLASSES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersArchiveCreateCsiStorageClassesErrorComponentAttr
] = {
    "csi_storage_classes",
}


def check_api_v1_providers_archive_create_csi_storage_classes_error_component_attr(
    value: str,
) -> ApiV1ProvidersArchiveCreateCsiStorageClassesErrorComponentAttr:
    if value in API_V1_PROVIDERS_ARCHIVE_CREATE_CSI_STORAGE_CLASSES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ARCHIVE_CREATE_CSI_STORAGE_CLASSES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
