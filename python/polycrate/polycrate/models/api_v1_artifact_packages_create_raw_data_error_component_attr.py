from typing import Literal

ApiV1ArtifactPackagesCreateRawDataErrorComponentAttr = Literal["raw_data"]

API_V1_ARTIFACT_PACKAGES_CREATE_RAW_DATA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesCreateRawDataErrorComponentAttr
] = {
    "raw_data",
}


def check_api_v1_artifact_packages_create_raw_data_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesCreateRawDataErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_CREATE_RAW_DATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_CREATE_RAW_DATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
