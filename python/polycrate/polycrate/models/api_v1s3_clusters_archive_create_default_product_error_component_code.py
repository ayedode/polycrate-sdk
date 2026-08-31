from typing import Literal

ApiV1S3ClustersArchiveCreateDefaultProductErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1S3_CLUSTERS_ARCHIVE_CREATE_DEFAULT_PRODUCT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3ClustersArchiveCreateDefaultProductErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1s3_clusters_archive_create_default_product_error_component_code(
    value: str,
) -> ApiV1S3ClustersArchiveCreateDefaultProductErrorComponentCode:
    if value in API_V1S3_CLUSTERS_ARCHIVE_CREATE_DEFAULT_PRODUCT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_ARCHIVE_CREATE_DEFAULT_PRODUCT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
