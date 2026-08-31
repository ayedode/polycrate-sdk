from typing import Literal

ApiV1ArtifactPackagesUpdateRawDataErrorComponentAttr = Literal["raw_data"]

API_V1_ARTIFACT_PACKAGES_UPDATE_RAW_DATA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesUpdateRawDataErrorComponentAttr
] = {
    "raw_data",
}


def check_api_v1_artifact_packages_update_raw_data_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesUpdateRawDataErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_UPDATE_RAW_DATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_UPDATE_RAW_DATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
