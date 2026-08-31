from typing import Literal

ApiV1S3ClustersListKindItem = Literal["minio", "rook-ceph"]

API_V1S3_CLUSTERS_LIST_KIND_ITEM_VALUES: set[ApiV1S3ClustersListKindItem] = {
    "minio",
    "rook-ceph",
}


def check_api_v1s3_clusters_list_kind_item(value: str) -> ApiV1S3ClustersListKindItem:
    if value in API_V1S3_CLUSTERS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_LIST_KIND_ITEM_VALUES!r}")
