from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.last_state_enum import LastStateEnum, check_last_state_enum

if TYPE_CHECKING:
    from ..models.organization_simple import OrganizationSimple
    from ..models.region_simple import RegionSimple
    from ..models.s3_bucket_region_response_credential_type_0 import S3BucketRegionResponseCredentialType0
    from ..models.s3_credential import S3Credential
    from ..models.workspace_simple import WorkspaceSimple


T = TypeVar("T", bound="S3BucketRegionResponse")


@_attrs_define
class S3BucketRegionResponse:
    """Read-only response serializer for S3Bucket create endpoint.

    Attributes:
        id (UUID):
        name (str):
        region (RegionSimple):
        organization (OrganizationSimple): Simple Organization serializer for nested representations.

            Includes `url` field for direct navigation.
        workspace (WorkspaceSimple):
        labels (Any):
        annotations (Any):
        user_id (None | str):
        credential (None | S3BucketRegionResponseCredentialType0):
        access_keys (list[S3Credential]):
        state (LastStateEnum): * `OK` - Ok
            * `WARNING` - Warning
            * `CRITICAL` - Critical
            * `READY` - Ready
            * `DEGRADED` - Degraded
            * `DOWN` - Down
        conditions (Any): Conditions are managed by the API and will be added during the reconcile phase. Some
            conditions are `degrading`, meaning an object becomes DEGRADED if it has such a condition.
        reconciliation_running (bool):
        provider_reference (None | str):
        current_usage (int): Size in KB
        current_object_count (int):
        cors_allow_all (bool): Apply a permissive CORS configuration to this bucket. Only effective for Ceph clusters.
    """

    id: UUID
    name: str
    region: RegionSimple
    organization: OrganizationSimple
    workspace: WorkspaceSimple
    labels: Any
    annotations: Any
    user_id: None | str
    credential: None | S3BucketRegionResponseCredentialType0
    access_keys: list[S3Credential]
    state: LastStateEnum
    conditions: Any
    reconciliation_running: bool
    provider_reference: None | str
    current_usage: int
    current_object_count: int
    cors_allow_all: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.s3_bucket_region_response_credential_type_0 import S3BucketRegionResponseCredentialType0

        id = str(self.id)

        name = self.name

        region = self.region.to_dict()

        organization = self.organization.to_dict()

        workspace = self.workspace.to_dict()

        labels = self.labels

        annotations = self.annotations

        user_id: None | str
        user_id = self.user_id

        credential: dict[str, Any] | None
        if isinstance(self.credential, S3BucketRegionResponseCredentialType0):
            credential = self.credential.to_dict()
        else:
            credential = self.credential

        access_keys = []
        for access_keys_item_data in self.access_keys:
            access_keys_item = access_keys_item_data.to_dict()
            access_keys.append(access_keys_item)

        state: str = self.state

        conditions = self.conditions

        reconciliation_running = self.reconciliation_running

        provider_reference: None | str
        provider_reference = self.provider_reference

        current_usage = self.current_usage

        current_object_count = self.current_object_count

        cors_allow_all = self.cors_allow_all

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "region": region,
                "organization": organization,
                "workspace": workspace,
                "labels": labels,
                "annotations": annotations,
                "user_id": user_id,
                "credential": credential,
                "access_keys": access_keys,
                "state": state,
                "conditions": conditions,
                "reconciliation_running": reconciliation_running,
                "provider_reference": provider_reference,
                "current_usage": current_usage,
                "current_object_count": current_object_count,
                "cors_allow_all": cors_allow_all,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_simple import OrganizationSimple
        from ..models.region_simple import RegionSimple
        from ..models.s3_bucket_region_response_credential_type_0 import S3BucketRegionResponseCredentialType0
        from ..models.s3_credential import S3Credential
        from ..models.workspace_simple import WorkspaceSimple

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        region = RegionSimple.from_dict(d.pop("region"))

        organization = OrganizationSimple.from_dict(d.pop("organization"))

        workspace = WorkspaceSimple.from_dict(d.pop("workspace"))

        labels = d.pop("labels")

        annotations = d.pop("annotations")

        def _parse_user_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        user_id = _parse_user_id(d.pop("user_id"))

        def _parse_credential(data: object) -> None | S3BucketRegionResponseCredentialType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credential_type_0 = S3BucketRegionResponseCredentialType0.from_dict(data)

                return credential_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | S3BucketRegionResponseCredentialType0, data)

        credential = _parse_credential(d.pop("credential"))

        access_keys = []
        _access_keys = d.pop("access_keys")
        for access_keys_item_data in _access_keys:
            access_keys_item = S3Credential.from_dict(access_keys_item_data)

            access_keys.append(access_keys_item)

        state = check_last_state_enum(d.pop("state"))

        conditions = d.pop("conditions")

        reconciliation_running = d.pop("reconciliation_running")

        def _parse_provider_reference(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        provider_reference = _parse_provider_reference(d.pop("provider_reference"))

        current_usage = d.pop("current_usage")

        current_object_count = d.pop("current_object_count")

        cors_allow_all = d.pop("cors_allow_all")

        s3_bucket_region_response = cls(
            id=id,
            name=name,
            region=region,
            organization=organization,
            workspace=workspace,
            labels=labels,
            annotations=annotations,
            user_id=user_id,
            credential=credential,
            access_keys=access_keys,
            state=state,
            conditions=conditions,
            reconciliation_running=reconciliation_running,
            provider_reference=provider_reference,
            current_usage=current_usage,
            current_object_count=current_object_count,
            cors_allow_all=cors_allow_all,
        )

        s3_bucket_region_response.additional_properties = d
        return s3_bucket_region_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
