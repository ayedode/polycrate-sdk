from typing import Literal

ApiV1ArtifactsCreateLicenseErrorComponentAttr = Literal["license"]

API_V1_ARTIFACTS_CREATE_LICENSE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ArtifactsCreateLicenseErrorComponentAttr] = {
    "license",
}


def check_api_v1_artifacts_create_license_error_component_attr(
    value: str,
) -> ApiV1ArtifactsCreateLicenseErrorComponentAttr:
    if value in API_V1_ARTIFACTS_CREATE_LICENSE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_CREATE_LICENSE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
