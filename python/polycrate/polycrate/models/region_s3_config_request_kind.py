from typing import Literal

RegionS3ConfigRequestKind = Literal["minio", "rook-ceph"]

REGION_S3_CONFIG_REQUEST_KIND_VALUES: set[RegionS3ConfigRequestKind] = {
    "minio",
    "rook-ceph",
}


def check_region_s3_config_request_kind(value: str) -> RegionS3ConfigRequestKind:
    if value in REGION_S3_CONFIG_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REGION_S3_CONFIG_REQUEST_KIND_VALUES!r}")
