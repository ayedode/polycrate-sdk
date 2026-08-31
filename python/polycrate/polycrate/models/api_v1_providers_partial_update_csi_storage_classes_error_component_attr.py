from typing import Literal

ApiV1ProvidersPartialUpdateCsiStorageClassesErrorComponentAttr = Literal["csi_storage_classes"]

API_V1_PROVIDERS_PARTIAL_UPDATE_CSI_STORAGE_CLASSES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersPartialUpdateCsiStorageClassesErrorComponentAttr
] = {
    "csi_storage_classes",
}


def check_api_v1_providers_partial_update_csi_storage_classes_error_component_attr(
    value: str,
) -> ApiV1ProvidersPartialUpdateCsiStorageClassesErrorComponentAttr:
    if value in API_V1_PROVIDERS_PARTIAL_UPDATE_CSI_STORAGE_CLASSES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_PARTIAL_UPDATE_CSI_STORAGE_CLASSES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
