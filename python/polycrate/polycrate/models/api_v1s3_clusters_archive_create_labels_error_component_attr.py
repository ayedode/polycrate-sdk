from typing import Literal

ApiV1S3ClustersArchiveCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1S3_CLUSTERS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersArchiveCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1s3_clusters_archive_create_labels_error_component_attr(
    value: str,
) -> ApiV1S3ClustersArchiveCreateLabelsErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
