from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="S3BucketRegionRequest")


@_attrs_define
class S3BucketRegionRequest:
    """Serializer für Bucket-Erstellung mit Region-UUID.

    Accepts `region` as a workspaces.Region UUID (write-only) — resolves via
    region.legacy_s3_cluster to the backing S3Cluster. The bucket's region FK
    is NOT set at creation time; it is populated lazily by ensure_region() in
    reconciliation (Spec 333 Phase 2b).
    Falls back to SystemConfig.default_s3_bucket_cluster when region is omitted.
    Agent tokens: workspace/organization auto-assigned via perform_create().
    Regular users: workspace/organization required in request body.

        Attributes:
            name (str):
            region (None | Unset | UUID): UUID of the workspaces.Region where the bucket should be created. If omitted, the
                system default S3 cluster is used.
            organization (None | Unset | UUID): The ID of the organisation that owns this bucket
            workspace (None | Unset | UUID):
            labels (Any | Unset):
            annotations (Any | Unset):
            cors_allow_all (bool | Unset): Apply a permissive CORS configuration to this bucket. Only effective for Ceph
                clusters.
    """

    name: str
    region: None | Unset | UUID = UNSET
    organization: None | Unset | UUID = UNSET
    workspace: None | Unset | UUID = UNSET
    labels: Any | Unset = UNSET
    annotations: Any | Unset = UNSET
    cors_allow_all: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        elif isinstance(self.region, UUID):
            region = str(self.region)
        else:
            region = self.region

        organization: None | str | Unset
        if isinstance(self.organization, Unset):
            organization = UNSET
        elif isinstance(self.organization, UUID):
            organization = str(self.organization)
        else:
            organization = self.organization

        workspace: None | str | Unset
        if isinstance(self.workspace, Unset):
            workspace = UNSET
        elif isinstance(self.workspace, UUID):
            workspace = str(self.workspace)
        else:
            workspace = self.workspace

        labels = self.labels

        annotations = self.annotations

        cors_allow_all = self.cors_allow_all

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if region is not UNSET:
            field_dict["region"] = region
        if organization is not UNSET:
            field_dict["organization"] = organization
        if workspace is not UNSET:
            field_dict["workspace"] = workspace
        if labels is not UNSET:
            field_dict["labels"] = labels
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if cors_allow_all is not UNSET:
            field_dict["cors_allow_all"] = cors_allow_all

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.region, Unset):
            if isinstance(self.region, UUID):
                files.append(("region", (None, str(self.region), "text/plain")))
            else:
                files.append(("region", (None, str(self.region).encode(), "text/plain")))

        if not isinstance(self.organization, Unset):
            if isinstance(self.organization, UUID):
                files.append(("organization", (None, str(self.organization), "text/plain")))
            else:
                files.append(("organization", (None, str(self.organization).encode(), "text/plain")))

        if not isinstance(self.workspace, Unset):
            if isinstance(self.workspace, UUID):
                files.append(("workspace", (None, str(self.workspace), "text/plain")))
            else:
                files.append(("workspace", (None, str(self.workspace).encode(), "text/plain")))

        if not isinstance(self.labels, Unset):
            files.append(("labels", (None, str(self.labels).encode(), "text/plain")))

        if not isinstance(self.annotations, Unset):
            files.append(("annotations", (None, str(self.annotations).encode(), "text/plain")))

        if not isinstance(self.cors_allow_all, Unset):
            files.append(("cors_allow_all", (None, str(self.cors_allow_all).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_region(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                region_type_0 = UUID(data)

                return region_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        region = _parse_region(d.pop("region", UNSET))

        def _parse_organization(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                organization_type_0 = UUID(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        organization = _parse_organization(d.pop("organization", UNSET))

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

        cors_allow_all = d.pop("cors_allow_all", UNSET)

        s3_bucket_region_request = cls(
            name=name,
            region=region,
            organization=organization,
            workspace=workspace,
            labels=labels,
            annotations=annotations,
            cors_allow_all=cors_allow_all,
        )

        s3_bucket_region_request.additional_properties = d
        return s3_bucket_region_request

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
