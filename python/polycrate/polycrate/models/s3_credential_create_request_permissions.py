from typing import Literal

S3CredentialCreateRequestPermissions = Literal["full", "read", "readwrite", "write"]

S3_CREDENTIAL_CREATE_REQUEST_PERMISSIONS_VALUES: set[S3CredentialCreateRequestPermissions] = {
    "full",
    "read",
    "readwrite",
    "write",
}


def check_s3_credential_create_request_permissions(value: str) -> S3CredentialCreateRequestPermissions:
    if value in S3_CREDENTIAL_CREATE_REQUEST_PERMISSIONS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {S3_CREDENTIAL_CREATE_REQUEST_PERMISSIONS_VALUES!r}")
