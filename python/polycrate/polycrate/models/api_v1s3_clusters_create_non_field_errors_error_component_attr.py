from typing import Literal

ApiV1S3ClustersCreateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1S3_CLUSTERS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersCreateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1s3_clusters_create_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1S3ClustersCreateNonFieldErrorsErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
