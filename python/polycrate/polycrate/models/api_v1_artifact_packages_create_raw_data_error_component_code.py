from typing import Literal

ApiV1ArtifactPackagesCreateRawDataErrorComponentCode = Literal["invalid"]

API_V1_ARTIFACT_PACKAGES_CREATE_RAW_DATA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactPackagesCreateRawDataErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_artifact_packages_create_raw_data_error_component_code(
    value: str,
) -> ApiV1ArtifactPackagesCreateRawDataErrorComponentCode:
    if value in API_V1_ARTIFACT_PACKAGES_CREATE_RAW_DATA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_CREATE_RAW_DATA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
