from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.region_simple import RegionSimple


T = TypeVar("T", bound="S3BucketUpdate")


@_attrs_define
class S3BucketUpdate:
    """
    Attributes:
        id (UUID):
        name (str):
        reconciliation_running (bool):
        region (RegionSimple):
        organization (None | UUID): The ID of the organisation that owns this bucket
        provider_reference (None | str):
        credential (None | UUID):
        workspace (None | Unset | UUID):
        labels (Any | Unset):
        annotations (Any | Unset):
        include_in_cost_statement (bool | Unset): When False, this bucket is omitted from CostStatement generation even
            if the cluster is included. Cluster-level False still excludes the bucket.
        cors_allow_all (bool | Unset): Apply a permissive CORS configuration to this bucket. Only effective for Ceph
            clusters.
    """

    id: UUID
    name: str
    reconciliation_running: bool
    region: RegionSimple
    organization: None | UUID
    provider_reference: None | str
    credential: None | UUID
    workspace: None | Unset | UUID = UNSET
    labels: Any | Unset = UNSET
    annotations: Any | Unset = UNSET
    include_in_cost_statement: bool | Unset = UNSET
    cors_allow_all: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        reconciliation_running = self.reconciliation_running

        region = self.region.to_dict()

        organization: None | str
        if isinstance(self.organization, UUID):
            organization = str(self.organization)
        else:
            organization = self.organization

        provider_reference: None | str
        provider_reference = self.provider_reference

        credential: None | str
        if isinstance(self.credential, UUID):
            credential = str(self.credential)
        else:
            credential = self.credential

        workspace: None | str | Unset
        if isinstance(self.workspace, Unset):
            workspace = UNSET
        elif isinstance(self.workspace, UUID):
            workspace = str(self.workspace)
        else:
            workspace = self.workspace

        labels = self.labels

        annotations = self.annotations

        include_in_cost_statement = self.include_in_cost_statement

        cors_allow_all = self.cors_allow_all

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "reconciliation_running": reconciliation_running,
                "region": region,
                "organization": organization,
                "provider_reference": provider_reference,
                "credential": credential,
            }
        )
        if workspace is not UNSET:
            field_dict["workspace"] = workspace
        if labels is not UNSET:
            field_dict["labels"] = labels
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if include_in_cost_statement is not UNSET:
            field_dict["include_in_cost_statement"] = include_in_cost_statement
        if cors_allow_all is not UNSET:
            field_dict["cors_allow_all"] = cors_allow_all

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.region_simple import RegionSimple

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        reconciliation_running = d.pop("reconciliation_running")

        region = RegionSimple.from_dict(d.pop("region"))

        def _parse_organization(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                organization_type_0 = UUID(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        organization = _parse_organization(d.pop("organization"))

        def _parse_provider_reference(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        provider_reference = _parse_provider_reference(d.pop("provider_reference"))

        def _parse_credential(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                credential_type_0 = UUID(data)

                return credential_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        credential = _parse_credential(d.pop("credential"))

        def _parse_workspace(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                workspace_type_0 = UUID(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        workspace = _parse_workspace(d.pop("workspace", UNSET))

        labels = d.pop("labels", UNSET)

        annotations = d.pop("annotations", UNSET)

        include_in_cost_statement = d.pop("include_in_cost_statement", UNSET)

        cors_allow_all = d.pop("cors_allow_all", UNSET)

        s3_bucket_update = cls(
            id=id,
            name=name,
            reconciliation_running=reconciliation_running,
            region=region,
            organization=organization,
            provider_reference=provider_reference,
            credential=credential,
            workspace=workspace,
            labels=labels,
            annotations=annotations,
            include_in_cost_statement=include_in_cost_statement,
            cors_allow_all=cors_allow_all,
        )

        s3_bucket_update.additional_properties = d
        return s3_bucket_update

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
