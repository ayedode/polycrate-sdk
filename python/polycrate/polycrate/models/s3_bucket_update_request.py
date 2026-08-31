from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="S3BucketUpdateRequest")


@_attrs_define
class S3BucketUpdateRequest:
    """
    Attributes:
        workspace (None | Unset | UUID):
        labels (Any | Unset):
        annotations (Any | Unset):
        include_in_cost_statement (bool | Unset): When False, this bucket is omitted from CostStatement generation even
            if the cluster is included. Cluster-level False still excludes the bucket.
        cors_allow_all (bool | Unset): Apply a permissive CORS configuration to this bucket. Only effective for Ceph
            clusters.
    """

    workspace: None | Unset | UUID = UNSET
    labels: Any | Unset = UNSET
    annotations: Any | Unset = UNSET
    include_in_cost_statement: bool | Unset = UNSET
    cors_allow_all: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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
        field_dict.update({})
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

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.workspace, Unset):
            if isinstance(self.workspace, UUID):
                files.append(("workspace", (None, str(self.workspace), "text/plain")))
            else:
                files.append(("workspace", (None, str(self.workspace).encode(), "text/plain")))

        if not isinstance(self.labels, Unset):
            files.append(("labels", (None, str(self.labels).encode(), "text/plain")))

        if not isinstance(self.annotations, Unset):
            files.append(("annotations", (None, str(self.annotations).encode(), "text/plain")))

        if not isinstance(self.include_in_cost_statement, Unset):
            files.append(
                ("include_in_cost_statement", (None, str(self.include_in_cost_statement).encode(), "text/plain"))
            )

        if not isinstance(self.cors_allow_all, Unset):
            files.append(("cors_allow_all", (None, str(self.cors_allow_all).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        s3_bucket_update_request = cls(
            workspace=workspace,
            labels=labels,
            annotations=annotations,
            include_in_cost_statement=include_in_cost_statement,
            cors_allow_all=cors_allow_all,
        )

        s3_bucket_update_request.additional_properties = d
        return s3_bucket_update_request

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
