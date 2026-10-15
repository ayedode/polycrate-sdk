from typing import Literal

RegionS3ConfigKind = Literal["minio", "rook-ceph"]

REGION_S3_CONFIG_KIND_VALUES: set[RegionS3ConfigKind] = {
    "minio",
    "rook-ceph",
}


def check_region_s3_config_kind(value: str) -> RegionS3ConfigKind:
    if value in REGION_S3_CONFIG_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REGION_S3_CONFIG_KIND_VALUES!r}")
