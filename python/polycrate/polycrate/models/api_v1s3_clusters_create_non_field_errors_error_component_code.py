from typing import Literal

ApiV1S3ClustersCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null", "unique"]

API_V1S3_CLUSTERS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3ClustersCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
    "unique",
}


def check_api_v1s3_clusters_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1S3ClustersCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1S3_CLUSTERS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
