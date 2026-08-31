from typing import Literal

RegionS3ConfigKindEnum = Literal["minio", "rook-ceph"]

REGION_S3_CONFIG_KIND_ENUM_VALUES: set[RegionS3ConfigKindEnum] = {
    "minio",
    "rook-ceph",
}


def check_region_s3_config_kind_enum(value: str) -> RegionS3ConfigKindEnum:
    if value in REGION_S3_CONFIG_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REGION_S3_CONFIG_KIND_ENUM_VALUES!r}")
